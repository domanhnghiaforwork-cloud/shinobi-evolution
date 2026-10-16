# AGENTS.md — Hợp đồng làm việc cho AI

> Dự án: **Shinobi Evolution** (tên nội bộ). Ngôn ngữ trao đổi và tài liệu: **tiếng Việt**. Tên lớp, hàm, biến và ID kỹ năng: **tiếng Anh**. Phiên bản tài liệu: 1.0 — 2026-10-16.
>
> Đọc file này trước khi sửa bất kỳ thứ gì. Đây là hướng dẫn cho các agent; **không phải** nguồn sự thật về cân bằng gameplay.

## 0. Bối cảnh phải nhớ

- Game **PvPvE sinh tồn lai MOBA + RPG trong trận**, lấy cảm hứng từ thế giới nhẫn giả; **không** phải game nhập vai tuyến tính hoặc MOBA có tướng cố định.
- Trước trận chọn gia tộc, thiên phú/hệ chakra, chuyên môn và preset phát triển. Trong trận farm XP/Ryō, săn vật phẩm mở nhánh, tự xây build và chiến đấu trên bản đồ lớn.
- Mục tiêu: **Android landscape trước**, iOS và PC cân nhắc sau. Engine **Godot 4 stable phiên bản đã khóa trong dự án**, **GDScript**, đồ họa **2D HD Pixel Art**, camera **top-down 3/4 kiểu MOBA**.
- **VS Code** là nơi xem/quản lý code. **Antigravity** lập trình chính; **Codex** mặc định **review chỉ đọc**. **Godot Editor và điện thoại thật** là nơi kiểm thử.
- Trận đích (chưa xác nhận bằng playtest): **18 người / 6 đội × 3, 42 phút, cấp 20, 12 SP, 4 active + 1 ultimate + 3 passive + Thế thân riêng**. Các milestone ban đầu nhỏ hơn rất nhiều.
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
| Agent được làm gì và phải báo cáo gì? | `AGENTS.md` | — |

**Thứ tự xử lý mâu thuẫn:** yêu cầu mới nhất được người dùng chấp thuận > quyết định ghi rõ là **CHỐT** trong tài liệu liên quan > đặc tả thiết kế chi tiết > dữ liệu mẫu > suy đoán của agent. Khi có xung đột không rõ, **dừng phần bị ảnh hưởng và liệt kê câu hỏi/đề xuất**, không tự sửa luật chơi. Tài liệu mô tả luật, JSON chứa bản ghi; khi mâu thuẫn ID, giữ nguyên dữ liệu cho đến khi báo và được duyệt thay đổi.

**Trước mỗi task** chỉ đọc file cần thiết, nhưng bắt buộc đọc `AGENTS.md` và `docs/ARCHITECTURE.md`; đọc `GAME_DESIGN.md` nếu tác động gameplay; đọc `SKILL_SYSTEM.md` + `skills.json` nếu tác động kỹ năng, gia tộc, loot, PvP balance.

## 2. Vai trò phân tách

### Antigravity — Main Developer

1. Đọc yêu cầu và tài liệu nguồn; kiểm tra trạng thái `git status` trước khi thay đổi.
2. Đề xuất kế hoạch ngắn gồm **phạm vi, file sửa, tiêu chí nghiệm thu, rủi ro**.
3. Mỗi lần làm **một feature có thể chạy thử**. Chỉ sửa file cần thiết. Không viết cả hệ thống 162 skills trong một lượt.
4. Ưu tiên scene nhỏ, GDScript có kiểu dữ liệu, composition và dữ liệu ngoài code. Khi không đủ đặc tả, dùng **stub có nhãn TODO** hoặc đề nghị quyết định; **không giả tạo xác suất/drop/stat lore**.
5. Thực hiện kiểm tra (parse project, headless test khi khả thi, mở scene, checklist thủ công); ghi **đã chạy / chưa chạy / thất bại** trung thực.
6. Bàn giao Git diff và bản mô tả kết quả cho Codex; tiếp nhận findings, sửa tối thiểu và cho review lại.
7. **Không tự tạo commit, push, merge, cài phụ thuộc, xóa asset lớn, thay build/export signing, đổi kiến trúc hoặc thêm backend mới** khi chưa có phê duyệt.

### Codex — Independent Reviewer

1. **Chỉ đọc và review** mặc định; không tạo/sửa/xóa file, không tự chạy formatter ghi đè. Nếu muốn chạy test có tác dụng ghi file, báo trước.
2. Kiểm tra **diff của task** + ngữ cảnh tối thiểu; không review lại cả codebase trừ khi có dấu hiệu lỗi lan rộng.
3. Báo lỗi **P0 Blocker / P1 High / P2 Medium / P3 Low**, nêu file + dòng hoặc node scene + kịch bản tái hiện + hậu quả + gợi ý sửa.
4. Phân biệt **bug đã chứng minh**, **rủi ro cần test**, **ý kiến phong cách**. Không chế tạo lỗi hoặc thông số benchmark.
5. Tập trung: GDScript/Godot 4 API, dependency scene, InputMap, null, save/load, graph gating, server authority, Android performance, VFX visibility, UI safe area, testability.
6. Kết luận **PASS / NEEDS FIX / BLOCKED**, kèm danh sách kiểm thử. PASS không có nghĩa là đã chứng minh game không có bug.

### Người dùng — Product Owner

Phê duyệt thay đổi gameplay/kiến trúc quan trọng, duyệt diff, kiểm thử cảm giác điều khiển, quyết định art direction và ưu tiên phát triển. Agent không tự nhận thay quyền phê duyệt.

## 3. Quy ước kỹ thuật bắt buộc

- Godot **4.x đã pin**, **GDScript**; không tự chuyển sang Unity/C#, C++ hay Godot .NET.
- Dùng `snake_case` cho file/hàm/biến, `PascalCase` cho class/scene type, `UPPER_SNAKE_CASE` cho hằng và skill ID. Dùng `@export` và `@onready` có kiểm soát; ưu tiên type hints.
- Scene mô-đun; UI không trực tiếp trừ HP/Ryō hoặc sửa inventory. Controller phát **intent**, domain xử lý, view chỉ render kết quả.
- Không nhét 162 kỹ năng vào một `match skill_id` khổng lồ. Loader đọc catalog, combat runtime qua các hành vi tái sử dụng (projectile/area/buff/dash/summon/trap); node chưa có thực thi bị từ chối trang bị.
- **Tiên quyết AND/OR, gate cá biệt và loại trừ lẫn nhau** phải được kiểm tra. Quy tắc `unlock_gate` mô tả bằng tiếng Việt **không được âm thầm coi là đã thỏa**; mặc định **fail-closed** khi chưa có predicate triển khai.
- Sức mạnh huyết kế khác bí truyền; kết hợp Hỏa+Phong hoặc Thủy+Lôi **không** sinh huyết kế mới; `source_label=game_design` là sáng tạo game.
- Không hardcode drop ngẫu nhiên trong UI/client. RNG quyết định trên authority, có seed/log khi test, có cơ chế pity theo thiết kế.
- PvP/multiplayer khi triển khai: **server authoritative** về XP, currency, loot, gate, vị trí hợp lệ, cooldown, hit, HP, thắng thua. Không tin RPC client báo damage/drop/unlock.
- VFX pixel: nearest-neighbor cho world sprite, telegraph trước đòn mạnh, ưu tiên dễ đọc trong teamfight, giới hạn phân thân/triệu hồi/particle; đo FPS trên Android thật.
- Không đưa token/API key, signing keystore, credentials hay dữ liệu cá nhân vào Git. Không chạy lệnh destructively (`rm -rf`, reset --hard, forced push) khi chưa có phép.

## 4. Quy trình một task

1. **SPEC:** tóm tắt mục tiêu, phụ thuộc, file liên quan; tiêu chí hoàn thành kiểm được.
2. **PLAN:** nêu cách triển khai nhỏ nhất; cảnh báo xung đột tài liệu hoặc cổng mở khóa chưa đủ luật.
3. **IMPLEMENT:** Antigravity chỉnh trong nhánh Git tính năng, giữ diff gọn; không tự refactor không liên quan.
4. **TEST:** compile/import Godot headless nếu có CLI, unit tests + smoke test; kiểm tra trên điện thoại nếu đụng UI/mobile.
5. **REVIEW:** Codex chỉ đọc diff, trả findings có bằng chứng.
6. **FIX:** Antigravity sửa P0/P1/P2 được xác nhận; Codex re-review.
7. **ACCEPT:** người dùng thử Godot và phê duyệt, sau đó commit/merge.

Mẫu báo cáo kết thúc task:

```text
Task / Nhánh Git:
Thay đổi: [file + lý do]
Đã kiểm tra: [lệnh + kết quả]
Chưa kiểm tra: [lý do]
Codex: [PASS / NEEDS FIX / BLOCKED + issue còn lại]
Ảnh hưởng Android/network/data:
Hướng dẫn người dùng thử trong Godot:
Việc đề nghị tiếp theo:
```

## 5. Chính sách thay đổi tài liệu và dữ liệu

- Mọi thay đổi luật gameplay: cập nhật `GAME_DESIGN.md`/`SKILL_SYSTEM.md` trước hoặc cùng task, có mục **Decision/Change Log**.
- Thay đổi cấu trúc module, protocol, storage: cập nhật `ARCHITECTURE.md` và test migration.
- Thay đổi `skills.json`: không sửa ID cũ nếu đã tham chiếu save/replay; cập nhật `schema_version` nếu breaking; validate toàn bộ `requires_all`, `requires_any` và synergy refs trước merge.
- Catalog hiện có **chưa đủ combat stats**. Không tự invent damage/cooldown như cân bằng đã chốt; thêm theo các đợt prototype có lý do, benchmark và phê duyệt.
- Roadmap phân biệt rõ **planned / in_progress / done**; không đánh dấu done chỉ vì code được sinh ra.

## 6. Definition of Done chung

- Có tiêu chí nghiệm thu cụ thể được người dùng xác nhận; chạy thử bằng Godot **không lỗi blocker**; không xuất hiện input/visual regression rõ ràng.
- Code có kiểm thử hành vi chính/edge-case liên quan; nếu thay dữ liệu graph phải chạy validator và lưu số lượng nút/synergy.
- Nếu chạm PvP, client không thể tự cấp tiền/đồ/kỹ năng; nếu chạm UI, điều khiển chạm và safe area kiểm được.
- Có diff được Codex review, findings P0/P1 được giải quyết; tài liệu/roadmap cập nhật nếu cần.

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
