# ANTIGRAVITY_AUTOPILOT.md — Triển khai đến bản chơi được

**Phiên bản:** 1.0 • **Ngày:** 2026-10-16 • **Phạm vi được giao:** baseline solo hai người, Uchiha/Hỏa, đến hết M8. Người dùng nghiệm thu khi chơi được thực tế.

## 1. Lệnh giao việc và quyền thực hiện

Khi người dùng giao bắt đầu theo tài liệu này, Antigravity được tiếp tục từ task hiện tại đến bản chơi được, không cần xin duyệt từng plan, task, thông số prototype hoặc asset. Đây là cách thực hiện yêu cầu mới nhất, thay quy trình dừng chờ duyệt từng bước trước đây. Luật gameplay đã CHỐT vẫn giữ hiệu lực.

Đọc theo thứ tự: `AGENTS.md` → tài liệu này → `ARCHITECTURE.md` → `GAME_DESIGN.md` → `SKILL_SYSTEM.md` → `GRAPHICS_DESIGN.md` → `ART_GENERATION_GUIDE.md` → `TASK_BACKLOG.md` → `data/prototypes/solo_first_playable.json`. Đọc catalog theo tập ID cần làm. Kiểm Git và tiến độ thực tế; không khởi tạo lại project hoặc xóa thay đổi có sẵn.

Preflight đã có sẵn, dùng Python 3 stdlib, không ghi file: `python tools/validate_framework.py --self-test`. Chạy ở đầu và sau thay profile/catalog/task. Đây là kiểm tĩnh, không thay test Godot/ảnh/gameplay phía dưới.

**Được tự làm:** tạo/sửa scene, GDScript, test, profile prototype, manifest runtime, dữ liệu gate đã đặc tả; tạo art bằng `generate_image`; xử lý/đóng gói PNG; tạo branch local; sửa renderer/config debug/export preset; chạy server và hai client; tạo bản Windows debug và Android debug. Lập plan ngắn rồi thực hiện, không dừng ở plan. Không tự commit/push/merge/publish.

**Được tự quyết trong phạm vi:** chi tiết kỹ thuật còn OPEN, danh sách handler theo tập ID được giao, số liệu thử chưa được Product Owner chốt, cách tổ chức test và asset. Ghi lựa chọn, lý do, phạm vi và kịch bản kiểm chứng **trước khi** triển khai; dùng nhãn `PROTOTYPE_DEFAULT` hoặc `IMPLEMENTATION_DECISION`, không giả nhận Product Owner đã duyệt từng con số. Được điều chỉnh `tunable_defaults` khi có kết quả đo. Muốn đổi `fixed_rules` hoặc `owner_selected_test_values` phải có yêu cầu mới; không sửa luật để làm test qua.

**Công cụ local:** tìm bản đã cài trước. Khi cần, được lấy Godot Standard/export templates và công cụ xử lý ảnh từ nguồn chính thức, đặt portable trong `.tools/` hoặc môi trường dự án; không cài global/admin, thay PATH toàn máy hoặc chấp nhận thỏa thuận pháp lý thay người dùng. Không thêm backend trả phí/tài khoản dịch vụ, không đổi release signing. Không sửa cài đặt quyền/approval của Antigravity để vượt hạn chế công cụ. Thiếu quyền, quota hoặc binary là điều kiện thực tế phải báo, không giả kết quả; tiếp tục phần không phụ thuộc trước.

## 2. Đích bàn giao có thể chơi

Hoàn thành một bản có thể đi bằng input thật từ menu đến trận và kết quả:

1. Chạy server local/LAN và hai client; chọn vùng xuất phát, spawn an toàn, mỗi người một cuộn.
2. Di chuyển/camera, đánh thường, farm hai loại quái và boss; XP/Ryō/SP vận hành, hai hướng build Hỏa/Ảo khác nhau rõ.
3. Học/trang bị qua UI, kiểm timer combat 5s; không hoàn điểm, không cấp node ngoài allowlist.
4. Loot công khai, túi có giới hạn, cuộn Thế thân cap hai, vật tư rơi khi chết; pity đầy túi có quyền chờ riêng.
5. Thế thân 25%/3s/60s, thanh tẩy, damage phá ẩn, hit tiếp theo có thể giết; vòng bo kể cả lethal damage vẫn dùng cùng resolver.
6. Vòng bo đến hết vùng an toàn; người cuối thắng, cùng chết trong tick thì hòa; disconnect đứng yên không tự loại, reconnect cùng actor.
7. Result → về menu → bắt đầu trận mới, không giữ tiến trình/sinh đồ trùng từ trận cũ.
8. Art runtime do `generate_image` tạo, có animation và UI đọc được; không bàn giao toàn hình khối placeholder với nhãn hoàn chỉnh.

PC là nơi tự kiểm/dev và một client debug; **Android landscape vẫn là đích**. Bản bàn giao gồm launcher local, hướng dẫn hai người/LAN, Windows debug và APK debug nếu toolchain hoạt động. Không cần matchmaking công cộng, tài khoản, Nakama, rank, store hoặc M6B/M9/M10.

## 3. Thứ tự làm và cách tiếp tục

Đường chính: M0 → M1 → M2 → M3 → M4 → M5 → M6A → M7 → M8. M3-NET-01 được phép làm sau M3 để thử server hai client sớm; không chờ mở rộng content. M6B/M9/M10 giữ DEFERRED.

Mỗi task: **đọc SPEC → lập brief → làm → chạy kiểm tra → sửa lỗi → kiểm lại → self-review → cập nhật bằng chứng → task kế tiếp**. Task nhỏ giúp kiểm được, không có nghĩa phải dừng cuộc giao việc sau mỗi task. Chưa đủ thông số thử thì dùng profile và ghi bổ sung; không treo task chỉ vì tài liệu còn chữ OPEN.

Trạng thái thống nhất:

| Trạng thái | Ý nghĩa / quyền tiếp tục |
|---|---|
| PLANNED | Chưa làm |
| READY | Đủ brief/phụ thuộc và nằm trong quyền đã giao; không cần duyệt lại từng task |
| IN_PROGRESS | Đang làm |
| SELF_REVIEW | Antigravity đang tự rà diff; không ghi là Codex review |
| VERIFIED | Kiểm tra áp dụng đã chạy đạt, có log; được tự sang task tiếp theo |
| PLAYABLE_CANDIDATE | Có gói chơi được để người dùng nghiệm thu; nêu rõ kiểm tra Android thật còn thiếu nếu có |
| ACCEPTED / DONE | Người dùng đã chơi và chấp thuận phạm vi đó |
| BLOCKED_EXTERNAL | Thiếu công cụ/quyền/thiết bị thật, có bằng chứng và cách tiếp tục cụ thể |
| DEFERRED | Ngoài baseline hiện tại |

Codex review độc lập nếu có sẵn là lớp kiểm bổ sung; không bắt người dùng chuyển diff qua lại trước mỗi task. Khi không gọi được Codex, tự review có checklist và ghi `independent_review=NOT_RUN`. Không tự nhận Codex PASS. Không chờ commit hoặc nghiệm thu người dùng để tiếp tục task đã VERIFIED.

Tạo/cập nhật `docs/reports/IMPLEMENTATION_STATUS.md` khi bắt đầu code: task hiện tại, trạng thái từng task, file sửa, lệnh/test/log, quyết định prototype, lỗi còn lại, bước kế tiếp. Sau lỗi, gián đoạn hay đổi phiên phải đọc lại checkpoint/Git và chạy kiểm tra liên quan; không đánh dấu DONE hoặc làm lại toàn dự án chỉ vì mất ngữ cảnh.

## 4. Cấu hình kỹ thuật mặc định

- M0 xác nhận executable/version/build và API; `4.7` trong `project.godot` không chứng minh binary đã cài. Dùng Godot 4 Standard tương thích, pin build thực tế; không chuyển major hoặc ghi đè project để sửa lỗi môi trường.
- Cho prototype 2D Android, được cấu hình Compatibility, viewport world 640×360 với policy vùng nhìn ngang nhau giữa các aspect ratio, UI safe area riêng; kiểm trên render thực. Ghi diff renderer trước/sau. Thông số art theo GRAPHICS/ART guide.
- Online local/LAN: **Godot server riêng authoritative + ENet** mặc định, không tin client. Một server và hai client tách process; server không là một người chơi thứ ba. Prototype tick 30Hz, snapshot 15Hz theo profile, có thể điều chỉnh sau đo.
- Server chỉ bắt đầu running sau khi đủ hai người đã hoàn tất entry/ready; không xét alive_count=1 lúc preparing thành thắng. Reconnect dùng session token ngẫu nhiên do server phát, gắn match/player; không tin player_id client tự khai. Hai client local dùng profile/token cache riêng, token không ghi Git/log. Người thứ ba không chiếm slot actor disconnected; thiếu token hợp lệ không được điều khiển actor cũ.
- Tách catalog và runtime: giữ `skills.json` là nguồn graph; tạo `data/runtime/content_manifest.json` và `data/runtime/abilities.json` khi triển khai. Manifest override trạng thái runtime **theo từng ID** sau handler + test; không lật quyền toàn 162 node. `approved_for_runtime=false` của catalog nghĩa không được nạp trực tiếp làm bộ combat. Trạng thái hiệu lực ngoài allowlist hoặc thiếu binding/predicate là fail-closed. Loader phải test phép hợp nhất này.
- Windows launcher sau khi triển khai: `tools/run_local_playtest.ps1`; test runner: `tools/run_checks.ps1`; hướng dẫn: `docs/PLAY_GUIDE.md`. Đây là đầu ra phải tạo, **chưa phải script đã tồn tại**. Chạy bằng đường dẫn executable/argument array, không `Invoke-Expression` hay ghép chuỗi lệnh từ dữ liệu.
- Launcher có tùy chọn client thứ hai chạy test bot để một người có thể thử luồng ngay; ghi rõ là test fixture, bot gửi cùng intent/network contract, không sửa thẳng state để giả thành công. Main mode vẫn hỗ trợ hai người thật trên LAN; kết quả bot test không được ghi là playtest hai người thật.
- UI hiển thị bốn active + ultimate, tool và attack; ba passive, trait và Thế thân là trạng thái. Slot chưa có nội dung vẫn disabled/empty, không dựng ability giả để đủ ô. Bản đầu không bắt đủ ba passive khác nhau.

## 5. Tập nội dung và số liệu thử

[solo_first_playable.json](../data/prototypes/solo_first_playable.json) là điểm xuất phát có thể đọc bằng máy. Không ghi các số này thành cân bằng canonical. Runtime config do task tạo phải lưu profile/seed/version được dùng.

- Tập kế hoạch 22 node có đóng đủ tiền đề; hai preset tốn lần lượt 9 và 8 SP theo catalog, chưa tính lựa chọn bổ sung. Sáu T0 được grant; node sở hữu không đồng nghĩa thêm nút HUD.
- `FIRE_ZONE` và `GEN_DOMAIN` là hai ultimate prototype; T4 có thể là ultimate, không tự mở T5. `UCH_EYE1` là trait slot, `UCH_FIRE` là passive; phân loại các node khác theo effect và ghi manifest trước code.
- `UCH_FIRE` giữ ý định giảm chi phí học Hỏa, không đổi thành buff damage: profile thử giảm 10% **Ryō** của node Hỏa mua sau khi passive được học/trang bị, SP không giảm; làm tròn chi phí nguyên theo một quy tắc domain, không hoàn khoản đã mua. Tháo passive chỉ mất giảm giá cho lần mua sau, không sửa learned state hoặc cấp lại tiền. Kiểm trước/sau học/tháo và request lặp.
- `GATE_FIRE_ROOT`: resolver thiên phú FIRE, không mặc định mọi nature đều hợp lệ. `GATE_UCH_EYE1`: Uchiha **và** cờ thức tỉnh cơ bản, cờ do authority cấp sau ba normal mob kills ở profile thử; không tự đặt true vì đã chọn clan.
- `BASE_SHADOWCLONE`: giữ OR cuộn/huấn luyện. Ba `SHADOW_CLONE_PAGE` đổi thành `SCROLL_SHADOW_CLONE`; hoặc 20 normal mob kills cấp cờ `training.shadow_clone_basic` theo profile. Resolver triển khai/test cả hai đường; không viết true vào gate text. Nếu training đã đủ thì không tự tiêu cuộn dư; nếu dùng đường item thì consume cuộn cùng transaction học, retry không tiêu hai lần.
- Các item ID trên là ID prototype mới, không thay skill ID. Rare group đầu tiên là `SHADOW_CLONE_PAGES`; pity mục tiêu là một page, không đợi đủ ba page mới tính thành công. Điều kiện clan/tier/SP/Ryō vẫn kiểm khi học.
- Khi M5 có inventory, cuộn Thế thân là item trong túi và bị động đọc/tiêu cùng nguồn số lượng đó; không giữ thêm một bộ charge miễn phí ngoài túi. Tổng cuộn trên mọi stack vẫn cap hai. Tích hợp M3→M5 không cấp lại cuộn đầu trận, không làm rơi lại cuộn đã tiêu trong chính giao dịch Thế thân.
- Thu nhập được mô phỏng trước chơi; tổng SP level 1..20 phải đúng 12. Đo thời gian T2/T3/T4, farm và gặp đối thủ; điều chỉnh số liệu thử khi nhịp quá nhanh/chậm, giữ mục tiêu 20–25 phút.
- Stat ability còn thiếu: lập bảng `skill_id / archetype / cast / damage / chakra / cooldown / range / CC / counterplay / slot` trước implementation. Có thể tự chọn số prototype hợp lý, ghi lý do và test, không dừng xin người dùng duyệt từng chiêu. Giữ ý định effect catalog, tránh hard CC vô hạn; tuyệt đối không bypass gate, đổi cách thắng hoặc cấp miễn sát thương cho Thế thân.
- Đổi target pity lưu revision/epoch; reward cũ giữ target đã đăng ký, không cộng miss sang target mới. Một quyền bảo hiểm đã cấp không được phát lại khi đầy túi; ledger/claim và reward đến sau phải có thứ tự xác định. Test trước khi bật nhóm loot.
- Bo có tổng phase khởi đầu 23 phút theo profile, sau đó damage tăng đến 100% max HP/tick để chống kéo dài vô hạn; vẫn giải quyết Thế thân như mọi lethal damage. Khi hết phase cuối, `safe_area_exists=false`: **ngay cả actor ở đúng tâm radius=0 cũng ở ngoài vùng**, không dùng so sánh distance<=radius để giữ lại một điểm an toàn.

## 6. Kiểm thử bắt buộc và bằng chứng

Antigravity tạo test runner tối thiểu bằng Godot/GDScript và PowerShell, tránh framework phụ thuộc nặng. Test trên domain thật/scene thật; không chép lại thuật toán vào test để luôn xanh. **Không** dùng bot/fixture sửa thẳng HP/túi để thay bằng chứng luồng gameplay cuối.

| Lớp kiểm tra | Phải chứng minh |
|---|---|
| Import/parse | Project mở bằng engine đã pin, toàn bộ GDScript/scene/resource liên quan không lỗi |
| Catalog/runtime | 162/29/12, AND/OR, DAG, refs, gate fail-closed, allowlist/binding; hai preset đủ tiền đề/ngân sách |
| Domain | Mốc 5s/60s; Thế thân/cleanse/DOT/cùng tick; chi phí học atomic; inventory/rơi đồ; pity 3/4/5, reset/claim/retry |
| Integration | Menu → spawn → farm → học qua UI → loot → bo → thắng/hòa → result → trận mới |
| Network | Server + hai client thật; contest pickup, RPC giả mạo tiền/damage/unlock bị từ chối, disconnect >60s không tự loại, token sai bị từ chối, reconnect không nhân state |
| Visual/input | Chạy có render, ảnh/video thật; joystick + aim/cancel, safe area, animation/foot anchor, pixel filter, telegraph/stealth/pity UI |
| Export/device | Windows debug khởi động được; Android APK debug export được, INTERNET cho LAN; test máy thật nếu ADB/thiết bị được cấp quyền |

Network profiles tối thiểu: localhost/LAN bình thường; profile thử RTT 150ms/jitter 30ms/loss 1%; stress RTT 300ms/jitter 60ms/loss 3%. Đây là cấu hình thử, không phải benchmark đã đạt. Nếu không có network emulator, được tạo transport test adapter có seed; phải ghi simulated, không gọi là thử mạng thật.

Lệnh tham chiếu, thay bằng binary/preset/test script thực tế sau `--version`/`--help`:

```powershell
& $godot_exe --headless --path . --editor --quit
& $godot_exe --headless --path . --script res://tests/run_all.gd
& $godot_exe --headless --path . --export-debug "Windows Desktop" builds/windows/shinobi_evolution.exe
& $godot_exe --headless --path . --export-debug "Android" builds/android/shinobi_evolution.apk
```

Thư mục output/preset/templates và `tests/run_all.gd` phải được tạo trước khi gọi. Runner trả exit code khác 0 khi fail; capture stdout/stderr và phát hiện parse/script errors, không kết luận pass chỉ vì process kết thúc. GDScript runner phải kế thừa `SceneTree`/`MainLoop` phù hợp API engine đã pin. Import có thể ghi cache, nằm trong quyền kiểm thử được giao.

Headless không chứng minh hình ảnh/touch đúng. Có test rendered riêng, screenshot gắn scenario và người/agent thực sự đã xem ảnh. Bot hai client chỉ là test, không thay nút điều khiển thật; ít nhất một lượt smoke gửi input qua UI/InputMap thật. Có một trận test gia tốc bằng profile riêng và **ít nhất một trận thời gian thực** với config bàn giao; không ghi trận gia tốc là đã đạt nhịp 20–25 phút.

Với test chạy lâu, theo dõi process/log theo lượt ngắn, cập nhật tiến độ và tiếp tục việc độc lập; không dùng một lệnh chờ khóa tương tác cả 23 phút. Không kết luận đã test bo cuối nếu trận kết thúc sớm do combat: cần scenario đưa cả hai đến phase cuối, kể cả actor tại đúng tâm, rồi kiểm thắng/hòa và Thế thân.

Đích thử Android ban đầu: 30 FPS ổn định, đo p95 frame time theo thiết bị; đây là ngưỡng prototype để sửa, không được ghi đã đạt khi chưa có máy thật. Không có thiết bị: ghi `NOT_RUN_DEVICE`, vẫn làm rendered desktop, touch-event simulation và export; để người dùng nghiệm thu trên điện thoại cuối cùng. Không đánh dấu DONE/mobile-verified vì emulator/desktop đạt.

## 7. Tự rà soát và điều kiện dừng

Sau task, tự tìm P0/P1/P2 liên quan, sửa và chạy lại đúng kiểm tra bị ảnh hưởng. Rà final gồm startup, call stack/error log, learned/equipped, gate/status, death/reward, network authority, asset provenance, manifest/pivot và clean restart. Không mở rộng refactor hoặc tạo thêm 162 handler.

Không kết thúc công việc ở một scene di chuyển, kế hoạch, bộ ảnh rời, code chưa chạy hoặc báo cáo hết milestone. Tiếp tục đến `PLAYABLE_CANDIDATE` cho phạm vi M8. Nếu công cụ thật bị chặn, lưu checkpoint, phần đã chạy/chưa chạy và lỗi cụ thể; không giấu bằng placeholder hay tự đánh dấu pass. Thiếu điện thoại thật không chặn hoàn tất phần có thể chạy trên máy, nhưng phải để trạng thái Android đúng thực tế.

Tạo `docs/reports/QA_REPORT.md` với **lệnh, thời điểm, engine/profile/seed, kết quả, đường dẫn log/ảnh/video và lỗi còn lại**. `docs/PLAY_GUIDE.md` phải nói cách mở game, chạy hai client/LAN, điều khiển, hai hướng build, APK, server IP/port và cách gửi bug. Đóng các process test do mình tạo; không kill process không thuộc task.

Người dùng nhận một gói có thể tự mở chơi, kèm hướng dẫn ngắn và các giới hạn có bằng chứng. Chỉ sau khi họ chơi/chấp thuận mới chuyển ACCEPTED/DONE. Tạo local checkpoint không cần commit; push, merge, deploy/store hoặc thanh toán là công việc khác.

## 8. Nguồn kỹ thuật đã đối chiếu

`generate_image` được tài liệu Antigravity liệt kê với `Prompt`, `ImageName`, `ImagePaths` tùy chọn; kiểm schema công cụ thực tế của phiên trước gọi: [Antigravity supported tools](https://antigravity.google/docs/hooks#supported-tools).

Mẫu CLI và lựa chọn ENet dựa trên tài liệu chính thức; khi triển khai phải đọc theo bản engine thực tế: [Godot command line](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html), [Godot multiplayer](https://docs.godotengine.org/en/stable/tutorials/networking/high_level_multiplayer.html).
