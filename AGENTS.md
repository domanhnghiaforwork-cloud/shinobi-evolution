# AGENTS.md — Hợp đồng làm việc cho AI

> Dự án: **Shinobi Evolution** (tên nội bộ). Ngôn ngữ trao đổi và tài liệu: **tiếng Việt**. Tên lớp, hàm, biến và ID kỹ năng: **tiếng Anh**. Phiên bản tài liệu: 2.1 — 2026-10-16.
>
> Đọc file này trước khi sửa bất kỳ thứ gì. Đây là hướng dẫn cho các agent; **không phải** nguồn sự thật về cân bằng gameplay.

**Chế độ giao việc hiện hành — người dùng đã ủy quyền:** khi được giao bắt đầu, Antigravity tự triển khai, tạo art, test, sửa và tự rà soát liên tục đến bản hai người chơi được M8; không dừng chờ duyệt từng task/asset. Người dùng nghiệm thu bằng chơi thực tế ở cuối. Đọc [ANTIGRAVITY_AUTOPILOT](docs/ANTIGRAVITY_AUTOPILOT.md), [ART_GENERATION_GUIDE](docs/ART_GENERATION_GUIDE.md) và [profile prototype](data/prototypes/solo_first_playable.json). Quyền này áp dụng chi tiết triển khai/thông số thử, không cho đổi luật CHỐT hoặc mở rộng M6B/M9/M10. `VERIFIED` cho phép sang task kế tiếp; chỉ người dùng chấp thuận mới `ACCEPTED/DONE`.

## 0. Bối cảnh phải nhớ

- Game **PvPvE sinh tồn solo**, mỗi người một phe, người sống sót cuối cùng thắng; lấy cảm hứng thế giới nhẫn giả. Sinh tồn, loot, vòng bo và phát triển build trong trận là trọng tâm; cảm hứng MOBA chỉ ở farm quái lấy XP.
- Trước trận chọn gia tộc, thiên phú/hệ chakra, chuyên môn và preset phát triển. Trong trận farm XP/Ryō, săn vật phẩm mở nhánh, tự xây build và chiến đấu trên bản đồ lớn.
- Mục tiêu: **Android landscape trước**, iOS và PC cân nhắc sau. Engine **Godot 4 Standard/GDScript**, binary/build chính xác xác nhận ở M0-01 theo ARCHITECTURE; đồ họa **2D HD Pixel Art**, camera **top-down 3/4 kiểu MOBA**.
- **VS Code** là nơi xem/quản lý code. **Antigravity** lập trình chính; **Codex** mặc định **review chỉ đọc**. **Godot Editor và điện thoại thật** là nơi kiểm thử.
- Mode chính **solo hai người/trận, không hồi sinh, không có cứ điểm chiếm giữ để nhận buff**. Chọn vùng xuất phát rồi spawn ngẫu nhiên có khoảng cách an toàn; mục tiêu thời lượng **20–25 phút**, không phải timeout. Cấp 20/12 SP cần kiểm chứng nhịp tiến trình. Tăng số người, chế độ đội và trụ hồi sinh để sau; không áp cấu hình đội cũ cho solo.
- **Thế thân bị động:** một cuộn khởi đầu, cap hai; tự tiêu cuộn trước lethal damage (kể cả vòng bo) khi cooldown sẵn sàng, hồi HP theo config, xóa CC/hiệu ứng bất lợi đang có rồi tàng hình và bắt đầu cooldown. Trong cooldown vẫn có thể chết dù còn cuộn. Tàng hình vẫn nhận damage, gây/nhận damage làm lộ thân; effect mới vẫn áp được ngay. Không có nút dùng chủ động. Đọc `SKILL_SYSTEM.md` §10.4 về profile thử đã duyệt và tương tác cần đặc tả theo handler.
- Tải kỹ năng mục tiêu: **4 active + 1 ultimate + 3 passive + Thế thân bị động riêng**; giữ XP/SP/Ryō và điều kiện SP/Ryō khi học node. Mỗi milestone triển khai tập nhỏ đã duyệt.
- Học node và đổi trang bị chỉ ngoài giao tranh; trong giao tranh được xem cây. Chết rơi toàn bộ vật tư, kể cả cuộn Thế thân còn lại; không rơi XP/SP/Ryō hoặc node đã học.
- **Baseline chính thức 2.0:** Uchiha + Hỏa, hai hướng Hỏa thuật/Ảo thuật. Ngoài combat sau 5s; Thế thân thử 25% max HP/3s stealth/60s cooldown. Cả hai chết cùng tick thì hòa; disconnect đứng yên, không timeout tự loại. Bo cuối hết vùng an toàn. Túi chung giới hạn ô, pity đầy túi thì chờ riêng không bị cướp. Tra luật chi tiết tại GAME_DESIGN/SKILL_SYSTEM, task tại TASK_BACKLOG.
- Dữ liệu gốc: `data/skills/skills.json` có **162 nút, 29 nhóm, 12 synergy**; là **catalog thiết kế**, **không** phải 162 kỹ năng có logic chiến đấu đã hoàn chỉnh.
- Nội dung, tên nhân vật/thuật và hình ảnh gắn Naruto có rủi ro quyền sở hữu trí tuệ. Dùng placeholder hoặc thiết kế gốc trong prototype; cần quyền phù hợp nếu phát hành sử dụng IP gốc.

## 1. Thẩm quyền tài liệu và cách tra cứu

| Loại câu hỏi | Nguồn chính | Đọc thêm |
|---|---|---|
| Game phải vận hành thế nào? | `docs/GAME_DESIGN.md` | `docs/DEVELOPMENT_ROADMAP.md` |
| Hệ thống/scene/API/module triển khai ở đâu? | `docs/ARCHITECTURE.md` | `project.godot`, code hiện hành |
| Nhẫn thuật, nhánh, khóa, tương tác được định nghĩa ra sao? | `docs/SKILL_SYSTEM.md` | `data/skills/skills.json` |
| Danh sách ID/nút/tiên quyết cụ thể? | `data/skills/skills.json` | `docs/SKILL_SYSTEM.md` |
| Công việc nào được phép thực hiện ngay? | Yêu cầu hiện tại của người dùng + roadmap đang được duyệt | Git diff, kiểm thử |
| Task nào phụ thuộc task nào và nghiệm thu ra sao? | `docs/TASK_BACKLOG.md` | `docs/DEVELOPMENT_ROADMAP.md` |
| Agent được làm gì và phải báo cáo gì? | `AGENTS.md` | — |
| Quyết định nào đang hiệu lực hoặc đã được thay thế? | Tài liệu nguồn tương ứng | `docs/DESIGN_DECISIONS.md` |
| Hình ảnh, HUD, asset và animation? | `docs/GRAPHICS_DESIGN.md` | `docs/GAME_DESIGN.md`, `docs/ARCHITECTURE.md` |
| Antigravity tự làm đến đâu, tự test và tiếp tục thế nào? | `docs/ANTIGRAVITY_AUTOPILOT.md` | `docs/TASK_BACKLOG.md` |
| Tạo hình bằng công cụ tích hợp nào, prompt và kiểm ảnh ra sao? | `docs/ART_GENERATION_GUIDE.md` | `docs/GRAPHICS_DESIGN.md` |
| Số liệu thử và tập ID đầu tiên? | `data/prototypes/solo_first_playable.json` | `docs/ANTIGRAVITY_AUTOPILOT.md` §5 |

**Thứ tự xử lý mâu thuẫn:** yêu cầu mới nhất của người dùng > luật **CHỐT** > đặc tả chi tiết > profile thử > suy đoán. Các bước chờ duyệt từng task/asset cũ được thay bằng AUTOPILOT hiện hành. Chi tiết OPEN trong baseline được Antigravity tự đặc tả/ghi lý do/test theo quyền đã giao; không hỏi lại mỗi lựa chọn thường lệ. Nếu thật sự xung đột với luật CHỐT hoặc ID bất biến, chỉ dừng phần bị ảnh hưởng, báo cụ thể và tiếp tục phần độc lập; không tự sửa luật để né lỗi.

**Trước mỗi task** chỉ đọc file cần thiết, nhưng bắt buộc đọc `AGENTS.md` và `docs/ARCHITECTURE.md`; đọc `GAME_DESIGN.md` nếu tác động gameplay; đọc `SKILL_SYSTEM.md` + `skills.json` nếu tác động kỹ năng, gia tộc, loot, PvP balance.

## 2. Vai trò phân tách

### Antigravity — Main Developer

1. Đọc yêu cầu và tài liệu nguồn; kiểm tra trạng thái `git status` trước khi thay đổi.
2. Ghi kế hoạch ngắn gồm **phạm vi, file sửa, tiêu chí kiểm, rủi ro**, rồi thực hiện; không dừng xin duyệt lại task thuộc baseline.
3. Mỗi lần làm **một feature có thể chạy thử**, kiểm đạt rồi tự sang task kế tiếp đến M8. Không viết cả hệ thống 162 skills hoặc chỉ dừng ở một scene di chuyển.
4. Ưu tiên scene nhỏ, typed GDScript, composition và dữ liệu ngoài code. Chi tiết chưa đủ được đặc tả bằng profile prototype trước code; giữ log lý do và test. TODO/stub chỉ cho ngoài scope, không coi tính năng baseline chưa chạy là hoàn chỉnh. Không giả tạo stat lore hoặc cân bằng đã chốt.
5. Thực hiện kiểm tra (parse project, headless test khi khả thi, mở scene, checklist thủ công); ghi **đã chạy / chưa chạy / thất bại** trung thực.
6. Tự review diff, sửa findings và kiểm lại. Nếu có Codex độc lập thì tiếp nhận review, không bắt người dùng chuyển diff từng lượt; nếu không có, ghi `independent_review=NOT_RUN`, không giả Codex PASS. Lưu checkpoint và tiếp tục task đã VERIFIED.
7. Được setup portable/dependency local, renderer và debug export theo AUTOPILOT; dùng `generate_image` cho art, tự validate/promote asset do mình tạo. **Không tự commit/push/merge/publish, cài global/admin, xóa asset người dùng, đổi release signing hoặc thêm dịch vụ trả phí**. Luật gameplay/kiến trúc cốt lõi ngoài quyền đã giao vẫn cần yêu cầu mới.

### Codex — Independent Reviewer

1. **Chỉ đọc và review** mặc định; không tạo/sửa/xóa file, không tự chạy formatter ghi đè. Nếu muốn chạy test có tác dụng ghi file, báo trước.
2. Kiểm tra **diff của task** + ngữ cảnh tối thiểu; không review lại cả codebase trừ khi có dấu hiệu lỗi lan rộng.
3. Báo lỗi **P0 Blocker / P1 High / P2 Medium / P3 Low**, nêu file + dòng hoặc node scene + kịch bản tái hiện + hậu quả + gợi ý sửa.
4. Phân biệt **bug đã chứng minh**, **rủi ro cần test**, **ý kiến phong cách**. Không chế tạo lỗi hoặc thông số benchmark.
5. Tập trung: GDScript/Godot 4 API, dependency scene, InputMap, null, save/load, graph gating, server authority, Android performance, VFX visibility, UI safe area, testability.
6. Kết luận **PASS / NEEDS FIX / BLOCKED**, kèm danh sách kiểm thử. PASS không có nghĩa là đã chứng minh game không có bug.

### Người dùng — Product Owner

Quyết định gameplay/art direction cốt lõi và nghiệm thu bản chơi được thực tế ở cuối. Không phải duyệt từng task, PNG hoặc số liệu prototype trong quá trình đã ủy quyền. Agent không tự nhận thay human acceptance.

## 3. Quy ước kỹ thuật bắt buộc

- Godot **4.x đã pin**, **GDScript**; không tự chuyển sang Unity/C#, C++ hay Godot .NET.
- Dùng `snake_case` cho file/hàm/biến, `PascalCase` cho class/scene type, `UPPER_SNAKE_CASE` cho hằng và skill ID. Dùng `@export` và `@onready` có kiểm soát; ưu tiên type hints.
- Scene mô-đun; UI không trực tiếp trừ HP/Ryō hoặc sửa inventory. Controller phát **intent**, domain xử lý, view chỉ render kết quả.
- Không nhét 162 kỹ năng vào một `match skill_id` khổng lồ. Catalog giữ graph; manifest runtime chỉ cấp trạng thái `implemented` theo ID sau handler/test. Node có trạng thái hiệu lực design_only, ngoài allowlist hoặc thiếu binding tiếp tục bị từ chối. Catalog không được dùng trực tiếp như runtime đã hoàn chỉnh.
- **Tiên quyết AND/OR, gate cá biệt và loại trừ lẫn nhau** phải được kiểm tra. Quy tắc `unlock_gate` mô tả bằng tiếng Việt **không được âm thầm coi là đã thỏa**; mặc định **fail-closed** khi chưa có predicate triển khai.
- Sức mạnh huyết kế khác bí truyền; kết hợp Hỏa+Phong hoặc Thủy+Lôi **không** sinh huyết kế mới; `source_label=game_design` là sáng tạo game.
- Không hardcode drop ngẫu nhiên trong UI/client. RNG quyết định trên authority, có seed/log khi test, có cơ chế pity theo thiết kế.
- PvP/multiplayer khi triển khai: **server authoritative** về XP, currency, loot, gate, vị trí hợp lệ, cooldown, hit, HP, thắng thua. Không tin RPC client báo damage/drop/unlock.
- VFX pixel: nearest-neighbor cho world sprite, telegraph trước đòn mạnh, ưu tiên dễ đọc trong teamfight, giới hạn phân thân/triệu hồi/particle; đo FPS trên Android thật.
- Không đưa token/API key, signing keystore, credentials hay dữ liệu cá nhân vào Git. Không chạy lệnh destructively (`rm -rf`, reset --hard, forced push) khi chưa có phép.

## 4. Quy trình một task

1. **SPEC:** đọc task/profile, bổ sung brief chi tiết trong quyền đã giao; tiêu chí kiểm được.
2. **PLAN:** ghi cách làm nhỏ nhất và file dự kiến; tự giải chi tiết thường lệ, không dừng chờ duyệt plan.
3. **IMPLEMENT:** Antigravity chỉnh trong nhánh Git tính năng, giữ diff gọn; không tự refactor không liên quan.
4. **TEST:** compile/import Godot headless nếu có CLI, unit tests + smoke test; kiểm tra trên điện thoại nếu đụng UI/mobile.
5. **SELF_REVIEW:** Antigravity tự rà diff, log và rendered output; Codex độc lập nếu sẵn có, ghi đúng ai đã review.
6. **FIX / VERIFIED:** sửa lỗi, kiểm lại phần liên quan, lưu bằng chứng và tự chuyển task kế tiếp.
7. **PLAYABLE_CANDIDATE / ACCEPT:** đến hết M8, bàn giao gói chạy được/hướng dẫn/QA; người dùng chơi rồi nghiệm thu. Commit/merge là quyền riêng, không là điều kiện để sang task đã VERIFIED.

Mẫu báo cáo kết thúc task:

```text
Task / Nhánh Git:
Thay đổi: [file + lý do]
Đã kiểm tra: [lệnh + kết quả]
Chưa kiểm tra: [lý do]
Self-review / independent review: [kết quả; NOT_RUN nếu chưa có reviewer độc lập]
Trạng thái: [VERIFIED / PLAYABLE_CANDIDATE / BLOCKED_EXTERNAL; không tự DONE]
Ảnh hưởng Android/network/data:
Hướng dẫn người dùng thử trong Godot:
Việc đề nghị tiếp theo:
```

## 5. Chính sách thay đổi tài liệu và dữ liệu

- Mọi thay đổi luật gameplay: cập nhật `GAME_DESIGN.md`/`SKILL_SYSTEM.md` trước hoặc cùng task, có mục **Decision/Change Log**.
- Thay đổi cấu trúc module, protocol, storage: cập nhật `ARCHITECTURE.md` và test migration.
- Thay đổi `skills.json`: không sửa ID cũ nếu đã tham chiếu save/replay; cập nhật `schema_version` nếu breaking; validate toàn bộ `requires_all`, `requires_any` và synergy refs trước merge.
- Catalog hiện có **chưa đủ combat stats**. Được tự chọn/chỉnh số prototype trong phạm vi AUTOPILOT/profile, có lý do và kết quả thử; không ghi là cân bằng cuối hoặc tự đổi giá trị người dùng đã chọn.
- Roadmap phân biệt rõ **planned / in_progress / done**; không đánh dấu done chỉ vì code được sinh ra.

## 6. Definition of Done chung

- Tiêu chí task theo baseline/quyền đã giao; Godot **không lỗi blocker**, không input/visual regression rõ. VERIFIED là kết quả kỹ thuật để tiếp tục, chưa phải nghiệm thu cuối.
- Code có kiểm thử hành vi chính/edge-case liên quan; nếu thay dữ liệu graph phải chạy validator và lưu số lượng nút/synergy.
- Nếu chạm PvP, client không thể tự cấp tiền/đồ/kỹ năng; nếu chạm UI, điều khiển chạm và safe area kiểm được.
- Có self-review và bằng chứng test; nếu có independent review thì ghi người/kết quả thật. Sửa P0/P1/P2 được xác nhận; tài liệu/roadmap cập nhật. Chỉ người dùng chơi/chấp thuận mới ACCEPTED/DONE.

## 7. Lệnh kiểm thử tham khảo (chỉ khi Godot executable đã cài)

```bash
# Ví dụ: thay 'godot' bằng đường dẫn CLI thực tế trên máy bạn.
godot --headless --path . --editor --quit
# Khi đã có main scene và smoke test:
godot --headless --path . --quit-after 60
```

Không tuyên bố các lệnh này đã chạy nếu chưa thực sự chạy. CLI/option cụ thể phải kiểm tra theo phiên bản Godot project đã pin.

## 8. Chú thích IP và an toàn tài sản

File danh mục có tên gia tộc, thuật và khái niệm Naruto để phục vụ thiết kế nội bộ. **Không** tự động nhập sprite/nhạc/anime footage có bản quyền. Trước beta thương mại, quyết định một trong hai: có giấy phép hợp lệ, hoặc đổi sang IP nguyên bản (tên, thiết kế, lore và nội dung được bảo hộ) theo tư vấn phù hợp.

## 9. Change Log

- 2026-10-16 — 2.1: theo yêu cầu mới, Antigravity tự làm/test/sửa đến M8, người dùng chỉ nghiệm thu cuối khi chơi được; thêm generate_image, profile prototype, VERIFIED và self-review không giả independent review. Giữ Codex reviewer mặc định và quyền thay tài liệu khi người dùng giao trực tiếp.
