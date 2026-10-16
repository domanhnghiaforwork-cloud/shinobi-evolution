# Shinobi Evolution

Dự án **PvPvE sinh tồn solo** bằng Godot, phạm vi hiện tại **hai người mỗi trận**, mỗi người một phe, người sống sót cuối cùng thắng. Chọn vùng xuất phát rồi spawn ngẫu nhiên với khoảng cách an toàn; thời lượng mục tiêu **20–25 phút**. Trọng tâm là loot, farm quái lấy XP, phát triển build bằng XP/SP/Ryō và vòng bo.

Solo không hồi sinh hoặc chiếm cứ điểm buff. Thế thân là bị động dùng cuộn: một cuộn khởi đầu, cap hai; khi sẵn sàng sẽ tự tiêu cuộn trước đòn gây chết (kể cả vòng bo), hồi HP theo cấu hình rồi tàng hình và bắt đầu cooldown. Trong cooldown vẫn có thể chết dù còn cuộn; tàng hình vẫn nhận damage và lộ khi gây/nhận damage.

Thế thân kích hoạt xóa khống chế và hiệu ứng bất lợi đang có; hiệu ứng mới vẫn áp được ngay. Chết rơi toàn bộ vật tư đang mang, không rơi XP/SP/Ryō hoặc kỹ năng đã học. Học node và đổi trang bị chỉ ngoài giao tranh; trong giao tranh được xem cây.

## Tài liệu dự án

**Bản khung 2.1, giữ luật gameplay 2.0:** Uchiha + Hỏa, hai hướng Hỏa thuật và Ảo thuật cho trận hai người. Antigravity bắt đầu M0-01, tự làm/test/sửa theo phụ thuộc đến M8; người dùng nghiệm thu bản chơi được cuối. Profile có 22 ID kế hoạch và hai preset, handler/stat từng chiêu đặc tả theo lô; mở rộng clan/hệ/số người để sau.

Ngoài giao tranh sau 5 giây. Cấu hình Thế thân thử đầu tiên: HP về 25% tối đa, tàng hình tối đa 3 giây, hồi chiêu 60 giây. Cả hai chết cùng tick thì hòa; mất kết nối không tự loại, nhân vật vẫn chịu sát thương. Bo cuối thu hết vùng an toàn. Tư liệu kỹ năng chung túi giới hạn ô; phần pity khi đầy giữ quyền nhận riêng.

- [GAME_DESIGN](docs/GAME_DESIGN.md): trải nghiệm solo, luật trận, kinh tế và sinh tồn.
- [SKILL_SYSTEM](docs/SKILL_SYSTEM.md): đồ thị, gate, loadout, loot/pity và Thế thân bị động.
- [ARCHITECTURE](docs/ARCHITECTURE.md): module, authority và hợp đồng kỹ thuật.
- [GRAPHICS_DESIGN](docs/GRAPHICS_DESIGN.md): đồ họa, HUD và pipeline asset.
- [DEVELOPMENT_ROADMAP](docs/DEVELOPMENT_ROADMAP.md): milestone, phụ thuộc và nghiệm thu.
- [TASK_BACKLOG](docs/TASK_BACKLOG.md): task theo giai đoạn, điều kiện bắt đầu và tiêu chí kiểm chứng.
- [ANTIGRAVITY_AUTOPILOT](docs/ANTIGRAVITY_AUTOPILOT.md): quyền tự triển khai đến M8, kiểm thử, sửa lỗi và bàn giao bản chơi được.
- [ART_GENERATION_GUIDE](docs/ART_GENERATION_GUIDE.md): master prompt, JOB mẫu và quy trình dùng `generate_image` tích hợp.
- [Prototype profile](data/prototypes/solo_first_playable.json): số liệu thử, 22 node dự kiến và hai preset đầu tiên; không tự bật runtime.
- [AUTOPILOT_REVIEW](docs/AUTOPILOT_REVIEW.md): kết quả rà soát cấu hình và các giới hạn kiểm tra đã chạy.
- [DESIGN_DECISIONS](docs/DESIGN_DECISIONS.md): lựa chọn đã chốt, câu hỏi còn mở và quyết định đã thay thế.
- [AGENTS](AGENTS.md): quy tắc làm việc của các agent.

## Bắt đầu

Gửi Antigravity một lệnh:

```text
Đọc AGENTS.md và docs/ANTIGRAVITY_AUTOPILOT.md rồi tự triển khai liên tục đến PLAYABLE_CANDIDATE M8, dùng generate_image theo docs/ART_GENERATION_GUIDE.md; tự test, sửa lỗi, rà soát và bàn giao bản hai người chơi được thực tế để tôi nghiệm thu, không dừng xin duyệt từng task/asset.
```

Antigravity bắt đầu M0-01 từ project hiện có; người dùng nhận hướng dẫn mở game, chạy hai client/LAN, bản debug và bằng chứng kiểm thử ở cuối. Các kiểm tra cần điện thoại/quyền công cụ thực tế phải được báo đúng trạng thái, không suy từ test desktop.

## Cấu trúc thư mục

- `docs/`: tài liệu thiết kế game, kiến trúc và hệ thống kỹ năng.
- `scenes/`: các scene chính, nhân vật, kẻ địch, bản đồ và giao diện.
- `scripts/`: mã nguồn theo từng hệ thống.
- `data/`: dữ liệu kỹ năng, gia tộc và vật phẩm.
- `assets/`: hình ảnh, hoạt ảnh, hiệu ứng, tileset và âm thanh.
- `tests/`: kiểm thử của dự án.

Các thư mục rỗng có file `.gitkeep` để Git theo dõi. Có thể xóa file này khi thư mục đã có nội dung.
