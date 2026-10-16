# TASK_BACKLOG.md — Task phát triển theo giai đoạn

**Phiên bản:** 2.1 • **Ngày:** 2026-10-16 • **Bản khung:** `OFFICIAL_DESIGN_BASELINE` • **Task:** `PLANNED / DEFERRED`.

Nguồn luật: [GAME_DESIGN](GAME_DESIGN.md), [SKILL_SYSTEM](SKILL_SYSTEM.md). Nguồn module và quy trình: [ARCHITECTURE](ARCHITECTURE.md), [AGENTS](../AGENTS.md). [DEVELOPMENT_ROADMAP](DEVELOPMENT_ROADMAP.md) mô tả cổng phát hành; tài liệu này chia cổng thành task có thể giao riêng. Quyết định còn mở tra tại [DESIGN_DECISIONS](DESIGN_DECISIONS.md).

## 1. Cách sử dụng

- Task trong phạm vi hiện tại đang `PLANNED`; M6B/M9/M10 là `DEFERRED`. Tiêu chí nghiệm thu là yêu cầu tương lai, không phải kết quả đã chạy.
- Trước READY: đủ phụ thuộc/brief/test plan và nằm trong AUTOPILOT đã giao. Agent dùng profile/tự bổ sung chi tiết thử, ghi lý do, không dừng xin duyệt từng task/asset. Luật CHỐT không đổi.
- Đường dẫn sản phẩm dưới đây là dự kiến theo kiến trúc; người triển khai kiểm tra cây thư mục thực tế trước khi thêm file. Không tạo toàn bộ module chỉ để khớp danh sách.
- Mỗi task giữ phạm vi nhỏ; kiểm/self-review đạt thì VERIFIED và tự sang task kế tiếp. Người dùng chỉ nghiệm thu cuối M8 bằng chơi thực tế; không chờ Codex/commit từng task. Đọc [AUTOPILOT](ANTIGRAVITY_AUTOPILOT.md), [ART guide](ART_GENERATION_GUIDE.md) và [profile](../data/prototypes/solo_first_playable.json).
- Task nội dung M6B/M9/M10 phải có danh sách ID, tiên quyết, gate, handler và fixture cụ thể trước `READY`. Số node catalog không thay cho số ability thật.

**Đường nghiệm thu:** M0 → M1 → M2 → M3 → M4 → M5 → M6A → M7 → M8, solo hai người/20–25 phút. M3-NET được thực hiện sau M3 theo AUTOPILOT, ENet/server riêng local. M6B/M9/M10 vẫn ngoài scope. Nếu thiếu thiết bị/toolchain Android thật ở M2-03, tiếp tục M3 từ input M2-02; giữ việc export/device còn thiếu trong QA, không gọi Android đã đạt.

**Nội dung CHỐT SLICE-02/03:** Uchiha + Hỏa, hai hướng Hỏa thuật/Ảo thuật. Cả hai người dùng cùng tập nội dung; chốt ID/handler/stat thử trước M3/M4. Chỉ một nature được enable trong baseline dù luật mở rộng cho phép học thêm theo gate.

## 2. M0 — Xác nhận môi trường đang có

### M0-01 — Kiểm engine, renderer và khả năng chạy project

**Phụ thuộc:** không. **Quyết định:** TECH-01 phần môi trường. **Sản phẩm:** hồ sơ engine/build/export templates/thiết bị trong ARCHITECTURE; cấu hình project chỉ sửa theo quyết định được duyệt.

- Dùng project hiện có; phân biệt `config/features` với phiên bản executable thực sự. Ghi main scene có/chưa có, lỗi import và công cụ còn thiếu.
- Đối chiếu renderer thực tế; được cấu hình Compatibility/debug export theo AUTOPILOT, ghi diff/lý do và kiểm lại. Không thay release signing hoặc tạo lại project.
- Chạy kiểm tra import/parse phù hợp bản engine nếu có CLI; lưu lệnh và kết quả thật. Thiếu binary/templates thì ghi điều kiện thiếu, không báo đã chạy.

### M0-02 — Kiểm Git, dữ liệu nguồn và cấu trúc tối thiểu

**Phụ thuộc:** M0-01. **Sản phẩm:** kiểm tra cấu trúc, ignore và dữ liệu; bản ghi kiểm chứng.

- Tài liệu nguồn và JSON đọc được bằng UTF-8; thống kê đúng 162 node, 29 tree, 12 synergy trước mọi thay đổi catalog.
- Kiểm `.gitignore` bỏ cache/build sinh ra, giữ asset nguồn; không đưa credentials/signing vào diff.
- Xác nhận trạng thái Git, đường dẫn VS Code/Godot và điểm bắt đầu task tiếp theo; commit là hành động riêng sau phê duyệt.

## 3. M1 — Di chuyển và camera offline

### M1-01 — Actor di chuyển trong arena nhỏ

**Phụ thuộc:** M0-02. **Sản phẩm:** player, input adapter và arena placeholder trong `scenes/`, `scripts/`.

- Di chuyển tám hướng; tốc độ chéo được chuẩn hóa; thả input dừng đúng.
- Va chạm vật cản theo physics; kiểm ở các frame rate thử được ghi, không chỉ một tốc độ máy.
- Input tạo intent; view không tự sửa trạng thái domain; scene mở/chạy không lỗi parse.

### M1-02 — Camera và giới hạn arena

**Phụ thuộc:** M1-01. **Quyết định:** VIEW-01 phần camera. **Sản phẩm:** camera theo actor, ranh giới map và fixture kiểm góc nhìn.

- Camera theo player, không lộ ngoài map trái policy; kiểm sát biên và đổi hướng nhanh.
- Tỉ lệ 16:9/20:9 tuân thủ policy vùng nhìn được duyệt; zoom/debug không tạo quyền quan sát trong mode chính.
- World pixel rõ, không rung đáng kể ở tốc độ thử; ghi tình huống và thiết bị dùng để đánh giá.

## 4. M2 — Điều khiển Android và bố cục đích

### M2-01 — HUD touch đủ vị trí, gameplay nhỏ

**Phụ thuộc:** M1-02. **Quyết định:** VIEW-01 phần HUD. **Sản phẩm:** joystick, attack, bốn active, ultimate, nhẫn cụ và chỉ báo Thế thân trong `scenes/ui/`.

- Có đủ chỗ cho bố cục đích; ô chưa có ability bị vô hiệu hóa, không giả lập đầy đủ kỹ năng.
- Giữ joystick đồng thời chạm/kéo ngắm; nút HUD phát intent, không trực tiếp trừ HP/chakra hoặc cấp đồ.
- Thế thân chỉ hiển thị số cuộn, readiness và cooldown; không có nút kích hoạt thủ công.

### M2-02 — Vòng đời input và panel

**Phụ thuộc:** M2-01. **Sản phẩm:** touch ownership, hủy ngắm và focus handling.

- Nhấc/rê ngón ra ngoài nút, mất focus hoặc mở panel không để nhân vật tự chạy/cast.
- Hai ngón không tranh quyền joystick; thao tác UI không xuyên xuống world gây đánh nhầm.
- Khi đóng panel, input trở về trạng thái xác định; ghi ca test đa chạm và khả năng hủy thao tác.

### M2-03 — APK và kiểm tra hình ảnh trên máy thật

**Phụ thuộc:** M2-02; export/thiết bị đã sẵn sàng. **Sản phẩm:** bản debug và ghi nhận Android; không đưa signing secret vào Git.

- APK chạy landscape trên ít nhất một máy thật, HUD nằm trong safe area.
- Sprite dùng lọc phù hợp pixel art; UI đọc được và joystick không bị che ở các aspect ratio thử.
- Ghi model/OS/resolution, FPS và lỗi quan sát được; chưa đo thì không kết luận đạt hiệu năng mục tiêu.

## 5. M3 — Combat và bị động sinh tồn

### M3-01 — Damage, tài nguyên và ability mẫu

**Phụ thuộc:** M2-02. **Quyết định:** COMBAT-01 agent đặc tả trong quyền AUTOPILOT; dùng profile/stat thử có log. **Sản phẩm:** domain combat, attack và một projectile + một area hoặc dash; M2-03 hoàn tất theo toolchain, không chặn phần code độc lập.

- Cast kiểm cooldown, chakra, trạng thái caster và mục tiêu; spam intent không bypass chi phí.
- Mỗi hit có định danh và policy số lần trúng; event lặp không trừ HP hai lần; HP clamp đúng.
- Kiểm hết chakra, mục tiêu rời range/chết, cancel và self-hit theo policy; telegraph thể hiện trước đòn mạnh.

### M3-02 — Thế thân tự động bằng cuộn

**Phụ thuộc:** M3-01. **Quyết định:** SOLO-SUB-09 đã chốt bộ số thử; LIFE-01 đặc tả effect/shield/làm tròn HP. **Sản phẩm:** handler bị động, trạng thái cuộn/cooldown và HUD phản hồi.

- Một cuộn đầu trận, cap hai; lethal damage khi sẵn sàng tiêu đúng một cuộn, hồi HP/tàng hình và bắt đầu cooldown trước khi phát kill.
- Trong cooldown/hết cuộn thì lethal damage gây chết; zone damage cũng được xét. Không cấp thêm thao tác dùng thủ công hoặc miễn damage ngầm.
- Kích hoạt xóa CC/effect bất lợi đang có và hủy DOT cũ; không áp lại debuff của hit kích hoạt sau thanh tẩy. Hit/effect mới vẫn tác động ngay; damage mới làm lộ. Kiểm hit trùng, hit khác cùng tick và nhặt cuộn/đổi loadout không reset cooldown.
- Dùng profile thử HP về 25% max HP, ẩn tối đa 3s, cooldown 60s; kiểm trước/đúng/sau mốc 60s, lộ sớm không rút cooldown và không tự hồi thêm lần hai.

### M3-03 — Quái và status có vòng đời

**Phụ thuộc:** M3-01, M3-02. **Sản phẩm:** hai quái fixture, chase/attack và ít nhất một status có TTL.

- Quái có telegraph, HP và chết đúng một lần; respawn fixture được tách khỏi luật loại người chơi solo.
- Status hết hạn/cleanup khi actor bị loại; không còn tick gây damage từ actor đã giải phóng trái policy.
- Combat chạy lại được với cấu hình/seed fixture; ghi damage, chết và Thế thân để tái hiện lỗi.

### M3-NET-01 — Spike server riêng và hai client

**Phụ thuộc:** M3-03. **Sản phẩm:** arena thử Godot server riêng + hai client ENet local, báo cáo profile và ADR triển khai; trong quyền AUTOPILOT, không cần xin duyệt lại.

- Thử movement, một ability, HP và Thế thân; client gửi intent, không được tự báo damage/HP hợp lệ.
- Ghi input/snapshot/tick và hành vi theo profile latency/loss được duyệt; đo trên thiết bị dự kiến.
- Nêu phần tái sử dụng và phần phải đổi khi lên online; không tự thêm tài khoản/database/backend. Spike không phải bằng chứng game đã hỗ trợ PvP đầy đủ.

## 6. M4 — Graph và tiến trình tối thiểu

### M4-01 — Catalog validator và runtime allowlist

**Phụ thuộc:** M3-03. **Quyết định:** SKILL-01. **Sản phẩm:** loader/validator và báo cáo ID được phép dùng.

- Validate số lượng, ID, AND/OR, reference, DAG, synergy và schema; fixture sai phải báo lỗi hữu ích.
- Gate chưa có predicate phải fail-closed; node `design_only` không được trang bị/cast.
- Tách node tiến trình/passive/active/ultimate và runtime binding theo đặc tả được duyệt; không viết một nhánh `match` cho toàn catalog.

### M4-02 — XP/SP/Ryō tối thiểu trước học node

**Phụ thuộc:** M4-01. **Quyết định:** ECON-01 theo profile, agent mô phỏng/chỉnh số thử có log. **Sản phẩm:** tiến trình và ví domain, nguồn cấp cố định cho arena.

- XP/cấp/SP theo cấu hình đã duyệt; không vượt ngân sách hoặc nhận lại điểm do event lặp.
- Học node cần đủ SP và Ryō; hai khoản và learned state cập nhật nguyên tử, từ chối không mất tài nguyên.
- Fixture cấp tài nguyên tách khỏi gameplay chính; kiểm thiếu một loại, đủ đúng chi phí, vượt cấp và retry. Farm/loot đầy đủ thực hiện ở M5.

### M4-03 — Học node và thay loadout

**Phụ thuộc:** M4-02. **Quyết định:** BUILD-01 theo brief agent và 22 ID kế hoạch trong profile; manifest chỉ bật ID có handler/test. **Sản phẩm:** unlock/equip intent và domain policy.

- Kiểm AND/OR, gate, giới hạn nature, loại trừ và item cùng điều kiện SP/Ryō; cuộn thường không tự mở hệ thứ ba.
- Không respec/hoàn điểm trong trận; đổi preset không sửa learned state; slot chỉ nhận node phù hợp có runtime.
- Learn/equip chỉ khi alive/ngoài combat, mọi vị trí; trong combat xem cây được nhưng request mua bị từ chối không mất SP/Ryō/item và không tự mua lại. Đổi slot giữ cooldown; cleanup buff/summon theo policy được duyệt.
- COMBAT-02: timer 5s từ event combat gần nhất, cả PvE/PvP; kiểm mốc trước/đúng 5s, dùng đòn hụt, DOT/bo và panel đã mở trước khi bị đánh. Cập nhật combat tick trước commit giao dịch.

### M4-04 — Graph UI có lọc cho mobile

**Phụ thuộc:** M4-03, M2-02. **Sản phẩm:** panel graph/loadout và đường preset.

- Touch chọn node được, hiện tiền đề, gate và thiếu SP/Ryō; không phụ thuộc hover.
- Phân biệt đã học, đã trang bị, khóa thiết kế và chưa có runtime; không hứa mở node chỉ bằng thanh tiến trình.
- Lọc/preset giúp đọc nhánh nhỏ trên Android; đóng panel không làm mất hoặc lặp giao dịch học.

## 7. M5 — Farm, loot và bảo hiểm tiến trình

### M5-01 — Thưởng kết liễu, loot công khai và inventory

**Phụ thuộc:** M4-04. **Quyết định:** LOOT-01 phần pickup/inventory; LOOT-04 đã chốt rơi đồ khi chết. **Sản phẩm:** reward, drop, pickup và inventory domain.

- XP/Ryō theo bên kết liễu; retry death/reward không nhân thưởng. Vật phẩm hiếm rơi công khai, không độc quyền cho người nhận XP.
- Hai request nhặt đồng thời chỉ một người nhận; xác nhận range, capacity và trạng thái sống trên authority.
- Túi đầy/đã đủ hai cuộn không làm mất world item; kiểm disconnect/retry bằng fixture, không nhân hoặc mất vật phẩm trái policy.
- Khi bị loại chuyển toàn bộ item đang mang, gồm cuộn chưa dùng, thành loot công khai đúng một lần; không rơi XP/SP/Ryō/node. Thế thân thành công không chạy drop chết; kiểm replay death sau khi người khác đã nhặt đồ.
- LOOT-05: tư liệu chung túi giới hạn ô với vật tư sinh tồn; số ô/stack được chốt trong brief, không cấp ngăn tư liệu vô hạn. Pickup kiểm đồng thời capacity và cap hai cuộn Thế thân.

### M5-02 — Pity cá nhân cùng loot công khai

**Phụ thuộc:** M5-01. **Quyết định:** PITY-01. **Sản phẩm:** participation ledger, settle, miss counter và quyền chọn riêng.

- PITY-04: damage ít nhất 5% max HP trong 30s cuối, alive/in-area lúc mục tiêu chết; kiểm ngay dưới/đúng ngưỡng và cửa sổ, không thay eligibility theo vị trí sau đó.
- PITY-05: chỉ settle khi toàn bộ mảnh hiếm reward đã nhặt/hết hạn; có TTL hữu hạn và event order trong nhóm. Không có mảnh rơi thì không chờ; item vừa spawn chưa phải đã nhận/trượt.
- Miss thứ tư tạo quyền chọn ngay trong reward thứ tư; trả thẳng cá nhân, không đưa phần bảo hiểm xuống đất.
- PITY-06: nhận mảnh mục tiêu/bảo hiểm hoặc đổi mục tiêu cùng nhóm thì reset; nhóm độc lập, target ghi trước lượt, không chuyển miss cũ. Kiểm nhận mảnh thường, đổi mục tiêu khi còn reward pending và thứ tự event.
- LOOT-05: đầy túi giữ private pending claim, có chỗ/alive mới giao vào túi; retry/reconnect không nhân quyền/đồ. Claim chưa giao không là đồ đang mang; không cho người bị loại claim để tiếp tục trận.
- Pickup rồi chết làm item rơi lại không được mở lại lượt đã settle, phát thêm quyền chọn hoặc tính miss hai lần; giữ provenance reward/item và phân biệt giao dịch rơi đồ mới.

### M5-03 — Kiểm nhịp farm và đường build dự phòng

**Phụ thuộc:** M5-02. **Sản phẩm:** fixture seed/loot cố định, báo cáo thời gian và chi phí build thử.

- Mỗi build thử tính đủ tiên quyết/gate/SP/Ryō và nguồn item; không coi tổng ba node đích là chi phí cả build.
- Chạy ca thuận lợi, thiếu cuộn và bị cướp loot; có lựa chọn hữu dụng theo phạm vi được duyệt, không âm thầm tặng gate.
- Ghi thời gian lên tier, Ryō/phút, lượt pity và quyết định điều chỉnh; giữ thông số chưa duyệt ngoài nhãn cân bằng chính thức.

## 8. M6 — Vertical slice offline, chia hai cổng

### M6A-01 — Ghép lobby và tập build nhỏ

**Phụ thuộc:** M5-03. **Quyết định:** SLICE-02/03; ID/stats trong brief SLICE-01. **Sản phẩm:** lobby Uchiha/Hỏa, hai preset Hỏa thuật/Ảo thuật, bắt đầu trận mới.

- Lobby chỉ cho chọn nội dung allowlist, không cấp miễn phí node/SP/item ngoài loadout được duyệt.
- Hai hướng build thử khác nhau về hành vi và có đường thiếu đồ; liệt kê toàn bộ ID/runtime trước mở cổng.
- Trận mới reset tài nguyên, cuộn, pity và progression thuộc trận; preset chỉ giữ vai trò gợi ý.

### M6A-02 — Vào map, vòng bo và điều kiện kết thúc solo

**Phụ thuộc:** M6A-01. **Quyết định:** MATCH-01; LIFE-01 phần loại người chơi. **Sản phẩm:** match state, spawn/entry, zone phases và fixture nhiều actor.

- Chọn vùng rồi spawn ngẫu nhiên với khoảng cách an toàn; kiểm cả hai chọn cùng vùng và không có vị trí hợp lệ, không âm thầm bỏ khoảng cách đã cấu hình.
- ZONE-02: bo cảnh báo/thu nhỏ/damage theo config đến hết vùng an toàn, áp lực tăng đủ kết thúc dù có hồi phục/cuộn; không có cứ điểm buff hoặc tắt Thế thân.
- Solo không respawn; giải quyết toàn bộ damage/Thế thân hợp lệ trong tick trước result; một người sống thắng, không ai sống thì hòa. Đảo thứ tự actor không đổi kết quả; result phát một lần.
- MATCH-06: disconnect đứng yên nhưng vẫn alive/targetable đến khi bị hạ; không timeout tự loại. Kiểm cả hai mất kết nối, bo/Thế thân vẫn chạy và match vẫn kết thúc theo sống sót/hòa.

### M6A-03 — Vòng chơi từ lobby đến kết quả

**Phụ thuộc:** M6A-02. **Sản phẩm:** slice offline có farm/loot/boss/build/zone/result, đối thủ fixture.

- Đi trọn lobby → vào map → phát triển → loại/thắng → kết quả → trận mới mà không dùng lệnh sửa state để vượt luồng.
- Chết dọn input/UI/effect theo policy, chuyển màn hình đúng; phần thưởng và số liệu không phát lại khi quay về lobby.
- Ghi rõ đối thủ mô phỏng/offline; kiểm cảm giác và logic, chưa kết luận đạt PvP hoặc số người đích.

### M6B-01 — Mở rộng content slice sau khi vòng chơi đạt — DEFERRED

**Phụ thuộc:** M8-03 và duyệt scope mới; kết quả M3-NET-01 nếu phương án spike được duyệt. **Sản phẩm:** các lô clan/nature/ability mở rộng đã duyệt, không thuộc baseline một clan/một hệ.

- Mục tiêu scope hiện có: ba clan, 24–36 node và 8–12 ability thật; chỉ mở từng lô có ID/handler/stats/telegraph được duyệt.
- Mỗi clan có ít nhất hai hướng phát triển thử, với tiên quyết và đường dự phòng đã kiểm tài nguyên.
- T5 hoặc gate chưa triển khai tiếp tục khóa; cập nhật allowlist và kiểm validator sau mỗi lô.

### M6B-02 — Hai synergy có binding rõ — DEFERRED

**Phụ thuộc:** M6B-01. **Quyết định:** FUSE-01. **Sản phẩm:** bảng công thức → kết quả và handler hai tương tác được chọn.

- Xác định owner, trigger, điều kiện, cost/cooldown và kết quả; không suy mọi phản ứng nguyên tố là huyết kế.
- Không cấp hiệu ứng hai lần do synergy và node lai cùng bind; kiểm ca thiếu một tiền đề và tương tác lặp.
- Telegraph/counterplay nhận biết được trên Android; giới hạn entity/chain/TTL theo config được duyệt.

### M6B-03 — Cổng kiểm chứng slice mở rộng — DEFERRED

**Phụ thuộc:** M6B-02. **Sản phẩm:** kết quả playtest offline và hồ sơ hiệu năng.

- Đo nhịp farm/build, số lần dùng Thế thân, thời gian bị khóa điều khiển và độ rõ telegraph theo mục tiêu thử.
- Stress entity/VFX/UI trên thiết bị, lưu cấu hình và quan sát; không dùng FPS editor thay số Android.
- Ghi quyết định giữ/thu nhỏ/sửa slice trước online; lỗi blocker đã được giải quyết và review lại.

## 9. M7 — Tích hợp mạng có authority

### M7-01 — Command, replication và visibility

**Phụ thuộc:** M6A-03, M3-NET-01. **Quyết định:** TECH-01/VIEW-01 được agent đặc tả theo AUTOPILOT; không cần M6B. **Sản phẩm:** hai client + server với contract phiên bản hóa.

- Client gửi intent; server xác thực vị trí, cast, cooldown, HP và Thế thân; không chấp nhận client tự khai damage/drop/unlock.
- Content/schema mismatch được xử lý rõ; tick/input/snapshot và reconciliation theo policy đo được.
- Stealth/LOS/minimap/spectator chỉ nhận dữ liệu được phép; không chỉ ẩn sprite khi đối thủ vẫn nhận toàn bộ vị trí bí mật.

### M7-02 — Đồng bộ progression, loot và reward

**Phụ thuộc:** M7-01. **Sản phẩm:** authoritative graph/economy/inventory/pity.

- Client không tự cấp XP/Ryō/SP/item hoặc thỏa gate; mọi giao dịch được server xác thực.
- Request trùng/đến muộn và hai người tranh loot không nhân đồ, âm tiền hoặc học node hai lần.
- Event/reward/claim có định danh đủ tái hiện và bảo đảm xử lý một lần; HUD render state xác nhận.

### M7-03 — Reconnect và mạng xấu

**Phụ thuộc:** M7-02. **Quyết định:** MATCH-01 phần disconnect/reconnect. **Sản phẩm:** báo cáo test network và sửa lỗi liên quan.

- Mất kết nối xóa input giữ, actor đứng yên/vẫn chịu damage và xét Thế thân, không tự loại theo timeout; kiểm vượt 60s và cả hai mất kết nối. Không tạo bản sao hoặc quyền sống lại.
- Reconnect tiếp tục cùng actor/state từ authority; không reset cooldown/pity/zone, nhận lại cuộn đầu trận hoặc đồ đã dùng. Actor đã bị loại không được phục hồi để chơi.
- Chạy profile latency/loss/timeout được duyệt; ghi điều kiện, sai lệch và giới hạn còn lại trước nghiệm thu vòng chơi hai người.

## 10. M8 — Hoàn thiện hai người; M9/M10 mở rộng để sau

### M8-01 — Trận solo hai người đầy đủ

**Phụ thuộc:** M7-03. **Sản phẩm:** playtest hai người, mỗi người một phe; mục tiêu 20–25 phút.

- Hai client theo cùng match state, chọn vùng/spawn an toàn, zone và loot; không còn logic đồng đội trong điều kiện thắng solo.
- Thử tranh boss/loot, Thế thân và loại người; tất cả client nhận kết quả nhất quán từ server.
- Ghi tải server/network/Android, nhịp trận và lỗi desync; nghiệm thu đúng phạm vi hai người, không tự mở số người lớn hơn.

### M8-02 — Luồng loại người và xem trận

**Phụ thuộc:** M8-01. **Quyết định:** VIEW-01 spectator; loot khi chết đã chốt. **Sản phẩm:** eliminated/result/spectator UI.

- Người đã bị loại không gửi intent gameplay, nhặt đồ hoặc nhận quyền hồi sinh.
- Loot/effect sau chết đúng policy, result không lặp khi disconnect hoặc rời màn hình.
- Spectator không cung cấp thông tin bí mật cho người còn chơi trái policy; kiểm trên hai thiết bị.

### M8-03 — Cổng playtest solo

**Phụ thuộc:** M8-02. **Sản phẩm:** PLAYABLE_CANDIDATE, launcher/build và hướng dẫn nghiệm thu; không tự mở alpha/scope mới.

- Đo thời gian chạm trán/farm/di chuyển, nguyên nhân chết và khả năng đọc đối trọng.
- Kiểm lợi thế build, RNG và tranh loot theo nhiều seed/trận thử; phân biệt thiếu dữ liệu với kết luận cân bằng.
- Có launcher hai client/LAN, Windows debug, Android debug theo toolchain, PLAY_GUIDE và QA_REPORT với log/ảnh/video thật; báo riêng kiểm tra máy thật chưa chạy. Không bàn giao code chưa chạy như bản chơi được hoặc tự DONE.

### M9-01 — Alpha content theo lô — DEFERRED

**Phụ thuộc:** M8-03 và duyệt phạm vi mở rộng. **Sản phẩm tham khảo:** sáu clan/năm hệ/60–80 node, chia thành task con trước `READY`; không là yêu cầu phiên bản hai người.

- Mỗi lô có ID, đầy đủ tiên quyết, gate, handler, stat thử và counterplay; giữ node ngoài lô khóa runtime.
- Validate toàn graph/synergy sau mỗi lô; thay schema/save/protocol phải có phương án tương thích được duyệt.
- Hồi quy các luồng học/trang bị/loot/pity/Thế thân liên quan; không nhận đủ content chỉ bằng đủ số node.

### M9-02 — Alpha map và tải mở rộng — DEFERRED

**Phụ thuộc:** M9-01 và duyệt số người mới nếu tăng. **Sản phẩm:** map/loot/zone theo quy mô alpha được duyệt.

- Mật độ spawn, tài nguyên và vùng bo phù hợp số người thử; đo thời gian di chuyển và chạm trán.
- Stress AI/entity/VFX/network trên server và Android mục tiêu; nêu rõ cấu hình/profile.
- Chỉ tăng số người khi kết quả đạt ngưỡng được duyệt; cập nhật rủi ro và dự toán tải beta bằng bằng chứng.

### M10-01 — Quy mô mở rộng và content beta — DEFERRED

**Phụ thuộc:** M9-02. **Quyết định:** số người/thời lượng đích và scope beta được duyệt. **Sản phẩm:** bản beta theo cấu hình đã kiểm.

- Kiểm số người đích bằng trận có tải tương ứng; không tự chuyển về sáu đội × ba.
- Chốt content cần phát hành; 162 node catalog không mặc định đều phải enable trong beta.
- Chạy trọn entry/build/loot/zone/elimination/result trong tải đích, kèm log và lỗi còn lại.

### M10-02 — Hardening và hồ sơ bàn giao beta — DEFERRED

**Phụ thuộc:** M10-01. **Sản phẩm:** bản kiểm ổn định, danh sách nội dung/asset và release checklist riêng.

- Xử lý blocker và rủi ro mất/nhân state, crash, exploit và tụt hiệu năng theo ngưỡng đã duyệt.
- Kiểm các luồng chính trên thiết bị/mạng mục tiêu; ghi phiên bản engine/content và kết quả có thể tái hiện.
- Kiểm nguồn asset/nội dung, cấu hình phát hành và việc còn phải duyệt trước phát hành; xuất bản/đẩy store không thuộc quyền tự động của task này.

## 11. Change Log

| Ngày | Phiên bản | Thay đổi |
|---|---|---|
| 2026-10-16 | 1.0 | Chia M0–M10 thành task có phụ thuộc, đầu ra và nghiệm thu; bổ sung nguồn tài nguyên tối thiểu trước học node, đề xuất spike M3-NET và chia M6A/M6B |
| 2026-10-16 | 1.1 | Giới hạn đường nghiệm thu ở solo hai người/20–25 phút; M6B là nhánh mở rộng, M9/M10 deferred, không bắt tăng số người để hoàn thành phiên bản hiện tại |
| 2026-10-16 | 1.2 | Đồng bộ LOOT-04/SOLO-SUB-08/BUILD-03, bổ sung ca kiểm giao dịch rơi đồ, thanh tẩy và từ chối mua trong combat |
| 2026-10-16 | 2.0 | Backlog chính thức Uchiha/Hỏa/hai hướng build cho hai người; thêm ca biên 5s/60s, pity 5%/30s/reset/túi đầy, hòa cuối tick và disconnect không timeout; M6B/M9/M10 deferred |
| 2026-10-16 | 2.1 | Antigravity tự làm/test/sửa đến candidate M8 theo AUTOPILOT; dùng profile/generate_image, loại cổng chờ duyệt từng task, tách kiểm Android thật khỏi phụ thuộc code độc lập và thêm đầu ra bàn giao chạy được |
