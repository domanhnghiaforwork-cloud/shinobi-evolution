# DEVELOPMENT_ROADMAP.md — Lộ trình cho người mới Vibe Code

**Game:** Shinobi Evolution • **Ngày:** 2026-10-16 • **Status:** `PLANNED; nothing implemented yet`.

> Mục đích: chia game lớn thành những feature có thể chạy và kiểm được. **Antigravity code chính; Codex review chỉ đọc; người dùng duyệt và kiểm thử bằng Godot + điện thoại Android.** Kết quả chưa được thực hiện không được đánh dấu `DONE`.

## 1. Bắc đẩu của dự án (north star)

- **Vision:** PvPvE sinh tồn lai MOBA, chọn gia tộc ở sảnh, build nhẫn thuật không giới hạn tuyến cố định, farm XP/Ryō/loot, săn boss, giao tranh trên bản đồ rộng.
- **Visual:** 2D HD Pixel Art nhịp hành động gợi Wizard of Legend; camera top-down 3/4, Android landscape, sprite/tiles nearest-neighbor, UI touch.
- **Tech:** Godot 4 Standard/GDScript, VS Code, Antigravity main dev, Codex code review, Git/GitHub.
- **Design input:** 162 node/29 tree/12 synergy là catalog, **chưa phải 162 skill lập trình hoàn chỉnh**.
- **Mốc game đích:** 18 người/6 đội 3, 42 phút, boss/ba phong ấn/Hạch Trận, skill T0–T5. Đây là tầm nhìn, **không phải scope để agent làm ngay**.

## 2. Trạng thái chuẩn

- `PLANNED`: chưa bắt đầu, chỉ có tài liệu.
- `READY`: đã có acceptance criteria, phụ thuộc và test plan; người dùng cho phép triển khai.
- `IN_PROGRESS`: Antigravity đang code task cụ thể.
- `REVIEW`: Codex đang kiểm tra diff.
- `QA`: người dùng chạy Godot/Android để kiểm chứng.
- `DONE`: đáp ứng DoD và được người dùng chấp thuận.
- `BLOCKED`: thiếu tài liệu/asset/thiết bị/điều kiện, không được tự đóng.

**Tất cả milestone dưới đây đều khởi đầu ở `PLANNED`.** Không gán thời gian hứa hẹn theo ngày/tuần khi chưa có tốc độ phát triển thực tế; các "buổi" chỉ là thứ tự học việc.

## 3. Roadmap theo cổng (gated delivery)

| Cổng | Milestone | Sản phẩm test được | Phụ thuộc | Trạng thái |
|---|---|---|---|---|
| M0 | Dev Environment | tạo project, chạy Godot, Git checkpoint, VS Code extension | — | PLANNED |
| M1 | Ninja Movement | map placeholder, player, camera, WASD/8-way & collision | M0 | PLANNED |
| M2 | Mobile Input & Pixel Art | joystick 2 ngón, HUD, sprite 4/8 hướng, APK chạy | M1 | PLANNED |
| M3 | Core Combat | HP/Chakra, attack, dodge, hitbox, damage, 2 quái | M2 | PLANNED |
| M4 | Skill Graph Engine | load/validate JSON, unlock T0–T2, trang bị, UI graph | M3 | PLANNED |
| M5 | PvE Economy & Loot | XP/Ryō/SP, elite, cuộn, pity test, farm progression | M4 | PLANNED |
| M6 | Vertical Slice Offline | 3 clan + 3 hệ, boss, 24–36 node, 2 synergy, 1 objective | M5 | PLANNED |
| M7 | Networking Spike | 2 client + 1 server, movement reconciliation, secure hit/loot | M6 | PLANNED |
| M8 | Multiplayer Playtest | 6 người, lobby test, quái & boss sync, objectives | M7 | PLANNED |
| M9 | Alpha Content & Map | 6 clan, 5 hệ, 60–80 node, 8–12 người | M8 | PLANNED |
| M10 | Beta Target & Hardening | 10 clan, tối đa 162 node đã duyệt, 18 người, full map | M9 | PLANNED |

**Đường tắt không khuyến nghị:** nhảy M0 → M7 hoặc triển khai Nakama trước khi có gameplay offline hấp dẫn. **Được phép** thu nhỏ/phân lại milestone nếu benchmark hoặc khả năng triển khai yêu cầu; thay đổi scope phải phê duyệt.

## 4. Chi tiết các milestone và tiêu chí nghiệm thu

### M0 — Môi trường, Git, tài liệu

**Task giao Antigravity:** kiểm project hiện tại, pin engine version, kết nối VS Code, tạo cấu trúc tối thiểu, xác nhận tài liệu/skill JSON parse.

**DoD:**

- Godot 4 stable được tạo bằng Project Manager, `project.godot` hiện diện; mở Godot Editor không lỗi import.
- VS Code mở cùng thư mục project; có extension GDScript, Antigravity/Codex sẵn sàng.
- Git init và commit checkpoint **sau khi người dùng duyệt**; `.gitignore` có `.godot/` và builds, nhưng không loại asset nguồn.
- Sáu file trong bộ tài liệu được copy đúng đường dẫn; JSON UTF-8 parse hợp lệ.
- Antigravity ghi version Godot và công cụ local thực tế vào `ARCHITECTURE.md` sau khi kiểm tra; **không tự giả lập kết quả**.

**Codex review:** đường dẫn, ghi đè file, binary/secrets, tài liệu mâu thuẫn, JSON chưa đủ runtime không bị hiểu nhầm.

### M1 — Di chuyển ninja + camera (offline)

**Scope:** một player placeholder, map nhỏ có vật cản, camera theo actor, 8 hướng vector; keyboard debug.

**DoD:**

- Start game, dùng WASD/mũi tên di chuyển chuẩn 8 hướng, tốc độ chéo không nhanh hơn ngang.
- Camera theo nhân vật, không rung, không xuyên tường, không hụt collision trên frame rate khác nhau.
- Có `player.tscn`, `main.tscn`, `test_arena.tscn` cùng code module hóa, không hardcode script runtime vào UI.
- Godot chạy không báo lỗi parse; screen capture ít nhất một tình huống kiểm thử.

**Không làm:** hệ chakra hoàn chỉnh, quái AI phức tạp, online, skill tree.

### M2 — Android input + Pixel Art vertical look

**Scope:** joystick ảo trái, một nút action phải, thao tác đa chạm, safe area, sprite nhân vật pixel tạm + tiles.

**DoD:**

- Di chuyển bằng ngón trái, nút phải hoạt động **đồng thời**; thả ngón joystick về 0, không trôi nhân vật.
- Build APK debug test trên **ít nhất một thiết bị Android thật**; landscape không bị notch che HUD.
- Sprite nearest-neighbor không bị mờ, camera giữ world view hợp lý trên nhiều aspect ratio.
- Thử quality profile VFX nhẹ; ghi model/OS/resolution/FPS đo được, không báo 60FPS nếu chưa đo.

**Không làm:** đầy đủ VFX ninja tối thượng, tilemap thế giới mở vô hạn.

### M3 — Combat nền

**Scope:** HP, chakra, attack thường, 1 kỹ năng projectile, 1 kỹ năng area hoặc dash, cooldown, animation hit, quái chase cơ bản.

**DoD:**

- Hai quái test có HP, có thể tấn công/bị đánh, chết/respawn đúng; HP không âm; sprite hit có feedback.
- Cooldown/chakra bị kiểm trong domain, UI phản ánh dữ liệu, button spam không bypass cooldown.
- Enemy telegraph rõ hơn ally VFX; ít nhất một status (burn/slow) test TTL.
- Unit tests tối thiểu: trừ HP một lần, không hit team/self sai, cạn chakra từ chối cast.

**Không làm:** nhiều skill hardcoded dạng 162 ID, boss, PvP.

### M4 — Skill Graph + Catalog validator

**Scope:** parse `skills.json`, validator DAG và IDs, UI kỹ năng, học T0–T2 mẫu; loadout 1–2 active/Thế thân.

**DoD:**

- Validator xác nhận 162 node/29 cây/12 synergy; công bố chính xác lỗi missing/cycle nếu data hỏng.
- `requires_all` AND, `requires_any` OR-groups test bằng fixtures.
- **Gate có `requires_implementation` bị từ chối**, không bị auto-unlock; chỉ cho các gate đã explicit-resolve trong prototype.
- Người chơi có thể thấy vì sao skill locked, đủ/thiếu Ryō/SP; không trang bị/cast `design_only`.
- Thao tác chọn node dùng **touch**, không phụ thuộc hover PC.

**Không làm:** tự triển khai mọi skill vì hiển thị được graph, tự phát minh gate rank/huyết kế.

### M5 — Farming + vật phẩm điều kiện

**Scope:** quái thường/elite, XP/Ryō/SP, item inventory, loot group + bảo hiểm pity, nâng skill theo tier.

**DoD:**

- XP/Ryō/spend/trade được test trên domain; quái bị giết chỉ rơi phần thưởng **một lần**.
- Pity cùng loot group sau 4 lượt không được mảnh mục tiêu → cơ chế chọn mảnh phù hợp hoạt động nhất quán (làm rõ off-by-one trong test).
- Vật phẩm hiếm chỉ mở **điều kiện**, không bypass huyết kế/tier/SP/Ryō.
- Có ít nhất **một đường skill T4 thay thế** không lệ thuộc RNG; nếu chưa triển khai T4 hoàn chỉnh thì chứng minh bằng validator/simulation.

### M6 — Vertical slice playable offline

**Scope:** Uchiha/Hyūga/Nara, Hỏa/Lôi/Thổ, Thể + Phong ấn, 24–36 node được implement/approved theo tệp riêng, 2 synergy, 1 boss và 1 objective.

**DoD:**

- Có thể chơi từ lobby chọn clan tới trận, farm, nâng skill, đánh boss, kết thúc trận và quay về result.
- Mỗi clan có ≥2 hướng build hữu dụng; một build không auto thắng tất cả trường hợp trong playtest nội bộ.
- Tất cả skill đã implemented có chi phí, cooldown, telegraph, hitbox, test cơ bản.
- `T5` hiếm ngoài slice giữ disabled, không bị mua dù catalog có tên.
- Có dữ liệu gameplay: time to T3/T4, average Ryō/min, FPS trong fight, ít nhất 3 tình huống counterplay.

### M7 — Multiplayer proof of concept

**Scope:** một match server và 2 client, sync movement, ability, HP, loot, purchase, cooldown.

**DoD:**

- Hai client nhìn thấy cùng combat state; server từ chối giả mạo damage/mua T5 khi không đủ điều kiện.
- Chịu được disconnect/reconnect theo đặc tả thử, không dupe reward.
- Có log thời gian tick/network/late input; quyết định backend dựa trên kết quả thực.
- Đã test trên mạng không chỉ localhost ít nhất một tình huống latency mô phỏng.

**Decision gate:** chọn transport, Godot dedicated server, Nakama matchmaking hay phương án khác sau khi spike. Không khóa lựa chọn do AI thích thư viện nào.

### M8 — PvPvE 6 người

**Scope:** 2 đội x3 hoặc 3 đội x2 cho test; boss contested và một/tối thiểu các điểm mục tiêu; server authoritative.

**DoD:**

- 6 người sync quái/projectile/loot, không ăn thưởng đôi khi nhiều người đánh boss cùng lúc.
- PvP hit registration và stun/Thế thân hoạt động dưới latency mô phỏng.
- Mobile device stress test ghi p95 frame time, RAM, bandwidth; chỉnh budget clone/summon trước khi tăng người.
- Trận có điều kiện thắng rõ, không bị kẹt do player disconnect.

### M9 — Alpha

**Scope:** 6 clan, 5 nguyên tố, 60–80 node sau triển khai; 8–12 người nếu performance cho phép; map mở rộng, 3 boss, 3 điểm phong ấn.

**DoD:**

- Có QA regression theo toàn bộ clan/ability active, playtest thắng bằng mục tiêu không cần giết hết.
- Có chống snowball/pity analytics, nhiều tuyến farm; UI mobile mở graph không cản thao tác sống còn.
- Không P0/P1 trong cửa nghiệm thu; telemetry đủ phát hiện crash/disconnect và skill abuse.

### M10 — Beta target

**Scope:** 10 clan và mục tiêu full catalog 162 node **chỉ khi có đủ runtime/cân bằng**, 18 người mục tiêu, 42 phút, meta cosmetics/preset, rank/season nếu thật sự cần.

**DoD:**

- Tăng concurrency qua load test, không bằng suy đoán. Có giới hạn entity và VFX ngân sách thực nghiệm.
- Đã kiểm tra server authority, dữ liệu phiên bản, loadout exploit, reconnect, abuse RNG.
- Có lựa chọn IP rõ ràng trước marketing/store (license hoặc thế giới tự sáng tạo). Store policy, bảo mật, quyền riêng tư và thanh toán cần đánh giá riêng khi phát hành.
- Beta không đồng nghĩa game đã được duyệt thương mại.

## 5. Công việc đầu tiên đề nghị thực hiện ngay

**Chỉ thực hiện M0 + M1** trước; không cố xây nguyên một game bằng một prompt. Một chu trình feature:

```text
Người dùng tạo task (tiêu chí nghiệm thu rõ)
 → Antigravity đọc AGENTS + docs liên quan, lập plan
 → Người dùng duyệt phạm vi
 → Antigravity code + chạy kiểm tra
 → Git diff/checkpoint
 → Codex chỉ đọc diff và báo P0..P3
 → Antigravity sửa chính xác lỗi
 → Codex re-review
 → Người dùng chạy Godot/Android và duyệt
 → Commit, đổi trạng thái DONE
```

### Prompt Task 01 cho Antigravity

```text
Bạn là Main Developer dự án Shinobi Evolution. Đọc AGENTS.md,
docs/GAME_DESIGN.md, docs/ARCHITECTURE.md và
 docs/DEVELOPMENT_ROADMAP.md.

Thực hiện M1 sau khi kiểm tra M0 đã đủ: tạo game Godot 4 Standard
có Main scene, Player CharacterBody2D, Camera2D, map placeholder
có vật cản; di chuyển 8 hướng bằng keyboard và collision đúng.

Đưa plan + file sẽ sửa trước; không tự thêm multiplayer, skill tree,
Nakama, database, vũ trụ Naruto hay asset bên ngoài. Không tự commit.
Chạy kiểm thử khả thi và báo cáo những gì đã test/chưa test.
Dừng để Codex review sau khi hoàn thành.
```

### Prompt review cho Codex

```text
Bạn là reviewer độc lập. Đọc AGENTS.md + ARCHITECTURE.md
và review chỉ các file thay đổi của M1. KHÔNG sửa file.

Kiểm tra: Godot API hợp version, CharacterBody2D.move_and_slide,
InputMap, diagonal speed, camera, collision, leak, node paths,
scene dependencies, regression Android design, test coverage.

Báo P0/P1/P2/P3 với file/vị trí/kịch bản và cách sửa nhỏ nhất.
Kết luận PASS / NEEDS FIX / BLOCKED và danh sách smoke test.
```

## 6. Chuẩn quản lý công việc trong VS Code + Git

**Tên branch ví dụ:** `feature/m1-player-movement`, `feature/m3-combat-core`, `fix/m4-skill-gate`.

**Commit convention đề xuất:** `feat: player movement placeholder`, `fix: reject missing skill gate`, `test: validate skill graph`, `docs: clarify mobile hud`.

**Definition of Ready cho mỗi task:**

- Có user story, phạm vi và không-phạm-vi.
- Có đường dẫn file dự kiến và tài liệu nguồn.
- Có ít nhất 3 acceptance tests, nêu cách chạy/đầu ra kỳ vọng.
- Có rủi ro/điểm chưa quyết định; không tự suy đoán nếu thay gameplay.

**Definition of Done:**

- Antigravity bàn giao diff và test logs; Godot không lỗi blocker.
- Codex review xong; P0/P1 resolved; các P2 được xử lý hoặc Product Owner ghi nhận có chủ đích.
- Người dùng thử thực tế; chỉ khi đó chuyển `DONE`.
- Tài liệu đổi nếu interface/luật thay; checkpoint Git đã tạo sau phê duyệt.

## 7. Checklist chất lượng riêng cho mobile Pixel Art

- [ ] Dùng joystick và 1+ nút skill cùng lúc mà không mất pointer.
- [ ] Hướng sprite khi chạy chéo không nhấp nháy; va chạm không jitter.
- [ ] UI không che bởi camera notch/gesture bar; nút bấm đủ lớn cho ngón tay.
- [ ] Pixel sprite nearest không vỡ, không bị méo khi zoom; HUD text đọc được.
- [ ] Enemy telegraph thấy rõ dù 3 ninja cùng tung thuật; không phụ thuộc mỗi màu.
- [ ] Có quality `Low/Medium/High` cho VFX khi cần; camera shake/flash tắt được.
- [ ] Mục tiêu benchmark 30 FPS máy thấp và 60 FPS máy khuyến nghị **chỉ đánh dấu đạt sau đo trên thiết bị cụ thể**.
- [ ] RAM/CPU/battery/network khi 6 người giao tranh được ghi log sau M8.

## 8. Rủi ro chính và cách giảm

| Rủi ro | Dấu hiệu | Cách xử lý |
|---|---|---|
| Scope creep | AI tạo 162 skill trong một diff | giữ M1/M3/M4 tách biệt, mỗi feature có test |
| Spec mâu thuẫn | JSON có tên skill nhưng chưa gate/combats | fail-closed, đánh dấu draft, không tự điền stat |
| Mobile không dễ chơi | nút nhỏ, drag aim khó, hẹp tầm nhìn | prototype trên Android từ M2 |
| PvP lộ gian lận | client tự tăng XP/drop/damage | domain authority ngay offline, server từ M7 |
| Quái/particle quá nhiều | tụt FPS, RAM spike | profiler và entity/VFX budget theo class |
| Lore/IP sai | người nào cũng mở huyết kế hiếm | gate lore và kiểm giấy phép trước marketing |
| Review AI lan man | sửa lại toàn codebase sau mỗi task | review diff + file/line/repro + severity |
| Không có rollback | AI hỏng project và xóa asset | Git snapshot trước task, không reset/force push |
| Mạng di động không ổn định | disconnect/lag làm trùng thưởng | idempotency, reconnect, server authoritative |

## 9. Milestone chất lượng dữ liệu skill

| Mốc | Mục tiêu data | Khả năng thực thi |
|---|---|---|
| Ngay lúc bắt đầu | `skills.json`: 162 design nodes, refs hợp lệ | **đọc/tra cứu đồ thị, chưa chiến đấu** |
| M4 | gate validator + 3–5 kỹ năng mở hợp lệ | engine unlock, trang bị thử |
| M6 | 24–36 node đã duyệt + 8–12 ability thật được kiểm | full vertical slice |
| M9 | 60–80 implemented nodes | PvPvE alpha |
| M10 | up to 162 approved by content rollout | chỉ nếu runtime/balance QA đã đủ |

**Ghi chú:** số node và số active ability khác nhau. Một node có thể là tiến trình/root/passive, không nhất thiết cần một VFX riêng.

## 10. Decision Log / Change Log

| Ngày | Phiên bản | Quyết định |
|---|---|---|
| 2026-10-16 | 1.0 | Khởi tạo roadmap M0–M10, chống scope creep, xác định flow Antigravity/Codex, mobile-first pixel |

**Quy tắc cập nhật:** sau mỗi sprint/task đã nghiệm thu, đổi trạng thái và ghi ngày/commit; không biến định hướng sản phẩm thành cam kết tính năng hiện có.
