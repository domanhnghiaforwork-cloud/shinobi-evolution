# GAME_DESIGN.md — Shinobi Evolution

**Loại tài liệu:** Gameplay master specification • **Trạng thái:** `DRAFT_FOR_PROTOTYPE` • **Ngày:** 2026-10-16 • **Chủ quyết định:** Product Owner.

> Bản này tổng hợp ý tưởng trong cuộc trao đổi và `naruto_gdd_v1.md`. Tên/gameplay dựa trên Naruto là tham khảo thiết kế nội bộ; dùng IP đó để phát hành cần quyền phù hợp. Các con số game là **giả thuyết cần playtest**, không phải cân bằng cuối.

## 1. Tóm tắt 30 giây

**Shinobi Evolution** là game **2D HD Pixel Art trên điện thoại**, camera **MOBA top-down 3/4**, lai **survival + PvPvE + MOBA + RPG phát triển build ngay trong trận**. Người chơi tạo ninja ở sảnh, chọn gia tộc/thiên phú/chuyên môn và một **preset lộ trình không ép buộc**; vào bản đồ lớn, đánh quái để nhận XP và Ryō, săn bí quyển mở những nhánh hiếm, nâng đồ thị nhẫn thuật có nhiều ngả, tranh tài nguyên với người khác và chiến thắng bằng mục tiêu hoặc giao tranh cuối trận.

**Lời hứa trải nghiệm:** cùng một gia tộc không đồng nghĩa cùng một build; mỗi quyết định farm, giao tranh, loot và lai nhánh làm xuất hiện một con đường phát triển khác nhau nhưng vẫn có cách khắc chế.

### Bốn trụ thiết kế (pillars)

1. **Identity:** xuất thân có bản sắc, có giới hạn hợp lore, nhưng không quyết định 100% lối chơi.
2. **Evolution:** lựa chọn nhẫn thuật trong trận là quyết định chiến lược, không chỉ tăng sát thương.
3. **Contested discovery:** farm ổn định + vật phẩm mở nhánh ngẫu nhiên có kiểm soát + mục tiêu công khai để PvP xảy ra tự nhiên.
4. **Readable combat on mobile:** thao tác dễ hiểu, chiêu rõ vùng tác động, hiệu ứng pixel mạnh nhưng màn hình không nhiễu.

### Không phải game này

- Không phải gacha pay-to-win, game thế giới mở vô tận hay MMORPG lưu sức mạnh qua mọi trận.
- Không bắt đầu với tất cả 162 skill hoặc 18 người online cùng lúc ở prototype.
- Không tạo huyết kế chỉ bằng trộn hai nguyên tố; không cấp Thiên Chiếu cho mọi Uchiha.
- Không làm kiểu MOBA 3 đường/phá trụ bắt buộc; đặc trưng là **một bản đồ PvPvE sống** với điểm nóng.

## 2. Trải nghiệm từ sảnh đến kết quả

```text
SẢNH / CREATE NINJA
  chọn gia tộc → ngoại hình → thiên phú chakra → chuyên môn → preset nhánh
      ↓
GHÉP TRẬN / VÀO BẢN ĐỒ
  6 đội x 3 (mục tiêu) → vùng spawn phân tán
      ↓
ĐẦU TRẬN
  farm XP/Ryō → học T1/T2 → chọn đường đi, thăm dò kẻ địch
      ↓
GIỮA TRẬN
  săn elite/boss → cuộn + mảnh bí thuật → T3/T4, chiêu lai, PvP điểm nóng
      ↓
CUỐI TRẬN
  giai đoạn T5 → chiếm 3 khu phong ấn, mở Hạch Trận, khóa hồi sinh dần
      ↓
CHIẾN THẮNG / TỔNG KẾT
  thống kê build, mục tiêu, KDA, nguồn loot → lưu preset/đồ trang trí (không cộng stat vĩnh viễn)
```

### 2.1 Sảnh: quyết định và giới hạn

- **Gia tộc (chọn 1):** Uchiha, Hyūga, Nara, Yamanaka, Akimichi, Aburame, Inuzuka, Uzumaki, Yuki, Hōzuki là danh mục dự kiến; vertical slice chỉ Uchiha, Hyūga, Nara.
- **Thiên phú chakra:** chọn **1 trong 5 hệ cơ bản**; là khởi đầu, không vô hiệu khóa huyết kế/bí thuật. Hệ thứ hai học trong trận qua nhánh/cửa; giới hạn 2 nguyên tố chủ lực (đề xuất); thứ ba hiếm và bị giới hạn.
- **Chuyên môn ưu tiên:** Thể thuật, Ảo thuật, Y thuật, Phong ấn, Khôi lỗi, Triệu hồi hoặc Biến đổi hình thái (từng đợt cập nhật). Chỉ ảnh hưởng preset/thứ tự dễ học, không cho free skill ultimate.
- **Preset:** đánh dấu 3–6 nút mục tiêu kèm đường đi; là UI gợi ý, **không khóa cứng** hướng chơi. Người chơi đổi build trong trận dựa vào loot.
- **Trang phục / ngoại hình:** mô tả được silhouette 48×64 hoặc 64×64; nhân vật nhỏ vẫn cần nhận diện clan qua VFX/icon khi kích hoạt huyết kế.

### 2.2 Tiến trình trong trận

| Tài nguyên | Nguồn | Cách dùng | Giới hạn |
|---|---|---|---|
| XP | quái, tham gia mục tiêu, hỗ trợ combat | tăng level đến 20; gate tier | Không bán bằng tiền thật |
| Ryō | quái, nhiệm vụ, mục tiêu, PvP có giới hạn | học skill, nâng skill/đồ, nhẫn cụ | Mất phần chưa dùng nếu bị hạ tùy giai đoạn |
| SP | cấp và mốc trận | mua nút thuộc đồ thị | Tổng 12 SP mục tiêu cho trận đủ thời lượng |
| Bí quyển/mảnh | elite, boss, sự kiện | thỏa predicate mở nhánh | Không trực tiếp tăng hàng loạt sát thương |
| Chakra | tài nguyên chiến đấu tự hồi/thu hồi | dùng skill, lướt/duy trì nhãn thuật | Cần tài nguyên và counterplay |
| HP | sức sống | bị trừ trong combat, heal có kiểm soát | Không cho chain-heal bất tử |

**Chi phí thiết kế tham khảo:** T0 cấp 1 (0 SP, 0 Ryō), T1 cấp 1 (1 SP, 100 Ryō), T2 cấp 4 (1 SP, 180 Ryō), T3 cấp 8 (1 SP, 280 Ryō), T4 cấp 12 (1 SP, 450 Ryō), T5 cấp 17 (1 SP, 700 Ryō). Giá có thể khác tùy nhóm nếu được ghi rõ trong data.

**Tải kỹ năng (target):** 4 active + 1 ultimate + 3 passive + 1 nội tại gia tộc + 1 nhẫn cụ + 1 **Thế thân riêng**. Học 12 nút không đồng nghĩa dùng đồng thời tất cả. Không phải mỗi nút trong `skills.json` đều là skill bấm nút; root, trait và unlock node có thể chỉ là cổng tiến trình.

## 3. Vòng lặp trận mục tiêu và phase

**Cấu hình tham khảo:** 18 người, 6 đội × 3, mục tiêu 42 phút, cấp 20. Prototype **1 nhân vật offline → 2 client → 6 người**, không xây full 18 ngay.

| Mốc phút | Trải nghiệm chính | Hành vi mong muốn | Điều khiến đội gặp nhau |
|---|---|---|---|
| 00–07 | định hình cơ bản | farm, di chuyển, T1/T2, chọn đường | trại quái & chỗ băng sông |
| 07–15 | tăng tốc build | elite, cuộn, T3 | điểm tranh tài nguyên cấp thấp |
| 15–27 | đa dạng/chiến thuật | T4, lai nhánh, cứu đồng đội | boss vùng và 3 khu phong ấn |
| 27–36 | săn tài nguyên hiếm | chiêu thức tỉnh/đánh cược | boss thế giới, giếng chakra |
| 36–42 | quyết chiến | T5, tích điểm mục tiêu, sống sót | Hạch Trận và khu farm thu hẹp |

Cấp và thời gian là mục tiêu cho người chơi hoạt động bình thường, **không tự tăng level theo đồng hồ**. Thiết kế tránh snowball từ mạng hạ gục: nguồn XP/Ryō PvE ổn định; đội yếu có tuyến vòng khác để quay lại tranh mục tiêu.

### 3.1 Bản đồ mục tiêu

- Một map liền mạch cảm giác rộng, có **6 khu xuất phát tương đối đối xứng**, **4 vùng tài nguyên rìa**, **1 lõi**; đội hình đi theo luồng map chứ không bắt buộc lane.
- Biome: rừng tre/ninja, đầm sương, đồi đá/công sự, tàn tích/phong ấn, sông, boss arena. **Địa hình phải hỗ trợ nhẫn thuật**: đường hẹp cho Thổ, vùng ướt cho Lôi, sương cho trinh sát/Ảo thuật.
- **Phong ấn A/B/C:** điểm nóng kiểm soát, hiển thị trên minimap; phải có nhiều hướng vào và đường rút.
- **Hạch Trận:** trung tâm kết thúc trận; boss/sự kiện báo trước **ít nhất 3 phút** trong thiết kế mục tiêu.
- Không bắt đầu làm 3D traversal thực: góc nhìn **2D top-down 3/4**; chạy trên tường là cơ chế zone/animation giả lập có giới hạn nếu triển khai, không tạo parkour nhiều tầng cao.

### 3.2 Điều kiện thắng (giả thuyết thử nghiệm)

1. Đội chiếm đủ **3 mảnh phong ấn** từ mục tiêu; mang về Hạch Trận và giữ liên tục **120 giây** → thắng trận.
2. Nếu trận hết 42 phút: xếp theo **số điểm mục tiêu** (cách quy đổi sẽ đo và phê duyệt), sau đó số mục tiêu chiếm thành công, sau cùng điểm giao tranh (tie-break cụ thể chốt trước alpha).
3. Nếu chỉ còn một đội hợp lệ sống và không thể hồi sinh, đội đó thắng.
4. Không cho đội bị loại tiếp tục tạo sát thương/chiếm điểm bằng thực thể đã triệu hồi.

**Cần playtest:** giữ Hạch Trận có quá dễ phòng thủ? 120 giây đủ tạo phản công? Quy tắc thắng thời gian có khuyến khích núp không?

### 3.3 Hạ gục và hồi sinh

- **0–24 phút:** đồng đội có thể cứu; nếu bị hạ, hồi sinh giới hạn theo đội ở căn cứ. Dự kiến mất 10–15% Ryō chưa tiêu + một phần vật tư chưa khóa; **không mất kỹ năng đã học**.
- **24–36 phút:** hồi sinh đắt/hiếm, khuyến khích bảo toàn tài nguyên.
- **36 phút trở đi:** không hồi sinh; sống sót là yếu tố quyết định.
- Thời gian hồi sinh, lượt cứu và mức mất cụ thể chưa chốt; server quyết định, UI báo rõ trước mỗi thay đổi giai đoạn.

## 4. PvE, loot và ngẫu nhiên có kiểm soát

| Mục tiêu | Phần thưởng | Quy tắc xuất hiện |
|---|---|---|
| Quái thường | XP, Ryō, nguyên liệu cơ bản | nhiều điểm spawn, có tái sinh |
| Elite | mảnh nhánh hoặc quyền chọn giữa 2–3 nhóm | nguy hiểm vừa, có cạnh tranh |
| Boss vùng | khế ước, ấn lĩnh ngộ, tư liệu T3/T4 | thông báo khu vực / nhiều đường vào |
| Boss thế giới | lõi tiên thuật, chìa thức tỉnh, tài nguyên T5 | công bố toàn map, giới hạn sự kiện |
| Sự kiện tranh chấp | bí quyển đặc thù/đồ dùng chiến thuật | giao tranh chủ động, không độc quyền vô hạn |

**Pity design:** sau **4 lần** hoàn thành mục tiêu cùng nhóm loot mà chưa nhận **tư liệu mục tiêu phù hợp**, cho phép chọn một mảnh **cùng nhóm**. Counter cần tách theo người chơi + loot group, reset khi được mảnh/đổi mục tiêu theo quy tắc định nghĩa; **chưa chốt tỉ lệ %**. Trong prototype có thể dùng deterministic test drop, sau mới đưa RNG thật.

**Nguyên tắc:** vật phẩm hiếm **mở lựa chọn**, không tự cấp huyết kế trái lore hoặc tặng sát thương áp đảo. Nếu người chơi không gặp vật phẩm, luôn có ít nhất một nhánh T4 không phụ thuộc drop cho build có thể chơi tốt. Sự kiện world boss không drop trực tiếp kỹ năng tối thượng cho client.

## 5. Chiến đấu & đối trọng

- Điều khiển mục tiêu **2 ngón**: joystick ảo bên trái; đánh cơ bản + 4 skill + ultimate + nút Thế thân/ninja tool bên phải. Nút bấm không trùm vùng quan sát quan trọng; hỗ trợ tay trái/tay phải sau.
- **Targeting:** skill định hướng bằng kéo/thả (aim vector), skill khóa mục tiêu chỉ khi có tiêu chí rõ và có chỉ báo; không để auto-aim thay thế mọi kỹ năng đòi hỏi kỹ năng cá nhân.
- **Nhịp:** di chuyển phản ứng nhanh, cooldown ngắn cho cơ bản, đòn lớn có startup/telegraph/cost; giữ skill ceiling từ căn hướng và timing.
- **Chakra:** chi phí dùng và duy trì kỹ năng; khi cạn vẫn có nhẫn cụ/đòn thường; không ép đứng im hồi quá lâu.
- **CC:** giảm hiệu quả khi trói/stun liên tiếp (diminishing returns), tránh chuỗi khóa nhân vật không thể thao tác. Thế thân là lối thoát cơ bản có hồi chiêu, không miễn mọi trạng thái.
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
2. **Match HUD:** HP/Chakra, level, Ryō, 4 active + ultimate + Thế thân, joystick, minimap, ping/báo khu boss.
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
- **Vertical Slice:** Uchiha/Hyūga/Nara, Hỏa/Lôi/Thổ, 24–36 nút **được triển khai thật**, 2 combo, boss vùng, một mục tiêu, trận 6 người khi online sẵn sàng.
- **Alpha:** 6 clan, 5 nguyên tố, 60–80 nút, 8–12 người, 3 boss, các điểm phong ấn.
- **Beta target:** 10 clan, catalog 162 node có triển khai/balance theo ưu tiên, 18 người, full objective/telemetry/anti-cheat. Chỉ tăng concurrency sau load test.

Xem tiêu chí nghiệm thu theo cổng: `DEVELOPMENT_ROADMAP.md`.

## 12. Rủi ro / quyết định chưa chốt

| ID | Nội dung | Mặc định đến khi playtest |
|---|---|---|
| GD-01 | Solo hay 3 người chính? | đội 3 là chế độ đích |
| GD-02 | 18 người/42 phút có quá nặng trên mobile? | mục tiêu dài hạn, không ràng buộc prototype |
| GD-03 | Tốc độ trận/độ dày boss/loot? | chỉ giả thuyết, phải đo |
| GD-04 | Joystick, aim assist và camera zoom | test theo thiết bị Android thật |
| GD-05 | Cơ chế revive và tie-break | chưa khóa chi tiết; server phải cấu hình được |
| GD-06 | Tên/thuật bản quyền Naruto | dùng nội bộ; thương mại phải làm rõ quyền |
| GD-07 | Hệ thứ ba & cách lai skill/element | mở hạn chế, phải có counterplay |

## 13. Quy tắc chấp nhận chỉnh sửa Game Design

Thay đổi về số player, duration, economy, clan restriction, cách thắng, revive và target platform chỉ được đưa vào **CHỐT** khi Product Owner duyệt. Agent cập nhật bảng/Change Log và những file liên quan. **Không tự nâng trạng thái ý tưởng lên tính năng đã code**.

### Change Log

| Ngày | Phiên bản | Thay đổi |
|---|---|---|
| 2026-10-16 | 1.0 | Tổng hợp vòng chơi Naruto-inspired, đổi art direction sang mobile 2D HD Pixel Art, xác định scope prototype và trách nhiệm AI |
