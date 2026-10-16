"""Read-only preflight for the design catalog and autonomous prototype profile."""

import argparse
import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASK_ID = r"M\d+(?:[AB]|-NET)?-\d+"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_dag(edges):
    visited, active = set(), set()

    def visit(key):
        require(key in edges, f"Missing dependency: {key}")
        require(key not in active, f"Dependency cycle: {key}")
        if key in visited:
            return
        active.add(key)
        for dependency in edges[key]:
            visit(dependency)
        active.remove(key)
        visited.add(key)

    for key in edges:
        visit(key)


def validate_catalog(catalog):
    nodes = catalog["nodes"]
    by_id = {node["id"]: node for node in nodes}
    require(len(nodes) == len(by_id) == 162, "Expected 162 unique catalog nodes")
    require(len({node["tree"] for node in nodes}) == 29, "Expected 29 trees")
    require(len(catalog["synergies"]) == 12, "Expected 12 synergies")
    require(len({s["id"] for s in catalog["synergies"]}) == 12, "Duplicate synergy ID")
    metadata = catalog["metadata"]
    require((metadata["node_count"], metadata["tree_count"], metadata["synergy_count"]) == (162, 29, 12), "Catalog metadata counts mismatch")
    require(metadata["approved_for_runtime"] is False, "Raw catalog must not enable runtime")
    edges = {}
    for node in nodes:
        key = node["id"]
        require(node["tier"] in range(6), f"Invalid tier: {key}")
        require(node["implementation_status"] == "design_only", f"Use runtime manifest for readiness: {key}")
        require(all(value is None for value in node["combat_runtime"].values()), f"Keep runtime stats separate: {key}")
        tier = catalog["tier_rules"][str(node["tier"])]
        require(node["level_requirement"] == tier["min_level"], f"Tier level mismatch: {key}")
        require(node["cost_proposal"]["skill_points"] == tier["skill_points"], f"Tier SP mismatch: {key}")
        require(node["cost_proposal"]["ryo"] == tier["ryo"], f"Tier Ryo mismatch: {key}")
        groups = node["requires_any"]
        require(all(isinstance(group, list) and group for group in groups), f"Empty OR group: {key}")
        edges[key] = node["requires_all"] + [ref for group in groups for ref in group]
        has_gate = node["unlock_gate"] is not None
        require((node["gate_id"] is not None) == has_gate, f"Invalid gate ID: {key}")
        state = "requires_implementation" if has_gate else "none"
        require(node["access"]["gate_state"] == state, f"Invalid raw gate state: {key}")
    validate_dag(edges)
    for synergy in catalog["synergies"]:
        for ref in synergy["input_refs"]:
            kind = ref["kind"]
            require(kind in {"skill_id", "element_token"}, f"Invalid synergy ref kind: {kind}")
            targets = by_id if kind == "skill_id" else catalog["element_tokens"]
            require(ref["value"] in targets, f"Invalid synergy reference: {ref}")
    return by_id


def validate_profile(profile, catalog, by_id):
    rules = profile["fixed_rules"]
    selected = profile["owner_selected_test_values"]
    defaults = profile["tunable_defaults"]
    scope = profile["content_scope"]
    config = catalog["match_config_proposal"]
    require(rules["player_count"] == config["player_count"] == 2, "Player count must be two")
    require(rules["combat_exit_seconds"] == config["combat_exit_seconds"] == 5, "Combat exit must be 5s")
    require(rules["skill_point_budget"] == config["skill_points_per_match"] == 12, "SP budget must be 12")
    require(rules["clan"] == "Uchiha" and rules["chakra_nature"] == "FIRE", "Initial content must remain Uchiha/FIRE")
    require(rules["level_cap"] == 20 and rules["target_match_minutes"] == [20, 25], "Fixed level/duration target changed")
    require((rules["active_slots"], rules["ultimate_slots"], rules["passive_slots"]) == (4, 1, 3), "Wrong slot counts")
    require((rules["substitution_starting_scrolls"], rules["substitution_max_scrolls"]) == (1, 2), "Wrong scroll limits")
    for key in ("solo_respawn", "capture_points", "disconnect_auto_eliminates", "final_zone_has_safe_area", "hard_timeout", "substitution_blocks_new_damage_or_effects", "drop_xp_sp_ryo_or_learned_nodes"):
        require(rules[key] is False, f"Fixed rule must remain false: {key}")
    for key in ("substitution_is_passive", "substitution_triggers_on_zone_damage", "substitution_cleanses_existing_negative_effects", "stealth_breaks_on_dealt_or_received_damage", "drop_all_carried_items_on_elimination"):
        require(rules[key] is True, f"Fixed rule must remain true: {key}")
    require(rules["simultaneous_elimination_result"] == "draw", "Same-tick elimination must draw")
    require(rules["pity_misses_to_choice"] == 4, "Pity must trigger on fourth miss")
    sub = (selected["substitution_hp_fraction_after_trigger"], selected["substitution_stealth_seconds"], selected["substitution_cooldown_seconds"])
    require(sub == (0.25, 3, 60), "Owner substitution test values changed")
    pity = (selected["pity_min_target_max_hp_damage_fraction"], selected["pity_contribution_window_seconds"])
    require(pity == (0.05, 30), "Owner pity test values changed")
    grants = defaults["sp_grants_by_level_1_to_20"]
    require(len(grants) == 20 and sum(grants) == 12 and all(isinstance(v, int) and v >= 0 for v in grants), "Invalid SP schedule")
    planned = scope["planned_node_ids"]
    allowed = set(planned)
    require(len(planned) == len(allowed) == 22, "Expected 22 unique planned IDs")
    require(allowed <= by_id.keys(), "Planned IDs missing from catalog")
    require(scope["runtime_enabled_by_this_file"] is False, "Profile must not enable runtime")
    for key in planned:
        node = by_id[key]
        require(set(node["requires_all"]) <= allowed, f"Missing planned prerequisite: {key}")
        require(all(set(group) <= allowed for group in node["requires_any"]), f"Missing planned OR prerequisite: {key}")
    costs = []
    for preset in ("fire_preset_targets", "illusion_preset_targets"):
        learned = set()

        def collect(key):
            require(key in allowed, f"Preset node outside scope: {key}")
            if key in learned:
                return
            learned.add(key)
            require(not by_id[key]["requires_any"], f"Preset needs explicit OR choice: {key}")
            for parent in by_id[key]["requires_all"]:
                collect(parent)

        for key in scope[preset]:
            collect(key)
        sp = sum(by_id[key]["cost_proposal"]["skill_points"] for key in learned)
        ryo = sum(by_id[key]["cost_proposal"]["ryo"] for key in learned)
        require(sp <= rules["skill_point_budget"], f"Preset exceeds SP: {preset}")
        costs.append((preset, sp, ryo))
    durations = defaults["zone_phase_durations_seconds"]
    radii = defaults["zone_phase_target_radii_world_units"]
    damage = defaults["zone_phase_damage_max_hp_fraction_per_tick"]
    require(len(durations) == len(radii) == len(damage) and bool(durations), "Zone arrays mismatch")
    low, high = rules["target_match_minutes"]
    require(low * 60 <= sum(durations) <= high * 60, "Zone timing outside target range")
    require(all(value > 0 for value in durations), "Invalid zone phase duration")
    previous = [defaults["zone_initial_radius_world_units"]] + radii[:-1]
    require(all(a > b >= 0 for a, b in zip(previous, radii)) and radii[-1] == 0, "Zone must shrink to zero")
    require(all(0 < a <= b for a, b in zip(damage, damage[1:])), "Zone damage must increase")
    for key, value in defaults.items():
        if key.endswith("_probability"):
            require(0 <= value <= 1, f"Invalid probability: {key}")
    require(0 < defaults["snapshot_hz"] <= defaults["simulation_tick_hz"], "Invalid tick rates")
    require(defaults["simulation_tick_hz"] % defaults["snapshot_hz"] == 0, "Snapshot rate must divide simulation rate")
    return costs


def validate_documents():
    paths = [ROOT / "AGENTS.md", ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]
    for path in paths:
        text = path.read_text(encoding="utf-8-sig")
        require(len(re.findall(r"^```", text, re.M)) % 2 == 0, f"Unbalanced fences: {path.name}")
        for block in re.findall(r"^```json\s*\n(.*?)^```", text, re.M | re.S):
            json.loads(block)
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            target = link.strip("<>").split("#")[0]
            if target and not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                require((path.parent / target).exists(), f"Broken link: {path.name}: {target}")
    text = (ROOT / "docs/TASK_BACKLOG.md").read_text(encoding="utf-8")
    edges = {}
    for part in re.split(r"^### ", text, flags=re.M)[1:]:
        match = re.match(rf"({TASK_ID}) ", part)
        require(match is not None, "Unrecognized task header")
        key = match[1]
        require(key not in edges, f"Duplicate task: {key}")
        dependency = re.search(r"^\*\*[^*]+:\*\* (.*)", part, re.M)
        require(dependency is not None, f"Missing dependency line: {key}")
        edges[key] = re.findall(rf"\b{TASK_ID}\b", dependency[1])
        require(len(re.findall(r"^- ", part, re.M)) >= 3, f"Missing acceptance checks: {key}")
    require(len(edges) == 34, "Expected 34 task IDs; update contract explicitly if scope changes")
    validate_dag(edges)
    return len(paths)


def self_test(profile, catalog, by_id):
    bad = copy.deepcopy(profile)
    bad["tunable_defaults"]["sp_grants_by_level_1_to_20"][0] += 1
    missing = copy.deepcopy(profile)
    missing["content_scope"]["planned_node_ids"].remove("FIRE_ROOT")
    missing["content_scope"]["planned_node_ids"].append("BASE_SENSOR")
    for fixture in (bad, missing):
        try:
            validate_profile(fixture, catalog, by_id)
        except ValueError:
            continue
        raise ValueError("Invalid profile fixture was accepted")
    try:
        validate_dag({"A": ["B"], "B": ["A"]})
    except ValueError:
        return
    raise ValueError("Cycle fixture was accepted")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        catalog = json.loads((ROOT / "data/skills/skills.json").read_text(encoding="utf-8-sig"))
        profile = json.loads((ROOT / "data/prototypes/solo_first_playable.json").read_text(encoding="utf-8-sig"))
        nodes = validate_catalog(catalog)
        costs = validate_profile(profile, catalog, nodes)
        document_count = validate_documents()
        if args.self_test:
            self_test(profile, catalog, nodes)
        print("PASS: catalog 162 nodes / 29 trees / 12 synergies; prototype 22 planned IDs")
        print("PASS: presets (SP, base Ryo before modifiers):", costs)
        print(f"PASS: {document_count} Markdown files; links/JSON examples; 34 tasks, no cycles")
        print("PASS: invalid-profile and cycle fixtures" if args.self_test else "INFO: use --self-test for negative fixtures")
        print("INFO: static preflight only; no gameplay, image generation, Godot or Android test claimed")
        return 0
    except (ValueError, KeyError, TypeError, OSError, RecursionError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
