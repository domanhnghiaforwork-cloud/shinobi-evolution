# GAME_DESIGN.md — Shinobi Evolution

**Loại tài liệu:** Gameplay master specification • **Phiên bản:** 2.1 • **Trạng thái:** `OFFICIAL_DESIGN_BASELINE` • **Ngày:** 2026-10-16 • **Chủ quyết định:** Product Owner.

**Baseline chính thức 2.0:** solo hai người/trận, Uchiha + Hỏa, hai hướng Hỏa thuật/Ảo thuật, mục tiêu 20–25 phút. Đây là nguồn luật để giao task theo [TASK_BACKLOG.md](TASK_BACKLOG.md), bắt đầu M0-01. Các luật **CHỐT** phản ánh lựa chọn Product Owner; thông số prototype và chi tiết cần đặc tả trước từng task được theo dõi tại [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md). Các mục mở rộng không thuộc nghiệm thu phiên bản này.

**Cách thực hiện 2.1:** người dùng giao Antigravity tự làm/art/test/sửa đến M8, chỉ nghiệm thu khi chơi được. [AUTOPILOT](ANTIGRAVITY_AUTOPILOT.md) cho phép agent tự đặc tả chi tiết/số liệu thử và tiếp tục task VERIFIED, không dừng xin duyệt từng bước. [Profile khởi đầu](../data/prototypes/solo_first_playable.json) chứa 22 node kế hoạch, hai preset và số thử; không tự bật runtime hoặc đổi luật CHỐT. Art dùng `generate_image` theo [ART guide](ART_GENERATION_GUIDE.md).

> Bản này tổng hợp các quyết định được duyệt và thiết kế kế thừa từ `naruto_gdd_v1.md`. Tên/gameplay dựa trên Naruto là tham khảo nội bộ; dùng IP đó để phát hành cần quyền phù hợp. Luật **CHỐT** có hiệu lực cho baseline; thông số gắn nhãn prototype cần playtest và không là cân bằng cuối.

## 1. Tóm tắt 30 giây

**Shinobi Evolution** là game **PvPvE sinh tồn solo, 2D HD Pixel Art trên điện thoại**, camera **top-down 3/4**. Mỗi người là một phe, loot và di chuyển trên bản đồ, farm quái lấy kinh nghiệm, phát triển build bằng XP/SP/Ryō, tranh tài nguyên và giao tranh dưới áp lực vòng bo. **Người sống sót cuối cùng thắng.** Mỗi người vào trận có một cuộn Thế thân để tàng hình chạy thoát; có thể nhặt thêm cuộn rơi. Solo chết thì bị loại, không hồi sinh.

**CHỐT IDENTITY-01 / MODE-01:** sinh tồn là trọng tâm; cảm hứng MOBA chỉ ở farm quái lấy kinh nghiệm. Ưu tiên thiết kế và kiểm chứng solo nhiều người (mỗi người một phe). Trận offline một nhân vật là công cụ prototype, không phải định nghĩa chế độ solo phát hành. Góc camera 2D đã chọn được giữ nguyên.

**Lời hứa trải nghiệm:** cùng một gia tộc không đồng nghĩa cùng một build; mỗi quyết định farm, giao tranh, loot và lai nhánh làm xuất hiện một con đường phát triển khác nhau nhưng vẫn có cách khắc chế.

### Bốn trụ thiết kế (pillars)

1. **Identity:** xuất thân có bản sắc, có giới hạn hợp lore, nhưng không quyết định 100% lối chơi.
2. **Evolution:** lựa chọn nhẫn thuật trong trận là quyết định chiến lược, không chỉ tăng sát thương.
3. **Survival:** loot công khai, quyết định đường đi, farm có rủi ro, vòng bo và tài nguyên chạy thoát có giới hạn tạo giao tranh tự nhiên.
4. **Readable combat on mobile:** thao tác dễ hiểu, chiêu rõ vùng tác động, hiệu ứng pixel mạnh nhưng màn hình không nhiễu.

### Không phải game này

- Không phải gacha pay-to-win, game thế giới mở vô tận hay MMORPG lưu sức mạnh qua mọi trận.
- Không bắt đầu với tất cả 162 skill hoặc 18 người online cùng lúc ở prototype.
- Không tạo huyết kế chỉ bằng trộn hai nguyên tố; không cấp Thiên Chiếu cho mọi Uchiha.
- **CHỐT OBJECTIVE-01:** bỏ cơ chế chiếm giữ cứ điểm để nhận buff, quyền kiểm soát phong ấn và thắng bằng mục tiêu. Điểm nóng hình thành từ loot, quái/boss và vòng bo. Nhánh kỹ năng Phong ấn vẫn là hệ chiến đấu riêng.

## 2. Trải nghiệm từ sảnh đến kết quả

```text
SẢNH / CREATE NINJA
  chọn gia tộc → ngoại hình → thiên phú chakra → chuyên môn → preset nhánh
      ↓
GHÉP TRẬN / VÀO BẢN ĐỒ
  hai người, mỗi người một phe → chọn vùng → spawn ngẫu nhiên có khoảng cách an toàn
      ↓
ĐẦU TRẬN
  farm XP/Ryō → học T1/T2 → chọn đường đi, thăm dò kẻ địch
      ↓
GIỮA TRẬN
  loot/farm có rủi ro → cuộn + mảnh bí thuật → T3/T4, chiêu lai, giao tranh sinh tồn
      ↓
CUỐI TRẬN
  vòng bo thu hẹp → dùng tài nguyên chạy thoát có giới hạn → người sống sót cuối cùng thắng
      ↓
CHIẾN THẮNG / TỔNG KẾT
  thống kê build, mục tiêu, KDA, nguồn loot → lưu preset/đồ trang trí (không cộng stat vĩnh viễn)
```

### 2.1 Sảnh: quyết định và giới hạn

- **Gia tộc:** bản đầu chỉ bật **Uchiha**; cả hai người được dùng cùng tập nội dung. **SLICE-02/03:** một gia tộc, một hệ chakra **Hỏa**, hai hướng **Hỏa thuật và Ảo thuật**. Hai hướng có thể dùng các nhánh nền tảng/Thể/Ảo thuật cần thiết trong allowlist được đặc tả; không tự bật thêm gia tộc hoặc hệ chakra khác. Danh mục gia tộc còn lại là nguồn mở rộng để sau.
- **Thiên phú chakra — CHỐT NATURE-01:** chọn **1 trong 5 hệ cơ bản** ở sảnh; có thể học hệ thứ hai trong trận theo gate hợp lệ. Hai hệ thông thường; hệ thứ ba chỉ mở qua sự kiện hiếm có điều kiện riêng. Các khóa huyết kế/bí thuật vẫn được kiểm độc lập; cuộn thông thường không tự mở hệ thứ ba. Chi tiết sự kiện và predicate đếm hệ phải được định nghĩa trước khi bật nhánh liên quan.
- **Giới hạn bản đầu:** sảnh chỉ bật Hỏa; hệ thứ hai/thứ ba vẫn ngoài allowlist. NATURE-01 là luật cho khi mở rộng, không tự cho học nature ngoài phạm vi SLICE-03.
- **Chuyên môn ưu tiên:** Thể thuật, Ảo thuật, Y thuật, Phong ấn, Khôi lỗi, Triệu hồi hoặc Biến đổi hình thái (từng đợt cập nhật). Chỉ ảnh hưởng preset/thứ tự dễ học, không cho free skill ultimate.
- **Preset:** đánh dấu 3–6 nút mục tiêu kèm đường đi; là UI gợi ý, **không khóa cứng** hướng chơi. **CHỐT BUILD-02:** giữ các node đã học, không hoàn điểm trong trận; đổi hướng bằng SP còn lại và kỹ năng đã sở hữu. **CHỐT LOADOUT-01:** chỉ thay kỹ năng trang bị khi ngoài giao tranh, ở bất kỳ vị trí nào; cooldown được giữ khi đổi ô.
- **Trang phục / ngoại hình:** mô tả được silhouette 48×64 hoặc 64×64; nhân vật nhỏ vẫn cần nhận diện clan qua VFX/icon khi kích hoạt huyết kế.

### 2.2 Tiến trình trong trận

| Tài nguyên | Nguồn | Cách dùng | Giới hạn |
|---|---|---|---|
| XP | quái/mục tiêu PvE theo quỹ thưởng kết liễu | tăng level đến 20; gate tier | Không rơi khi chết, không chuyển cho người khác |
| Ryō | quái/mục tiêu PvE; nguồn bổ sung chỉ bật khi được duyệt | học skill, nâng skill/đồ, nhẫn cụ | Không rơi khi chết, không chuyển cho người khác |
| SP | cấp và mốc trận | mua nút thuộc đồ thị | Tổng 12 SP mục tiêu cho trận đủ thời lượng |
| Bí quyển/mảnh | elite, boss, sự kiện | thỏa predicate mở nhánh | Không trực tiếp tăng hàng loạt sát thương |
| Chakra | tài nguyên chiến đấu tự hồi/thu hồi | dùng skill, lướt/duy trì nhãn thuật | Cần tài nguyên và counterplay |
| HP | sức sống | bị trừ trong combat, heal có kiểm soát | Không cho chain-heal bất tử |

**CHỐT ECON-02 / REWARD-02 — tiến trình solo:** giữ XP/SP/Ryō; học node cần đủ SP và Ryō như khung hiện tại. Giữ nguyên tắc bên kết liễu nhận quỹ XP/Ryō: trong solo, mỗi phe là một người nên quỹ thuộc người kết liễu. Luật chia đều cho thành viên đủ điều kiện được lưu cho chế độ đội tương lai. Quyền XP/Ryō không tạo quyền độc chiếm vật phẩm rơi hoặc tự quyết quyền tính pity của người khác.

**Chi phí thiết kế tham khảo:** T0 cấp 1 (0 SP, 0 Ryō), T1 cấp 1 (1 SP, 100 Ryō), T2 cấp 4 (1 SP, 180 Ryō), T3 cấp 8 (1 SP, 280 Ryō), T4 cấp 12 (1 SP, 450 Ryō), T5 cấp 17 (1 SP, 700 Ryō). Giá có thể khác tùy nhóm nếu được ghi rõ trong data.

**Tải kỹ năng (target):** 4 active + 1 ultimate + 3 passive + 1 nội tại gia tộc + 1 nhẫn cụ + **Thế thân bị động riêng dùng cuộn**. Thế thân hiển thị số cuộn, không có nút chủ động kích hoạt. Học 12 nút không đồng nghĩa dùng đồng thời tất cả; root, trait và unlock node có thể chỉ là cổng tiến trình.

**Đổi build và trang bị — CHỐT BUILD-03/LOADOUT-01/COMBAT-02:** học node là quyết định giữ lại trong trận, không có thao tác quên node/hoàn SP để mua lại hướng khác. Đổi preset không hoàn tiền hoặc thay tiến trình. Cả học node mới lẫn đổi kỹ năng vào slot chỉ thực hiện khi còn sống và ngoài giao tranh, ở bất kỳ vị trí nào; không cần tới điểm huấn luyện. Thoát giao tranh sau **5 giây liên tục không gây/nhận sát thương và không dùng đòn hoặc kỹ năng tấn công**, áp dụng cả PvP và PvE. Đang giao tranh được xem cây nhưng chưa mua; mở cây không tạm dừng trận. Thay slot không reset cooldown. Chi tiết timer và kiểm tại thời điểm giao dịch theo `SKILL_SYSTEM.md` §10.1; vòng đời buff/summon khi tháo cần đặc tả trước handler liên quan.

## 3. Vòng lặp trận mục tiêu và phase

**Cấu hình hiện tại — CHỐT MATCH-02/03/04:** solo **hai người mỗi trận**; người chơi chọn vùng xuất phát rồi hệ thống chọn ngẫu nhiên vị trí hợp lệ trong vùng, bảo đảm khoảng cách an toàn giữa hai người. Thời lượng mục tiêu **20–25 phút**, không phải giới hạn cứng; trận kết thúc khi xác định người sống sót cuối cùng. Cấp 20 và ngân sách 12 SP là mục tiêu tiến trình cần kiểm chứng trong nhịp mới. Prototype **một nhân vật offline → hai client → hoàn thiện vòng chơi hai người**. Tăng số người và cấu hình đội cũ để sau, không nằm trên đường nghiệm thu hiện tại.

| Giai đoạn tham chiếu | Trải nghiệm chính | Hành vi mong muốn | Điều khiến người chơi gặp nhau |
|---|---|---|---|
| Đầu trận | định hình cơ bản | farm, di chuyển, T1/T2, chọn đường | trại quái và tuyến di chuyển |
| Giữa trận | tăng tốc và đổi hướng build | elite, cuộn, T3/T4 trong tập nội dung được bật | tài nguyên hiếm, boss và vòng bo |
| Cuối trận | quyết chiến sinh tồn | giữ lợi thế, tiêu tài nguyên thoát hiểm, loại đối thủ | vòng bo thu hẹp và sát thương ngoài vùng |

Cấp và thời gian là mục tiêu cho người chơi hoạt động bình thường, **không tự tăng level theo đồng hồ**. Người đang yếu cần có tuyến loot/farm khả thi để cải thiện build; tiến trình phải được đo cùng rủi ro lộ vị trí, vòng bo và mất mạng. Lịch từng phase và XP/Ryō phải được thử cho hai người/20–25 phút; bảng trên không tự mở T5 hoặc cấp chiêu theo phút.

### 3.1 Bản đồ mục tiêu

- Một map liền mạch có nhiều đường đi, khu loot, trại quái và vật cản hỗ trợ trốn/né/tiếp cận. **MATCH-03:** chọn vùng xuất phát trước trận, spawn ngẫu nhiên trong vùng với khoảng cách an toàn giữa hai người. Cần cấu hình khoảng cách, vùng hợp lệ và xử lý hai người cùng chọn một vùng trước task match; không ràng buộc sáu khu xuất phát theo cấu hình đội cũ.
- Biome: rừng tre/ninja, đầm sương, đồi đá/công sự, tàn tích/phong ấn, sông, boss arena. **Địa hình phải hỗ trợ nhẫn thuật**: đường hẹp cho Thổ, vùng ướt cho Lôi, sương cho trinh sát/Ảo thuật.
- **CHỐT OBJECTIVE-01:** không có phong ấn A/B/C hoặc cứ điểm chiếm giữ để cấp buff trong phạm vi chính. Hạch Trận và mảnh phong ấn kiểm soát bản đồ được bỏ khỏi vòng chơi hiện hành. Mảnh bí thuật mở skill và nhánh kỹ năng Phong ấn vẫn giữ vai trò riêng.
- **Boss/loot hiếm:** là nguồn tài nguyên có rủi ro, không tạo chiến thắng trực tiếp. Cảnh báo boss công khai ít nhất 3 phút vẫn là mục tiêu thử đang có; tần suất và cách lộ thông tin cần phù hợp nhịp solo.
- Không bắt đầu làm 3D traversal thực: góc nhìn **2D top-down 3/4**; chạy trên tường là cơ chế zone/animation giả lập có giới hạn nếu triển khai, không tạo parkour nhiều tầng cao.

### 3.2 Điều kiện thắng — CHỐT solo

1. **MODE-01:** mỗi người là một phe; người sống sót cuối cùng thắng.
2. **SOLO-LIFE-01:** solo chết hẳn thì bị loại, không hồi sinh. Không có cứu đồng đội, trụ hồi sinh hoặc lượt trở lại trong mode này.
3. Nhân vật bị loại không tiếp tục gây sát thương hoặc thắng thay chủ qua thực thể triệu hồi. Chi tiết cleanup effect/projectile phải được đặc tả theo ability.
4. **ZONE-01 / MATCH-04:** vùng an toàn thu hẹp dần, bên ngoài gây sát thương. 20–25 phút là mục tiêu cân chỉnh, không xét điểm hoặc tự kết thúc theo đồng hồ.
5. **OBJECTIVE-01:** không có thắng bằng chiếm giữ cứ điểm, phong ấn hoặc Hạch Trận.
6. **MATCH-05:** nếu sau khi xử lý toàn bộ sát thương và Thế thân hợp lệ trong cùng một tick authority, cả hai đều chết thì **hòa trận**. Không chọn người thắng theo ID, thứ tự loop, thứ tự nhận gói hoặc tổng sát thương. Chỉ xét người sống sót sau khi kết thúc xử lý tick, không phát thắng ngay tại sự kiện chết đầu tiên.

7. **MATCH-06 — mất kết nối:** nhân vật đứng yên/không nhận input mới nhưng vẫn ở trận, nhận sát thương và có thể bị bo hoặc đối thủ loại. Không có timeout tự loại vì disconnect. HP, cuộn Thế thân, cooldown, DOT và vòng bo tiếp tục theo authority; bị động Thế thân vẫn tự xét nếu đủ điều kiện. Kết nối lại tiếp tục cùng actor/state, không spawn mới hoặc nhận lại tài nguyên đầu trận. Mất kết nối không tạo pause hay miễn sát thương; actor vẫn tính là người còn sống đến khi thực sự bị loại.

**Cần đặc tả tiếp:** thứ tự xác định event hợp lệ trong tick và cấu hình phase vòng bo cuối. Kết quả cả hai chết cùng tick đã chốt hòa theo MATCH-05; disconnect theo MATCH-06. Cơ chế đội cũ được tách tại §3.5, không áp cho solo.

### 3.3 Một mạng và cuộn Thế thân bị động — CHỐT solo

- **SOLO-LIFE-01:** không hồi sinh trong solo. Cuộn Thế thân là cơ chế chạy thoát khi còn trong trận, không phải vật phẩm hồi sinh sau khi chết.
- **SOLO-SUB-01:** mỗi người vào trận có **một cuộn Thế thân**; cuộn cũng có thể rơi để nhặt thêm. Công dụng đã chốt là tàng hình để chạy thoát.
- **SOLO-SUB-02:** Thế thân là bị động tự dùng một cuộn khi sát thương sắp làm HP về 0 hoặc thấp hơn; kích hoạt trước khi chuyển sang trạng thái chết. Đây là ngưỡng gây chết, không phải đòn critical hit nhân sát thương. Người chơi không bấm nút để kích hoạt.
- **SOLO-SUB-03 / SOLO-SUB-09:** khi kích hoạt, ngăn lần chuyển sang chết, **đặt HP về 25% HP tối đa hiện tại**, tàng hình tối đa **3 giây**, cooldown nội tại **60 giây** tính từ kích hoạt. Bộ số 25%/3s/60s được duyệt cho lần thử đầu tiên, cần đo và điều chỉnh sau playtest; không phải cân bằng phát hành. Đây là đặt HP sau kích hoạt, không cộng thêm 25% vào HP trước hit.
- **SOLO-SUB-04:** sát thương gây chết từ vòng bo cũng kích hoạt cuộn, nếu bị động đủ điều kiện về số cuộn và hồi chiêu.
- **SOLO-SUB-05:** mang tối đa **hai cuộn**; chỉ cấp một cuộn lúc vào trận, cuộn thứ hai phải nhặt được. Đầy hai cuộn thì không nhận thêm; pickup không được làm mất cuộn rơi khi chưa chuyển thành công vào inventory.
- **SOLO-SUB-06:** có **hồi chiêu nội tại** bắt đầu khi kích hoạt. Trong hồi chiêu, sát thương gây chết vẫn giết được người chơi dù còn cuộn; không tiêu cuộn dự phòng để kích hoạt trái cooldown. Nhặt cuộn khác không reset hồi chiêu. Cấu hình thử 60 giây theo SOLO-SUB-09.
- **SOLO-SUB-07:** tàng hình vẫn chịu sát thương; gây hoặc nhận sát thương sau khi đã kích hoạt sẽ làm lộ thân. Lộ thân không xóa hồi chiêu. Vòng bo tiếp tục gây sát thương và có thể làm lộ/giết trong hồi chiêu.
- **SOLO-SUB-08:** khi kích hoạt, xóa khống chế và toàn bộ hiệu ứng bất lợi đang có, kể cả DOT. Đây là một lần thanh tẩy, không cấp miễn nhiễm; hit hoặc nguồn hiệu ứng mới ngay sau đó vẫn có thể gây CC/DOT/reveal bình thường. Vòng bo là nguồn sát thương môi trường tiếp tục hoạt động, không bị xóa khỏi trận.
- Đòn gây chết đã được bị động chặn không được xử lý lại như một hit mới phá tàng hình của chính lần kích hoạt. Các hit hợp lệ khác, kể cả đến cùng tick, được xét tiếp với HP vừa hồi và cooldown đã bắt đầu; không có miễn sát thương ngầm.
- Hiệu ứng bất lợi thuộc chính đòn kích hoạt phải được giải quyết trong cùng giao dịch và không áp lại sau bước thanh tẩy. Hit khác vẫn áp dụng theo thứ tự authority. Cần đặc tả phân loại effect, damage sau shield và reveal mới theo hợp đồng combat; không cấp thêm Thế thân chủ động miễn phí song song với cơ chế cuộn.
- Cuộn rơi bổ sung dùng loot table do authority quyết định; tỷ lệ và nguồn rơi cụ thể cần cấu hình được duyệt. Không tự đưa cuộn vào nhóm pity bí thuật.
- **LOOT-04:** khi chết hẳn/bị loại, rơi toàn bộ vật tư đang mang, kể cả cuộn Thế thân chưa dùng, thành loot công khai. Chỉ item đang nằm trong inventory được chuyển; không làm rơi hoặc sao chép node đã học, XP, SP hay Ryō. Các tài nguyên tiến trình kết thúc cùng trận, không chuyển sang người khác hoặc tự mang sang trận mới. Chết/retry event chỉ tạo một lượt chuyển vật tư; Thế thân kích hoạt thành công chưa phải chết nên không rơi đồ.

### 3.4 Vùng an toàn và vòng bo — CHỐT cơ chế

- Vùng an toàn thu hẹp dần theo giai đoạn; nhân vật bên ngoài nhận sát thương do authority xử lý. Telegraph và minimap hiển thị biên hiện tại cùng thông tin phase cần thiết.
- Cấu hình thử phải xác định lịch thu, kích thước/tâm vùng, khoảng báo trước, nhịp sát thương và tương tác với HP/chakra/hồi phục/miễn nhiễm. Không tự suy ra công thức damage từ mục tiêu 20–25 phút.
- **ZONE-02 — CHỐT:** bo cuối tiếp tục thu đến **không còn vùng an toàn**; sát thương bo tăng theo cấu hình để buộc kết thúc bằng sống sót. Không giữ một vùng an toàn vĩnh viễn. Cấu hình phải có sức ép tăng đủ để không thể duy trì hồi phục/miễn nhiễm/Thế thân vô hạn; Thế thân vẫn xét theo luật đã chốt, không bị tắt ở bo cuối. Nếu cả hai chết cùng tick thì hòa theo MATCH-05.
- Các giai đoạn trong bảng §3 là tham chiếu nhịp chơi; sự kiện boss cần đồng bộ với cấu hình phase đã duyệt. Solo không có mốc khóa hồi sinh vì không có hồi sinh ngay từ đầu.

### 3.5 Chế độ đội — lưu tham chiếu, phát triển sau

Các lựa chọn trước khi chuyển ưu tiên sang solo: đội cuối cùng sống sót thắng; cứu đồng đội/mục tiêu hồi sinh, không tự hồi sinh căn cứ; cả ba chết hẳn thì loại đội; đội kết liễu nhận quỹ XP/Ryō chia đều cho thành viên đủ điều kiện. Ý tưởng trụ hồi sinh được lưu cho mode đội nếu sau này mở phạm vi. Không đưa các hệ này vào task solo.

Quyết định chiếm phong ấn/giữ cứ điểm để nhận buff đã bị thay thế bởi OBJECTIVE-01, không tự khôi phục khi làm mode đội. Thông số 18 người / 6 đội × 3 là tham chiếu cũ, không xác lập số người cho solo.

## 4. PvE, loot và ngẫu nhiên có kiểm soát

| Mục tiêu | Phần thưởng | Quy tắc xuất hiện |
|---|---|---|
| Quái thường | XP, Ryō, nguyên liệu cơ bản | nhiều điểm spawn, có tái sinh |
| Elite | mảnh nhánh hoặc quyền chọn giữa 2–3 nhóm | nguy hiểm vừa, có cạnh tranh |
| Boss vùng | khế ước, ấn lĩnh ngộ, tư liệu T3/T4 | thông báo khu vực / nhiều đường vào |
| Boss thế giới | lõi tiên thuật, chìa thức tỉnh, tài nguyên T5 | công bố toàn map, giới hạn sự kiện |
| Sự kiện tranh chấp | bí quyển đặc thù/đồ dùng chiến thuật | giao tranh chủ động, không độc quyền vô hạn |

**CHỐT LOOT-02 — vật phẩm hiếm công khai:** cuộn hoặc mảnh bí thuật hiếm từ elite/boss rơi ra đất, người chơi khác có thể tranh nhặt. Người kết liễu không độc quyền vật phẩm rơi. Authority xác nhận pickup và chỉ chuyển vật phẩm cho một người thắng giao dịch; nhặt được vật phẩm vẫn phải kiểm gate khi học/sử dụng.

**CHỐT PITY-02/PITY-03/LOOT-03:** khi tham gia hợp lệ vào mục tiêu nhưng không nhận được mảnh mục tiêu, kể cả bị người khác nhặt mất, tính một lượt trượt pity cá nhân. Nếu lượt thứ tư liên tiếp cũng trượt thì chọn một mảnh phù hợp ngay trong reward thứ tư; mảnh chọn **vào thẳng túi người có quyền chọn, không bị cướp**. Quyền pity được xét riêng với quỹ XP/Ryō của người kết liễu.

**PITY-04 — điều kiện tham gia thử:** gây sát thương thực tế cộng dồn ít nhất **5% HP tối đa mục tiêu** trong **30 giây trước khi mục tiêu bị hạ**, đồng thời còn sống và ở trong vùng tham gia lúc đó. Authority chụp quyền tham gia tại lúc chết của mục tiêu, không kiểm lại vị trí sau khi loot được tranh nhặt; cần cấu hình bán kính vùng và HP tham chiếu cho mục tiêu trong task loot.

**PITY-05 — chốt lượt:** chờ đến khi **toàn bộ mảnh hiếm thuộc lượt rơi đó đã được nhặt hoặc hết hạn trên đất**, rồi chốt một lần. Không tự chốt theo đồng hồ 30 giây sau chết; 30 giây ở PITY-04 là cửa sổ đóng góp. Lượt không rơi mảnh hiếm nào có tập loot chờ rỗng, chốt ngay; lượt thứ tư vẫn chọn trong chính reward thứ tư khi nó hoàn tất. Phải có thời hạn world loot hữu hạn và thứ tự settle các lượt cùng nhóm; không tự gán tỷ lệ rơi, prototype có thể dùng deterministic test drop.

**PITY-06 — reset:** counter riêng từng nhóm loot trong trận. Nhận mảnh mục tiêu hoặc nhận phần bảo hiểm thì về 0; đổi mục tiêu trong cùng nhóm cũng về 0, không chuyển bộ đếm sang nhóm khác. Mục tiêu được chọn trước lượt đánh và lưu theo reward event; đổi sau không sửa kết quả cũ hoặc chuyển miss cũ sang mục tiêu mới.

**LOOT-05 — túi giới hạn và pity chờ nhận:** cuộn/mảnh mở kỹ năng chung túi giới hạn ô với vật tư sinh tồn; không có ngăn tư liệu vô hạn. Nếu túi đầy, phần pity giữ thành quyền nhận riêng, không bị cướp, không tự đẩy ra đất hoặc xóa đồ trong túi. Khi có chỗ và người chơi còn sống, nhận vào túi bằng giao dịch một lần; không nhân thêm quyền cho cùng chuỗi trượt trong lúc chờ. Số ô/stack là cấu hình cần chốt trước M5. Bảo vệ khỏi tranh cướp áp dụng lúc trao/chờ nhận; item đã vào túi vẫn rơi khi chết theo LOOT-04. Người bị loại không nhận thêm vật tư để dùng trong trận; quyền chờ chưa giao không là item đang mang, không chuyển qua trận mới.

**Nguyên tắc:** vật phẩm hiếm **mở lựa chọn**, không tự cấp huyết kế trái lore hoặc tặng sát thương áp đảo. Nếu người chơi không gặp vật phẩm, luôn có ít nhất một nhánh T4 không phụ thuộc drop cho build có thể chơi tốt. Sự kiện world boss không drop trực tiếp kỹ năng tối thượng cho client.

## 5. Chiến đấu & đối trọng

- Điều khiển mục tiêu **2 ngón**: joystick ảo bên trái; đánh cơ bản + 4 skill + ultimate + nhẫn cụ bên phải. Thế thân bị động có chỉ báo số cuộn/trạng thái, không có nút kích hoạt. Nút bấm không trùm vùng quan sát quan trọng; hỗ trợ tay trái/tay phải sau.
- **Targeting:** skill định hướng bằng kéo/thả (aim vector), skill khóa mục tiêu chỉ khi có tiêu chí rõ và có chỉ báo; không để auto-aim thay thế mọi kỹ năng đòi hỏi kỹ năng cá nhân.
- **Nhịp:** di chuyển phản ứng nhanh, cooldown ngắn cho cơ bản, đòn lớn có startup/telegraph/cost; giữ skill ceiling từ căn hướng và timing.
- **Chakra:** chi phí dùng và duy trì kỹ năng; khi cạn vẫn có nhẫn cụ/đòn thường; không ép đứng im hồi quá lâu.
- **CC:** giảm hiệu quả khi trói/stun liên tiếp (diminishing returns), tránh chuỗi khóa nhân vật không thể thao tác. Thế thân bị động bảo vệ ở ngưỡng gây chết khi đủ cuộn/cooldown; kích hoạt xóa CC và hiệu ứng bất lợi đang có, không miễn hiệu ứng mới. Cooldown thử 60 giây theo SOLO-SUB-09.
- **Counterplay:** nước dẫn điện; Hỏa/Phong khuếch đại vùng lửa nhưng phải có dấu cảnh báo; Thổ che đường; Huyết kế/ultimate mạnh tốn chakra, có thời gian chuẩn bị, cách phá hoặc tránh.
- **PvP fairness:** server là authority về vị trí hợp lệ, hit, item, unlock, số tiền và tỷ lệ rơi; client chỉ gửi thao tác. Người bị lag không được tự xác nhận hit.

### 5.1 Chỉ số đầu ra cần ghi để cân bằng (chưa có số chốt)

Từng skill chiến đấu cần `startup_ms`, `active_ms`, `recovery_ms`, `damage/heal`, `range`, `radius`, `chakra_cost`, `cooldown`, `cc_duration`, `counter_tags`, `hit_shape`, `network_prediction_class`. Chỉ số không có trong catalog hiện tại → **chưa đủ code combat**.

## 6. Nhẫn thuật, gia tộc, mở nhánh

**Loại thuật:** Nhẫn thuật, Thể thuật, Ảo thuật, Y thuật, Phong ấn, Triệu hồi, Khôi lỗi, nhãn thuật, Tiên thuật. **Phân loại chồng nhau** chứ không phải 9 tier. Chakra gồm Hỏa/Phong/Lôi/Thổ/Thủy. Rank E–S là độ khó trong lore, **khác** tier T0–T5 gameplay.

**Gia tộc nguồn:**

| Gia tộc | Đặc trưng build | Điểm yếu buộc phải có |
|---|---|---|
| Uchiha | Sharingan, phản công/ảo thuật, Hỏa/Lôi lai | hao chakra, AoE/che tầm nhìn |
| Hyūga | Byakugan, Nhu Quyền, áp sát khóa chakra | thua cấu rỉa, góc mù / địa hình |
| Nara | trói bóng, định vị, phong ấn lai | thiếu burst, dễ bị áp sát |
| Yamanaka | nhập tâm, đánh dấu, phối hợp | thân gốc nguy hiểm khi dùng thuật |
| Akimichi | bội hóa, tank, áp lực vùng | bị thả diều/khống chế |
| Aburame | côn trùng, trinh sát, hút chakra | AoE, mất bầy |
| Inuzuka | nhẫn khuyển, đuổi bắt, tốc độ | phải áp sát, dễ tách đồng đội thú |
| Uzumaki | sinh lực, phong ấn, kết giới | startup cao, cơ động thấp |
| Yuki | Băng Độn, zone-control, ảo thuật lai | tốn chakra, phá được kết giới |
| Hōzuki | hóa lỏng, né/di chuyển nước | yếu trước Lôi và phong ấn |

**Huyết kế (Kekkei Genkai)** là quyền huyết thống/sự kiện đặc thù; **Hiden** là bí thuật truyền dạy có điều kiện clan/mentor. Không cho học Sharingan qua cuộn rơi; không cho nguyên tố tự tạo Mộc/Băng. **Mở nhánh ngẫu nhiên** không làm mất điều kiện nguồn.

**Lai ba kiểu:** (A) phản ứng môi trường không cần mua nút mới; (B) skill lai cần hai tiền đề + SP/Ryō và chiếm ô; (C) huyết kế/đặc biệt cần khóa riêng, không phát sinh tự động. Quy tắc và 162 nút chi tiết: `SKILL_SYSTEM.md`; ID và tiên quyết: `data/skills/skills.json`.

## 7. Art direction — CHỐT CHO PROTOTYPE

### 7.1 Phong cách

- **2D HD Pixel Art**: gợi cảm hứng nhịp combat **Wizard of Legend**, địa hình pixel có chiều sâu, silhouette sắc nét; không lấy/copy sprite/âm thanh/texture từ game khác.
- **Camera top-down 3/4 MOBA** với nhân vật 2D nhìn chếch xuống; không phải 2D side-scroller, không phải camera sau lưng 3D, cũng chưa cần isometric toán học 2:1.
- **Palette:** nền có saturation vừa/thấp; VFX chakra giàu màu nhưng giới hạn glow/bloom, giúp nhìn rõ vùng đe dọa.
- **Silhouette:** ưu tiên tóc, băng trán, vũ khí, màu y phục; logo/icon huyết kế nổi khi kích hoạt vì mắt pixel rất nhỏ.
- **Tầng hình ảnh:** ground tiles → props thấp → character Y-sort theo chân → props che khuất có fade → VFX combat → telegraph → UI.

### 7.2 Target asset/spec khởi đầu

| Thành phần | Mức thử nghiệm | Quy tắc |
|---|---|---|
| Sprite nhân vật | 48×64 hoặc 64×64 px | một chuẩn thống nhất sau test; 4 hướng prototype, nâng 8 hướng |
| World tile | 32×32 px | góc top-down 3/4, không trộn perspective vô thức |
| Reference world | 640×360 logical px | pixel-perfect upscale thử nghiệm, kiểm viewport thật |
| Màn hình | landscape Android | UI an toàn cho 16:9 đến 20:9, notch/safe-area |
| Texture | nearest với sprite/tiles | font/UI có thể render ở lớp sắc nét riêng |
| Animation | idle, run, attack, hurt, dodge, cast, death | ưu tiên anticipation/recovery đọc được |
| Effects | sprite sheet pixel + particles vừa phải | 3 cấp quality, hạn chế overdraw |

**Không bắt buộc 640×360 pixel ở mọi điện thoại.** Chọn world reference và UI responsive riêng; không để hai vùng điều khiển chiếm hết diện tích xem giao tranh. Zoom/scale phải được test trên điện thoại tỉ lệ rộng và nhỏ.

### 7.3 Visual gameplay / sức mạnh tiến hóa

- T1 Hỏa Cầu = đạn lửa đơn, đọc hướng rõ; T3 Hỏa Liên = nhiều đạn; T5 Hỏa Vực = sân cháy + telegraph. Các tên biến thể có thể là **game design**, không phải nâng cấp canon.
- Sharingan kích hoạt = vòng mắt/icon + nhịp telegraph, không dựa vào việc pixel mắt có nhìn thấy hay không.
- Trói bóng = vệt bóng trên đất phân biệt với bóng môi trường; Hỏa = cảnh báo rìa đỏ/cam; Thủy+Lôi = vùng ướt + điện nhấp nháy khác biệt.
- Ultimate có hiệu ứng đặc trưng nhưng **không khóa camera gây bất lợi trong PvP**; ưu tiên telegraph/cách né trước spectacle.
- VFX của đồng đội/đối thủ có thể tự giảm khi giao tranh đông; vùng damage authoritative không phụ thuộc particle.

### 7.4 Âm thanh và cảm nhận

- Hành động cần tín hiệu âm thanh khác nhau giữa cast, hit, parry, bị CC, kích hoạt huyết kế, nhận loot.
- Có tùy chọn giảm camera shake, flash, particle density; nút rung/âm thanh mobile có thể tắt.
- Tránh âm nhạc/voice chính thức Naruto khi không có phép.

## 8. UX / màn hình tối thiểu

1. **Title → Lobby:** chọn gia tộc, chakra, chuyên môn, preset + xem bản đồ chiến trường.
2. **Match HUD:** HP/Chakra, level, Ryō, 4 active + ultimate + nhẫn cụ, chỉ báo cuộn Thế thân bị động, joystick, minimap và cảnh báo vòng bo/boss.
3. **Skill Graph:** lọc gia tộc/nguyên tố/chuyên môn/tier; node chưa đủ điều kiện hiện **lý do khóa**, nguồn tư liệu, nhánh thay thế; hỗ trợ chạm, phóng to/thu nhỏ, không cần hover.
4. **Loot:** thông báo nhận cuộn, lựa chọn mảnh hiếm không che tình huống chiến đấu; ưu tiên UI sau khi an toàn.
5. **Result:** thời gian sống, kill/assist, mục tiêu, build đã học, nhánh lai, biểu đồ thời gian mở T3/T4.
6. **Settings:** tùy chọn vị trí/độ lớn nút, chất lượng hiệu ứng, rung, camera shake, âm lượng, ngôn ngữ.

### Điều cần test usability

- Đọc tên skill và nút trên điện thoại nhỏ; nhận biết enemy skill 1 giây trước va chạm; không bấm nhầm skill với joystick; không có layout che minimap vì notch.

## 9. Chống snowball, trả tiền và trải nghiệm dài hạn

- **Không bán sức mạnh trong trận**; tiền thật chỉ trang phục, biểu cảm, tiện ích phi chiến đấu nếu kinh doanh sau.
- Meta progression: lưu preset, mở ngoại hình, tutorial clan, thống kê cá nhân; **tránh tăng stats vĩnh viễn làm lệch PvP**.
- Hệ thống anti-RNG frustration: pity + vật phẩm chọn nhóm + mỗi build luôn có đường chơi không yêu cầu boss hiếm.
- Có tutorial di chuyển/nhẫn thuật/loot cho người mới, có bot PvE luyện tập trước khi chơi online.
- Dùng tên game, art/lore gốc nếu không có giấy phép Naruto.

## 10. Mục tiêu đo đạc và ngưỡng điều chỉnh (proposal)

| Metric | Vì sao đo | Ngưỡng hành động thử nghiệm |
|---|---|---|
| Time to first meaningful branch | tránh farm nhàm | người mới nhìn thấy lựa chọn T2 trong vài phút đầu |
| Time to T3/T4 | kiểm nhịp tiến hóa | xảy ra xung quanh phase tương ứng, không bế tắc do RNG |
| Variety of viable builds | game có tính chọn lựa | mỗi gia tộc slice ≥2 hướng có counterplay rõ |
| Win rate by clan/build | phát hiện OP | điều tra chênh lệch lớn sau đủ mẫu; không khẳng định tỷ lệ 50% luôn |
| Death / combat duration | tránh one-shot vô nghĩa | người chơi có cửa sổ đọc và phản ứng với đòn lớn |
| FPS / frame time | khả thi mobile | kiểm ở teamfight nhiều VFX trên máy mục tiêu |
| Disconnect/rejoin | công bằng online | ghi % reconnect thành công khi networking có thật |
| Pity activation rate | điều chỉnh loot | nếu quá nhiều người chạm pity, RNG chưa đáp ứng mục tiêu |

Các ngưỡng số thống kê cụ thể chưa thể chốt trước khi có prototype và nhóm người chơi mẫu.

## 11. Kế hoạch nội dung (scope)

- **Prototype 0:** offline single player, placeholder sprite, joystick/keyboard, một map, quái đơn, HP/Chakra, 1–3 skill, một loot loại cố định.
- **Phạm vi hiện tại — CHỐT SLICE-02/03:** vòng solo hai người hoàn chỉnh, mục tiêu 20–25 phút; **Uchiha + Hỏa**, hai hướng Hỏa thuật/Ảo thuật, farm/loot/boss/vòng bo/Thế thân/kết quả. Tập node/ability cụ thể, tiền đề và stat thử lập trong brief M3/M4, không tự bật toàn bộ cây Uchiha hoặc T5 chỉ vì clan đã được chọn.
- **Mở rộng slice — đề xuất:** Uchiha/Hyūga/Nara, Hỏa/Lôi/Thổ, 24–36 nút thật và 2 combo; chỉ thêm khi vòng chơi nhỏ đã được kiểm chứng và duyệt mở rộng. Không là điều kiện để thử hai người.
- **Alpha/Beta mở rộng — DEFERRED:** thêm clan, hệ, node và tăng số người khi có yêu cầu mới cùng benchmark. Catalog 162 node là kho thiết kế; không bắt triển khai hết để nghiệm thu phạm vi hai người.

Xem tiêu chí nghiệm thu theo cổng: `DEVELOPMENT_ROADMAP.md`.

## 12. Rủi ro / quyết định chưa chốt

| ID | Nội dung | Mặc định đến khi playtest |
|---|---|---|
| GD-01 | Chế độ chính | CHỐT solo; đội là hướng phát triển sau |
| GD-02 | Quy mô và thời lượng solo | CHỐT hai người/trận, mục tiêu 20–25 phút, chọn vùng rồi spawn ngẫu nhiên an toàn; còn cấu hình map/phase để kiểm chứng |
| GD-03 | Tốc độ trận/độ dày boss/loot? | chỉ giả thuyết, phải đo |
| GD-04 | Joystick, aim assist và camera zoom | test theo thiết bị Android thật |
| GD-05 | Chết và kết thúc trận solo | CHỐT không hồi sinh, hòa cùng tick, disconnect không tự loại; Thế thân thử 25%/3s/60s, thanh tẩy; kiểm thứ tự event/cleanup theo handler |
| GD-06 | Tên/thuật bản quyền Naruto | dùng nội bộ; thương mại phải làm rõ quyền |
| GD-07 | Hệ thứ ba & cách lai skill/element | đã chốt hai hệ thông thường, hệ thứ ba qua sự kiện hiếm; còn predicate sự kiện và hợp đồng synergy |

## 13. Quy tắc chấp nhận chỉnh sửa Game Design

Thay đổi về số player, duration, economy, clan restriction, cách thắng, revive và target platform chỉ được đưa vào **CHỐT** khi Product Owner duyệt. Agent cập nhật bảng/Change Log và những file liên quan. **Không tự nâng trạng thái ý tưởng lên tính năng đã code**.

### Change Log

| Ngày | Phiên bản | Thay đổi |
|---|---|---|
| 2026-10-16 | 1.0 | Tổng hợp vòng chơi Naruto-inspired, đổi art direction sang mobile 2D HD Pixel Art, xác định scope prototype và trách nhiệm AI |
| 2026-10-16 | 1.1 | Theo lựa chọn Product Owner: đội sống sót cuối cùng thắng; phong ấn thuộc đội và có thể bị chiếm lại; chỉ đồng đội cứu hoặc mục tiêu hồi sinh, bỏ tự hồi sinh căn cứ; mục tiêu bàn giao là đặc tả chính thức để code |
| 2026-10-16 | 1.2 | Theo lựa chọn Product Owner: vòng bo thu hẹp/sát thương ngoài vùng, 42 phút là mục tiêu; phong ấn cho buff/kiểm soát bản đồ, hồi sinh qua mục tiêu riêng; cả đội chết hẳn bị loại ngay |
| 2026-10-16 | 1.3 | Theo lựa chọn Product Owner: giữ node đã học/không hoàn điểm trong trận, hai hệ thường và hệ thứ ba qua sự kiện hiếm; đổi kỹ năng ngoài giao tranh ở mọi vị trí, giữ cooldown |
| 2026-10-16 | 1.4 | Theo lựa chọn Product Owner: chia đều XP/Ryō trong nhóm đồng đội đủ điều kiện, cuộn/mảnh hiếm rơi công khai mọi đội tranh nhặt, pity cho chọn ngay tại lượt trượt thứ tư |
| 2026-10-16 | 1.5 | Ưu tiên solo sinh tồn, bỏ cứ điểm buff; solo không hồi sinh, khởi đầu một cuộn Thế thân tàng hình và có rơi thêm; giữ XP/SP/Ryō; chốt pity theo tham gia, mảnh bảo hiểm vào túi và quỹ XP/Ryō theo bên kết liễu; tách luật đội làm tham chiếu |
| 2026-10-16 | 1.6 | Chốt tối đa hai cuộn Thế thân, hồi chiêu nội tại và sát thương sau kích hoạt làm lộ tàng hình; không miễn damage hoặc tự dùng cuộn dự phòng trong cooldown |
| 2026-10-16 | 1.7 | Chốt phạm vi hai người/trận, chọn vùng rồi spawn ngẫu nhiên an toàn và mục tiêu 20–25 phút; bỏ lịch phase 42 phút khỏi luật hiện hành, tách mở rộng content/số người khỏi nghiệm thu hiện tại |
| 2026-10-16 | 1.8 | Chốt LOOT-04 rơi toàn bộ vật tư nhưng không XP/SP/Ryō; SOLO-SUB-08 thanh tẩy khi kích hoạt; BUILD-03 chỉ học ngoài giao tranh, được xem cây khi combat |
| 2026-10-16 | 1.9 | Chốt COMBAT-02 thoát giao tranh 5s, SOLO-SUB-09 cấu hình thử 25%/3s/60s, MATCH-05 hòa cùng tick; PITY-04 ngưỡng thử 5%/30s và PITY-05 chốt khi loot nhặt/hết hạn; MATCH-06 disconnect đứng yên, không tự loại |
| 2026-10-16 | 2.0 | Baseline chính thức cho hai người: SLICE-02/03 Uchiha + Hỏa/hai hướng build, ZONE-02 bo hết vùng an toàn, PITY-06 reset theo nhóm và LOOT-05 túi chung giới hạn/pity chờ riêng; các hướng mở rộng để sau |
| 2026-10-16 | 2.1 | Giữ luật gameplay 2.0; ủy quyền Antigravity tự đặc tả/triển khai/test/sửa đến M8, dùng generate_image, profile thử và nghiệm thu người dùng ở bản chơi được cuối |
