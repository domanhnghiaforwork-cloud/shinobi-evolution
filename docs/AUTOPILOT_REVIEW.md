# AUTOPILOT_REVIEW.md — Rà soát bộ giao việc Antigravity

**Ngày:** 2026-10-16 • **Phiên bản cấu hình:** 2.1 • **Kết quả:** `PASS_STATIC_CONFIGURATION`.

Đây là rà soát tài liệu/cấu hình và công cụ preflight do Codex thực hiện, không phải kết quả kiểm thử game đã được Antigravity lập trình. Quyền thực hiện và đích bàn giao ở [AUTOPILOT](ANTIGRAVITY_AUTOPILOT.md); prompt công cụ tích hợp ở [ART guide](ART_GENERATION_GUIDE.md).

## 1. Các điểm đã chỉnh sau rà soát

| Vấn đề | Kết quả chỉnh |
|---|---|
| Dừng chờ người dùng/Codex/commit sau mỗi task | Agent tự test/self-review, VERIFIED rồi tiếp tục đến M8; chỉ nghiệm thu người dùng ở bản chơi được cuối |
| Python generator và Pixelorama là luồng tạo hình bắt buộc | generate_image tích hợp tạo hình chính; prompt/reference/raw, hậu xử lý kỹ thuật và tự promote; không chờ duyệt từng PNG |
| Catalog design_only có thể khóa luôn toàn game hoặc bị mở đồng loạt | Raw graph giữ nguyên, readiness/binding/resolver theo ID trong runtime manifest; ngoài allowlist fail-closed |
| Thiếu số liệu thử khiến task OPEN bị treo | Profile có 22 node kế hoạch, hai preset, XP/SP/Ryō, inventory, loot/bo và network defaults; 11 brief giao agent tự đặc tả |
| Hiểu sai UCH_FIRE thành buff sát thương | Giữ giảm chi phí học Hỏa: prototype giảm Ryō cho lần mua sau, không giảm SP/hoàn tiền |
| Bo radius=0 vẫn có thể để tâm map an toàn | Hết phase cuối là không còn vùng an toàn, kể cả đúng tâm; thêm damage ramp và ca test |
| Disconnect có thể bị tự loại hoặc nhận lại cuộn/actor khác | Không timeout tự loại; input dừng, server vẫn chạy; reconnect token gắn đúng actor, hai client có profile riêng |
| Cuộn tồn tại cả inventory lẫn charge riêng | M5 dùng cùng nguồn quantity/transaction, tổng cap hai, không cấp thêm khi tích hợp hoặc rơi lại cuộn đã tiêu |
| Android chưa có thiết bị làm chặn mọi công việc | Tách software/export/device; tiếp tục phần độc lập, NOT_RUN_DEVICE không bị đổi thành mobile PASS |

## 2. Kiểm tra đã chạy

```text
python tools/validate_framework.py --self-test
git diff --check
```

Kết quả: exit code 0 cho cả hai.

- Catalog: 162 node, 29 tree, 12 synergy; ID/ref/AND/OR/DAG/gate/tier cost và raw runtime status được kiểm.
- Profile: 22 ID duy nhất, đóng đủ tiền đề; số SP cấp theo level cộng đúng 12; các luật cố định và bộ số Thế thân/pity người dùng chọn được bảo toàn.
- Hai preset có chi phí cơ sở trước modifier: Hỏa 9 SP/1.850 Ryō; Ảo 8 SP/1.570 Ryō. Đây là đường học có kiểm tiền đề, không phải 9 hoặc 8 nút HUD.
- Lịch bo khởi đầu tổng 23 phút, radius giảm về 0, damage tăng; xác suất/tick rate hợp lệ về cấu trúc, chưa là bằng chứng cân bằng.
- 34 task, không trùng ID hoặc vòng phụ thuộc; Markdown links/code fences và JSON examples hợp lệ.
- Negative fixtures: quá ngân sách SP, thiếu tiền đề trong scope và dependency cycle bị từ chối.

## 3. Phần phải chạy khi Antigravity bắt đầu

Chưa tạo/chạy game, chưa gọi generate_image của Antigravity, chưa chạy Godot/rendered/network/export/Android trong lượt cấu hình này. Những kiểm tra đó là đầu ra bắt buộc của giao việc, ghi lệnh/log/ảnh/video thật trong QA_REPORT khi thực hiện; không suy từ PASS_STATIC_CONFIGURATION thành game PASS.

Đích: có launcher hai client/LAN, bản debug, PLAY_GUIDE và QA_REPORT, người dùng mở chơi thực tế. Chưa nghiệm thu thì không tự ghi ACCEPTED/DONE; nguồn thủ công/owner_locked và luật gameplay CHỐT vẫn được bảo vệ.
