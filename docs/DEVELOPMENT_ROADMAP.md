# DEVELOPMENT_ROADMAP.md — Lộ trình cho người mới Vibe Code

**Game:** Shinobi Evolution • **Phiên bản:** 2.1 • **Ngày:** 2026-10-16 • **Bản khung:** `OFFICIAL_DESIGN_BASELINE` • **Task:** `PLANNED / DEFERRED`.

> Mục đích: chia game thành feature kiểm được, Antigravity tự code/art/test/sửa đến M8. Người dùng chỉ nghiệm thu bản chơi được ở cuối; Codex review độc lập nếu sẵn có. Kết quả tự kiểm là VERIFIED, không tự DONE.

**Task cụ thể:** [TASK_BACKLOG.md](TASK_BACKLOG.md) chia từng milestone thành đầu việc có ID, phụ thuộc, đầu ra và tiêu chí nghiệm thu. Luật còn mở tra tại [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md).

## 1. Bắc đẩu của dự án (north star)

- **Vision — CHỐT:** PvPvE sinh tồn solo, mỗi người một phe, người cuối cùng sống sót thắng. Trọng tâm là loot, đường đi, farm quái lấy XP, phát triển build bằng XP/SP/Ryō và áp lực vòng bo; lấy cảm hứng sinh tồn từ PUBG theo định hướng người dùng. Không có cứ điểm buff hoặc hồi sinh trong solo.
- **Visual:** 2D HD Pixel Art nhịp hành động gợi Wizard of Legend; camera top-down 3/4, Android landscape, sprite/tiles nearest-neighbor, UI touch.
- **Tech:** Godot 4 Standard/GDScript, VS Code, Antigravity main dev, Codex code review, Git/GitHub.
- **Design input:** 162 node/29 tree/12 synergy là catalog, **chưa phải 162 skill lập trình hoàn chỉnh**.
- **Phạm vi hiện tại — CHỐT MATCH-02/03/04:** solo hai người/trận, chọn vùng rồi spawn ngẫu nhiên an toàn, thời lượng mục tiêu 20–25 phút. Một cuộn Thế thân khởi đầu/người và có rơi thêm; bị động tự tiêu cuộn trước damage gây chết, hồi HP theo config rồi tàng hình, kể cả vòng bo. Tăng số người, mode đội và trụ hồi sinh để sau. Luật chi tiết theo `GAME_DESIGN.md` / `DESIGN_DECISIONS.md`.
- **Nội dung — CHỐT SLICE-02/03:** Uchiha + Hỏa, hai hướng Hỏa thuật/Ảo thuật. Có brief ID/handler/stat thử trước mỗi lô; không tự bật toàn bộ clan, T5, hệ thứ hai hoặc nội dung ngoài allowlist.

## 2. Trạng thái chuẩn

- `PLANNED`: chưa bắt đầu, chỉ có tài liệu.
- `READY`: đủ brief/phụ thuộc/test plan, nằm trong quyền AUTOPILOT đã giao; không cần xin phép lại từng task.
- `IN_PROGRESS`: Antigravity đang code task cụ thể.
- `SELF_REVIEW`: Antigravity tự rà diff và bằng chứng; review độc lập nếu có, không giả Codex PASS.
- `VERIFIED`: kiểm tra áp dụng đã chạy đạt; tự chuyển task tiếp theo.
- `PLAYABLE_CANDIDATE`: bản chơi được cuối M8, có launcher/build/hướng dẫn/QA để người dùng nghiệm thu.
- `DONE`: đáp ứng DoD và được người dùng chấp thuận.
- `BLOCKED_EXTERNAL`: thiếu công cụ/quyền/thiết bị thật; có bằng chứng, vẫn tiếp tục phần độc lập. OPEN chi tiết không tự là blocker nếu thuộc quyền agent đặc tả.
- `DEFERRED`: hướng mở rộng để sau, chỉ đưa lại vào kế hoạch khi người dùng duyệt phạm vi mới.

**Các milestone trong phạm vi hai người khởi đầu ở `PLANNED`; M6B/M9/M10 mở rộng là `DEFERRED`.** Không gán thời gian hứa hẹn theo ngày/tuần khi chưa có tốc độ phát triển thực tế; các "buổi" chỉ là thứ tự học việc.

## 3. Roadmap theo cổng (gated delivery)

| Cổng | Milestone | Sản phẩm test được | Phụ thuộc | Trạng thái |
|---|---|---|---|---|
| M0 | Dev Environment | kiểm project hiện có, engine/build, Git và công cụ | — | PLANNED |
| M1 | Ninja Movement | map placeholder, player, camera, WASD/8-way & collision | M0 | PLANNED |
| M2 | Mobile Input & Pixel Art | joystick 2 ngón, HUD, sprite 4/8 hướng, APK chạy | M1 | PLANNED |
| M3 | Core Combat | HP/Chakra, hitbox, damage, 2 quái, Thế thân bị động dùng cuộn | M2 | PLANNED |
| M4 | Skill Graph Engine | validator, XP/SP/Ryō tối thiểu, unlock T0–T2, trang bị và UI | M3 | PLANNED |
| M5 | PvE Economy & Loot | XP/Ryō/SP, elite, cuộn, pity test, farm progression | M4 | PLANNED |
| M6A | Vertical Slice Offline nhỏ | vòng lobby → farm/build/boss/zone → kết quả với tập nội dung được duyệt | M5 | PLANNED |
| M6B | Nhánh mở rộng slice, cần duyệt riêng | tham khảo ba clan/hai synergy sau khi bản nhỏ đạt | M8 + duyệt scope mới | DEFERRED |
| M7 | Network Integration | 2 client + 1 server, reconciliation, authority và secure loot | M6A + quyết định mạng | PLANNED |
| M8 | Hoàn thiện solo hai người | loot/farm/vòng bo/loại người/kết quả trên Android | M7 | PLANNED |
| M9 | Alpha mở rộng | thêm content/map hoặc số người theo phạm vi mới được duyệt | M8 + duyệt scope mới | DEFERRED |
| M10 | Beta mở rộng | nội dung và tải được duyệt, hardening cho phát hành | M9 + duyệt scope mới | DEFERRED |

**Đường tắt không khuyến nghị:** nhảy M0 → M7 hoặc triển khai Nakama trước khi có gameplay offline hấp dẫn. **Được phép** thu nhỏ/phân lại milestone nếu benchmark hoặc khả năng triển khai yêu cầu; thay đổi scope phải phê duyệt.

**Kiểm rủi ro sớm trong quyền đã giao:** M3-NET-01 thử movement/một ability/HP/Thế thân bằng server Godot riêng + hai client ENet sau M3. Không cần backend dịch vụ; ghi kết quả/ADR rồi M7 tích hợp toàn vòng chơi. Không dừng xin duyệt lại TECH-01 cho lựa chọn prototype đã ghi trong AUTOPILOT.

**Đường nghiệm thu hiện tại:** M0 → M1 → M2 → M3 → M4 → M5 → M6A → M7 → M8. Không cần mở rộng M6B/M9/M10 để hoàn thành bản hai người. M6B là nhánh đề xuất, chưa tự chốt số clan/node phải code.

## 4. Chi tiết các milestone và tiêu chí nghiệm thu

### M0 — Môi trường, Git, tài liệu

**Task giao Antigravity:** kiểm project hiện tại, pin engine version, kết nối VS Code, tạo cấu trúc tối thiểu, xác nhận tài liệu/skill JSON parse.

**DoD:**

- Kiểm project hiện có bằng executable Godot thực tế; ghi đầy đủ version/build và đối chiếu với cấu hình. Không tạo lại hoặc ghi đè project để đáp ứng checklist.
- VS Code/Antigravity đọc đúng project; công cụ cần thiết được kiểm thực tế. Codex độc lập không là phụ thuộc để Antigravity tiếp tục.
- Kiểm repository đang có; commit checkpoint **sau khi người dùng duyệt**; `.gitignore` có `.godot/` và builds, nhưng không loại asset nguồn.
- Tài liệu theo README hiện diện đúng đường dẫn; JSON UTF-8 parse hợp lệ.
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

**Scope:** joystick ảo trái, một action có thể thử và placeholder đủ bố cục HUD đích; thao tác đa chạm, safe area, sprite nhân vật pixel tạm + tiles. Nút chưa có gameplay bị vô hiệu hóa; Thế thân chỉ có indicator bị động.

**DoD:**

- Di chuyển bằng ngón trái, nút phải hoạt động **đồng thời**; thả ngón joystick về 0, không trôi nhân vật.
- Build APK debug test trên **ít nhất một thiết bị Android thật**; landscape không bị notch che HUD.
- Sprite nearest-neighbor không bị mờ, camera giữ world view hợp lý trên nhiều aspect ratio.
- Thử quality profile VFX nhẹ; ghi model/OS/resolution/FPS đo được, không báo 60FPS nếu chưa đo.

**Không làm:** đầy đủ VFX ninja tối thượng, tilemap thế giới mở vô hạn.

### M3 — Combat nền

**Scope:** HP, chakra, attack thường, 1 kỹ năng projectile, 1 kỹ năng area hoặc dash, cooldown, animation hit, quái chase cơ bản; Thế thân bị động dùng cuộn, không có nút kích hoạt riêng.

**DoD:**

- Hai quái test có HP, có thể tấn công/bị đánh, chết/respawn đúng; HP không âm; sprite hit có feedback.
- Cooldown/chakra bị kiểm trong domain, UI phản ánh dữ liệu, button spam không bypass cooldown.
- Enemy telegraph rõ hơn ally VFX; ít nhất một status (burn/slow) test TTL.
- Unit tests tối thiểu: trừ HP một lần, không hit team/self sai, cạn chakra từ chối cast.
- Thế thân: một cuộn khởi đầu, cap hai; hit không gây chết không kích hoạt; lethal hit khi có cuộn/cooldown sẵn sàng tiêu một cuộn, hồi HP/tàng hình trước kill và bắt đầu cooldown. Trong cooldown hoặc hết cuộn thì lethal hit gây chết. Tàng hình vẫn nhận damage và lộ khi gây/nhận damage; kiểm vòng bo, nhặt khi đầy, event trùng và hit khác cùng tick theo SKILL_SYSTEM §10.4.
- SOLO-SUB-08: xóa CC/hiệu ứng bất lợi đang có, hủy DOT cũ; không áp lại debuff của hit kích hoạt sau thanh tẩy. Hit/nguồn mới có thể gây effect ngay, không có miễn nhiễm ngầm.
- SOLO-SUB-09: cấu hình thử HP về 25% max HP, stealth tối đa 3s, cooldown 60s từ kích hoạt. Kiểm mốc cooldown ngay trước/đúng/sau 60s và lộ sớm không reset timer.

**Không làm:** nhiều skill hardcoded dạng 162 ID, boss, PvP.

### M4 — Skill Graph + Catalog validator

**Scope:** parse `skills.json`, validator DAG và IDs, XP/SP/Ryō tối thiểu từ fixture đã duyệt trước kiểm học node, UI kỹ năng và học T0–T2 mẫu; loadout 1–2 active/Thế thân. M5 mới bổ sung nguồn farm/loot đầy đủ.

**DoD:**

- Validator xác nhận 162 node/29 cây/12 synergy; công bố chính xác lỗi missing/cycle nếu data hỏng.
- `requires_all` AND, `requires_any` OR-groups test bằng fixtures.
- **Gate có `requires_implementation` bị từ chối**, không bị auto-unlock; chỉ cho các gate đã explicit-resolve trong prototype.
- Người chơi có thể thấy vì sao skill locked, đủ/thiếu Ryō/SP; không trang bị/cast `design_only`.
- Thao tác chọn node dùng **touch**, không phụ thuộc hover PC.
- Kiểm BUILD-02/LOADOUT-01: node đã học không bị quên/hoàn SP trong trận; đổi preset không sửa learned state; equip chỉ ngoài combat ở mọi vị trí và không reset cooldown. COMBAT-02: cần đủ 5s không gây/nhận damage hoặc dùng đòn/skill tấn công, cả PvE/PvP; kiểm lại lúc commit.
- BUILD-03: learn cũng chỉ ngoài combat và khi còn sống; trong combat xem cây được, mua bị từ chối không mất SP/Ryō/item. Không tự mua lại khi thoát combat.
- Kiểm NATURE-01 cho phạm vi được enable: hai hệ thông thường; request hệ thứ ba với cuộn thường bị từ chối, chỉ xét khi có quyền sự kiện hiếm hợp lệ. Nếu chưa triển khai sự kiện thì nhánh thứ ba tiếp tục khóa.

**Không làm:** tự triển khai mọi skill vì hiển thị được graph, tự phát minh gate rank/huyết kế.

### M5 — Farming + vật phẩm điều kiện

**Scope:** quái thường/elite, XP/Ryō/SP, item inventory, loot group + bảo hiểm pity, nâng skill theo tier.

**DoD:**

- XP/Ryō/spend được test trên domain; quỹ theo bên kết liễu, solo trả cho người kết liễu; retry cùng event không trả thưởng lặp. Chia đội/trade không thuộc scope solo mặc định.
- Cuộn/mảnh hiếm elite/boss rơi công khai; hai người cùng nhặt chỉ một người nhận, request lặp/reconnect không nhân vật phẩm. Người nhận XP/Ryō không độc quyền loot.
- LOOT-04: chết rơi toàn bộ vật tư đang mang, gồm cuộn Thế thân chưa dùng; không rơi XP/SP/Ryō/node. Retry death không nhân đồ; Thế thân ngăn chết thành công không tạo loot chết.
- PITY-02..06: đủ ngưỡng thử 5% max HP/30s cuối, sống trong vùng lúc mục tiêu chết; không nhận mục tiêu tính miss, kể cả bị cướp. Chốt khi toàn bộ mảnh hiếm lượt đó được nhặt/hết hạn; miss thứ tư chọn trong reward thứ tư. Nhận mục tiêu/bảo hiểm hoặc đổi mục tiêu cùng nhóm thì reset; không chuyển miss sang nhóm khác.
- LOOT-03/05: tư liệu chung túi giới hạn; pity vào túi, đầy thì chờ quyền nhận riêng không bị cướp. Kiểm retry/reconnect, không nhân quyền; item đã nhận vẫn rơi khi chết. Chốt số ô/stack, radius/TTL và ledger trong brief M5.
- Vật phẩm hiếm chỉ mở **điều kiện**, không bypass huyết kế/tier/SP/Ryō.
- Có ít nhất **một đường skill T4 thay thế** không lệ thuộc RNG; nếu chưa triển khai T4 hoàn chỉnh thì chứng minh bằng validator/simulation.

### M6A / M6B — Vertical slice playable offline

**M6A:** Uchiha/Hỏa với hai hướng Hỏa thuật/Ảo thuật theo SLICE-02/03, loot/farm, một boss, bo, Thế thân và lobby → kết quả. Brief SLICE-01 xác định ID/handler/stats cụ thể. **M6B — DEFERRED:** tham khảo ba clan/24–36 node/hai synergy sau khi M8 đạt và duyệt mở rộng; không chặn M7 hai người.

**DoD:**

- Có thể chơi từ lobby chọn clan tới trận, farm, nâng skill, đánh boss, kết thúc trận và quay về result.
- Tập clan được duyệt có hai hướng build thử; khi mở rộng M6B, mỗi clan thêm vào cũng phải có ≥2 hướng hữu dụng. Kiểm counterplay qua tình huống và playtest, không suy cân bằng từ số node.
- Tất cả skill đã implemented có chi phí, cooldown, telegraph, hitbox, test cơ bản.
- `T5` hiếm ngoài slice giữ disabled, không bị mua dù catalog có tên.
- Có dữ liệu gameplay: time to T3/T4, average Ryō/min, FPS trong fight, ít nhất 3 tình huống counterplay.
- Mode thử có vòng bo, cuộn Thế thân bị động và chết/bị loại không hồi sinh; có kịch bản mô phỏng đối thủ để kiểm logic người cuối cùng sống sót. Bài kiểm offline không thay thế kiểm chứng PvP solo nhiều người ở M8.

### M7 — Multiplayer proof of concept

**Scope:** một match server và 2 client, sync movement, ability, HP, loot, purchase, cooldown.

**DoD:**

- Hai client nhìn thấy cùng combat state; server từ chối giả mạo damage/mua T5 khi không đủ điều kiện.
- Disconnect xóa input giữ, actor đứng yên/vẫn chịu damage và xét Thế thân; không tự loại theo timeout kể cả quá 60s. Reconnect cùng actor/state, không dupe reward hoặc cấp lại cuộn.
- Có log thời gian tick/network/late input; quyết định backend dựa trên kết quả thực.
- Đã test trên mạng không chỉ localhost ít nhất một tình huống latency mô phỏng.

**Quyết định triển khai:** baseline dùng server Godot riêng/ENet local theo AUTOPILOT; agent kiểm spike rồi ghi ADR/điều chỉnh kỹ thuật có bằng chứng. Nakama/matchmaking công cộng và backend dịch vụ DEFERRED, không là cổng chờ duyệt để thử hai người.

### M8 — Hoàn thiện PvPvE solo hai người

**Scope:** hai người, mỗi người một phe; chọn vùng/spawn an toàn, tranh loot, farm quái/boss, vòng bo, Thế thân bị động và loại người chơi; server authoritative. Mục tiêu 20–25 phút, không hồi sinh hoặc cứ điểm buff. Hoàn thiện trải nghiệm hai người trước khi xin mở quy mô.

**DoD:**

- Hai người sync quái/projectile/loot, không ăn thưởng đôi khi cùng đánh boss.
- PvP hit registration, CC và Thế thân bị động trước damage gây chết hoạt động dưới latency mô phỏng; client không tự xác nhận thoát chết hoặc nhận thêm cuộn.
- Mobile device stress test ghi p95 frame time, RAM, bandwidth theo ngưỡng được duyệt cho hai người; giới hạn entity/VFX theo số đo.
- Trận thắng theo người sống sót cuối cùng; vòng bo/sát thương ngoài vùng sync đúng, không phân thắng thua theo mốc 25 phút. Kiểm chết đồng thời/disconnect, cuộn hết/còn, HP hồi và tàng hình đúng authority.
- MATCH-05: kết quả chốt sau batch damage/Thế thân của tick; cả hai chết thì hòa, đảo thứ tự actor trong fixture không đổi kết quả. ZONE-02: bo cuối hết vùng an toàn, áp lực đủ kết thúc dù có hồi phục/cuộn; không tự tắt Thế thân.

### M9 — Alpha mở rộng, DEFERRED

**Scope tham khảo để sau:** sáu clan, năm nguyên tố, 60–80 node; map/content hoặc số người lớn hơn phải duyệt lại từ kết quả M8. Không là điều kiện nghiệm thu bản hai người.

**DoD:**

- Có QA regression theo toàn bộ clan/ability active và Thế thân bị động; kiểm chứng loot/farm có rủi ro, phản công và thắng theo người sống sót cuối cùng.
- Có chống snowball/pity analytics, nhiều tuyến farm; UI mobile mở graph không cản thao tác sống còn.
- Không P0/P1 trong cửa nghiệm thu; telemetry đủ phát hiện crash/disconnect và skill abuse.

### M10 — Beta mở rộng, DEFERRED

**Scope tham khảo để sau:** thêm clan và node **chỉ khi có đủ runtime/cân bằng**; số người và scope phát hành cần yêu cầu mới. Mốc hai người/20–25 phút đang hiệu lực cho phiên bản hiện tại; không tự khôi phục cấu hình trận cũ hoặc đưa rank/season vào scope.

**DoD:**

- Tăng concurrency qua load test, không bằng suy đoán. Có giới hạn entity và VFX ngân sách thực nghiệm.
- Đã kiểm tra server authority, dữ liệu phiên bản, loadout exploit, reconnect, abuse RNG.
- Có lựa chọn IP rõ ràng trước marketing/store (license hoặc thế giới tự sáng tạo). Store policy, bảo mật, quyền riêng tư và thanh toán cần đánh giá riêng khi phát hành.
- Beta không đồng nghĩa game đã được duyệt thương mại.

## 5. Bắt đầu chế độ tự triển khai

Đọc [ANTIGRAVITY_AUTOPILOT](ANTIGRAVITY_AUTOPILOT.md), [ART_GENERATION_GUIDE](ART_GENERATION_GUIDE.md) và [profile prototype](../data/prototypes/solo_first_playable.json). Người dùng đã giao Antigravity tự làm/test/sửa đến M8; không dừng ở M0/M1 hoặc xin duyệt lại từng task/asset.

```text
Đọc trạng thái Git/checkpoint và task
 → bổ sung brief trong quyền đã giao, ghi plan
 → code + tạo art bằng generate_image + tự kiểm
 → sửa lỗi, kiểm lại, self-review
 → VERIFIED + lưu bằng chứng/checkpoint
 → tự sang task kế tiếp
 → M8: PLAYABLE_CANDIDATE + launcher/build/PLAY_GUIDE/QA_REPORT
 → người dùng chơi thực tế, chấp thuận thì ACCEPTED/DONE
```

Không bắt Codex độc lập, commit hoặc người dùng chuyển diff giữa các vòng làm. Review độc lập nếu có là bổ sung, phải ghi ai thực sự review. Khi thiếu tool/thiết bị, tiếp tục phần độc lập và báo điều kiện thiếu đúng thực tế; không giả test đã chạy.

Lệnh bắt đầu để gửi Antigravity:

```text
Đọc AGENTS.md và docs/ANTIGRAVITY_AUTOPILOT.md rồi tự triển khai liên tục đến PLAYABLE_CANDIDATE M8, dùng generate_image theo docs/ART_GENERATION_GUIDE.md; tự test, sửa lỗi, rà soát và bàn giao bản hai người chơi được thực tế để tôi nghiệm thu, không dừng xin duyệt từng task/asset.
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
- Self-review/test áp dụng đạt, P0/P1/P2 liên quan đã xử lý; independent review nếu sẵn có, thiếu thì ghi NOT_RUN. VERIFIED cho phép tự tiếp tục.
- Cuối M8 có bản chơi được/QA/PLAY_GUIDE; người dùng thử thực tế và chấp thuận mới ACCEPTED/DONE.
- Cập nhật tài liệu/manifest/checkpoint; không cần commit để tiếp tục, không tự commit/push.

## 7. Checklist chất lượng riêng cho mobile Pixel Art

- [ ] Dùng joystick và 1+ nút skill cùng lúc mà không mất pointer.
- [ ] Hướng sprite khi chạy chéo không nhấp nháy; va chạm không jitter.
- [ ] UI không che bởi camera notch/gesture bar; nút bấm đủ lớn cho ngón tay.
- [ ] Pixel sprite nearest không vỡ, không bị méo khi zoom; HUD text đọc được.
- [ ] Enemy telegraph thấy rõ dù 3 ninja cùng tung thuật; không phụ thuộc mỗi màu.
- [ ] Có quality `Low/Medium/High` cho VFX khi cần; camera shake/flash tắt được.
- [ ] Mục tiêu benchmark 30 FPS máy thấp và 60 FPS máy khuyến nghị **chỉ đánh dấu đạt sau đo trên thiết bị cụ thể**.
- [ ] RAM/CPU/battery/network trong trận hai người được ghi log ở M8.

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
| M6A | 22 node kế hoạch Uchiha/Hỏa theo profile, chỉ bật ID có handler/test | slice hai hướng build trong baseline |
| M6B | 24–36 node / ba clan tham khảo, DEFERRED | ngoài đường nghiệm thu bản đầu |
| M9 | 60–80 implemented nodes | PvPvE alpha |
| M10 | up to 162 approved by content rollout | chỉ nếu runtime/balance QA đã đủ |

**Ghi chú:** số node và số active ability khác nhau. Một node có thể là tiến trình/root/passive, không nhất thiết cần một VFX riêng.

## 10. Decision Log / Change Log

| Ngày | Phiên bản | Quyết định |
|---|---|---|
| 2026-10-16 | 1.0 | Khởi tạo roadmap M0–M10, chống scope creep, xác định flow Antigravity/Codex, mobile-first pixel |
| 2026-10-16 | 1.1 | Đồng bộ WIN-01/SEAL-01/REVIVE-01: thắng sinh tồn, tranh quyền kiểm soát phong ấn, cứu/mục tiêu hồi sinh; các task code vẫn PLANNED |
| 2026-10-16 | 1.2 | Đồng bộ ZONE-01/SEAL-02/ELIM-01: vòng bo thay giới hạn cứng 42 phút, phong ấn buff tách hồi sinh, kiểm chứng loại đội trong slice và multiplayer |
| 2026-10-16 | 1.3 | Thêm acceptance M4 cho BUILD-02/NATURE-01/LOADOUT-01: không hoàn điểm, quyền hệ thứ ba và equip ngoài combat giữ cooldown |
| 2026-10-16 | 1.4 | Thêm acceptance M5 cho REWARD-01/LOOT-02/PITY-02: chia XP/Ryō, tranh pickup công khai và mở chọn ở lượt thứ tư; trade cần phạm vi riêng |
| 2026-10-16 | 1.5 | Ưu tiên solo; bỏ cứ điểm buff và hồi sinh khỏi milestone chính, thêm acceptance Thế thân bị động dùng cuộn trước damage gây chết, đồng bộ pity nhận cá nhân và quỹ kết liễu |
| 2026-10-16 | 1.6 | Bổ sung acceptance M3 cho hai cuộn tối đa, cooldown nội tại và break stealth bởi damage theo SOLO-SUB-05..07 |
| 2026-10-16 | 1.7 | Thêm backlog task/phụ thuộc/nghiệm thu; cấp tài nguyên tối thiểu ở M4 trước học node, chia M6A/B và đề xuất spike sớm; chốt đường nghiệm thu hai người/20–25 phút, để tăng quy mô sau |
| 2026-10-16 | 1.8 | Thêm acceptance thanh tẩy Thế thân, học node ngoài combat và rơi toàn bộ vật tư khi chết; giữ XP/SP/Ryō/node ngoài loot chết |
| 2026-10-16 | 2.0 | Roadmap chính thức cho Uchiha/Hỏa/hai hướng build và trận hai người; đồng bộ timer/prototype/pity/túi đồ/hòa/disconnect/bo cuối, M6B/M9/M10 deferred; giữ task PLANNED |
| 2026-10-16 | 2.1 | Quyền tự thực hiện đến M8, VERIFIED để tiếp tục, self-review/QA có bằng chứng và chỉ nghiệm thu người dùng cuối; generate_image/profile prototype thay cổng chờ duyệt từng bước |

**Quy tắc cập nhật:** sau mỗi sprint/task đã nghiệm thu, đổi trạng thái và ghi ngày/commit; không biến định hướng sản phẩm thành cam kết tính năng hiện có.
