# GRAPHICS_DESIGN.md — Thiết kế đồ họa & quy trình sản xuất asset bằng AI

> **Dự án:** Shinobi Evolution (tên nội bộ)  
> **Phiên bản:** 2.1 — 2026-10-16
>
> **Trạng thái:** `ART_DIRECTION_APPROVED_FOR_PROTOTYPE` / các thông số kích thước và ngân sách hiệu năng là **đề xuất cần thử trên điện thoại**  
> **Phạm vi:** 2D HD Pixel Art, góc nhìn MOBA, Android landscape; quy trình làm asset dành cho **một người phát triển**.  
> **Tài liệu liên quan:** `GAME_DESIGN.md` (luật chơi, trải nghiệm); `ARCHITECTURE.md` (Godot và đường dẫn code); `SKILL_SYSTEM.md` (nhẫn thuật); `DEVELOPMENT_ROADMAP.md` (milestone); `../AGENTS.md` (quy tắc AI).

---

## 1. Mục tiêu và các quyết định đã chốt

### 1.1. Mục tiêu hình ảnh

- Game **PvPvE sinh tồn solo**, mỗi người một phe, **2D HD Pixel Art**, camera **top-down 3/4**. Loot, vòng bo và quyết định chạy/đánh cần đọc rõ; farm quái lấy XP là phần tiến trình. Tương phản và độ rõ đòn đánh lấy cảm hứng từ *Wizard of Legend*, không sao chép asset/nhân vật/hoạt ảnh/VFX.
- Thế thân là **bị động tự tiêu cuộn trước sát thương gây chết**, hồi HP rồi tàng hình, kể cả vòng bo. HUD hiển thị số cuộn (một lúc spawn, cap hai), cooldown nội tại và trạng thái sẵn sàng. Tàng hình vẫn nhận damage và lộ khi gây/nhận damage; VFX không hàm ý miễn sát thương. Không có nút kích hoạt thủ công, trụ hồi sinh hoặc cứ điểm buff trong solo.
- **Baseline 2.0:** hai người/trận, Uchiha + Hỏa, hai hướng Hỏa thuật/Ảo thuật. VFX thanh tẩy gỡ icon bất lợi cũ khi Thế thân kích hoạt; profile thử 25% HP/3s stealth/60s cooldown đọc từ state/config. Graph cho xem khi combat nhưng khóa mua/đổi theo timer 5s; túi đầy hiển thị pity chờ nhận riêng, không vẽ vật phẩm bảo hiểm xuống đất.
- Địa hình rừng, sông, hang, làng và khu boss có chiều sâu như game pixel RPG; nhưng chi tiết nền phải tiết chế để người chơi đọc được đòn đánh.
- Nhẫn thuật có nhận diện nguyên tố/gia tộc rõ; khi kỹ năng tiến hóa **hình dạng, nhịp animation và thông tin gameplay** cũng phát triển.
- Camera là 2D nhìn chéo xuống, **không phải** camera 3D sau lưng và **không bắt buộc isometric lưới kim cương 2:1**.
- Ưu tiên **điện thoại Android chạy ngang**, thao tác hai ngón, nhìn rõ nhân vật và telegraph dù nhiều người/quái giao tranh.
- Là dự án **solo**, tối đa hóa tái sử dụng nhân vật gốc, animation chung, tileset, shader và VFX; không bắt đầu bằng việc vẽ hàng trăm kỹ năng.

### 1.2. Bộ công cụ hiện hành

| Công cụ | Vai trò | Bắt buộc trong baseline |
|---|---|---|
| **Antigravity `generate_image`** | Tạo hình gốc, sprite, tile, icon và texture VFX theo reference/prompt | Có |
| **Godot 4 Standard** | UI thật, animation, telegraph/collision, import và kiểm rendered | Có |
| **Python/Pillow hoặc xử lý ảnh local tương đương** | Crop/pad/nearest, alpha, atlas, metadata, preview và validator | Khi cần; không thay tool tạo hình |
| **Pixelorama** | Chỉnh tay nguồn .pxo đã có hoặc khi người dùng muốn sửa về sau | Tùy chọn; không chặn luồng tự làm |
| **Git diff + manifest nguồn** | Giữ trace prompt/raw/revision và bảo vệ asset thủ công | Có; không tự commit/push |

### 1.3. Ranh giới công cụ và quyền tự thực hiện

Luồng chính dùng `generate_image` tích hợp trong Antigravity theo [ART_GENERATION_GUIDE](ART_GENERATION_GUIDE.md). Không tạo Python renderer vẽ ninja thay công cụ này, không yêu cầu người dùng mở Pixelorama để duyệt từng ảnh. Mẫu gọi tool, reference, alpha/grid và master prompt nằm trong guide; phải kiểm tool schema thật, không tự bịa tham số.

Antigravity tự kiểm structural + visual trong Godot rồi promote asset do mình tạo vào runtime theo AUTOPILOT; ghi `agent_validated`, không ghi người dùng đã duyệt. Source .pxo/asset người dùng sửa hoặc owner_locked vẫn được bảo vệ. PNG runtime không bắt buộc phải có bản .pxo; với nguồn sinh ảnh, giữ prompt + references + raw output và recipe hậu xử lý.

---

## 2. Quy chuẩn hình ảnh (visual bible)

### 2.1. Hệ ngôn ngữ thị giác

1. **Silhouette trước chi tiết:** ninja nhận diện qua đầu/tóc/khăn, thân, vũ khí, dáng đứng, màu trang phục; không trông đợi đôi mắt Sharingan có thể đọc từ xa.
2. **Pixel clusters rõ:** các cụm pixel có chủ đích; ưu tiên cạnh vuông sắc, không anti-aliasing trên sprite/tile pixel.
3. **Bóng đổ có chủ đích:** dùng 2–3 cấp sáng/tối cho mỗi vật liệu lớn, hạn chế gradient mượt trên nhân vật.
4. **Nền ít bão hòa hơn VFX:** nền không tranh độ sáng với telegraph; không dùng đồng loạt các vùng đỏ/cam rực trong map.
5. **Ánh sáng hiện đại có giới hạn:** glow, shader, particles có thể mềm hơn sprite nhưng chỉ phụ trợ; không được xóa nét pixel, che nhân vật hay thông tin PvP.
6. **Dễ đọc trên màn hình nhỏ:** ưu tiên vùng tác động, hướng đạn và trạng thái combat trước chi tiết trang trí.

### 2.2. Hướng nhìn và phối cảnh

- Nhân vật **3/4 từ trên xuống**: nhìn thấy đỉnh đầu/vai vừa đủ, chân chạm mặt đất; style phải giống nhau giữa nhân vật, quái và props.
- Camera `Camera2D` theo nhân vật, độ zoom **được thử thực tế**, không thay đổi tự do tùy chiêu để tránh bất lợi PvP.
- Props có gốc sắp lớp (Y-sort origin) tại **điểm tiếp xúc mặt đất**, không phải đỉnh sprite. Vật thể cao cho phép fade khi che nhân vật.
- Quái/boss và cây có thể có chiều cao giả bằng sprite chồng lớp; **không triển khai chiến đấu nhiều tầng 3D thực** ở prototype.

### 2.3. Kích thước và hệ tọa độ đề xuất

| Thành phần | Chuẩn **đề xuất cho prototype** | Ghi chú |
|---|---|---|
| Tile thế giới | **32×32 px** | Một tile grid chính; tránh trộn 16/24/48 pixel thiếu quy tắc |
| Canvas ninja thường | **64×64 px/frame** | Nhân vật có thể chỉ chiếm 32–44 px chiều rộng bên trong frame |
| Boss nhỏ | **128×128 px/frame** | Thực tế tùy boss, không buộc mọi quái cùng size |
| Icon kỹ năng | **32×32 hoặc 48×48 px** | Chọn 1 kích thước chính theo test HUD |
| Logical world reference | **640×360 px** | Mốc thử; UI và safe area có thể dùng cơ chế scale khác |
| Palette nhân vật | Khoảng **16–32 màu** sử dụng có chủ đích | Không phải giới hạn cứng của file PNG |
| Hướng chuyển động | **4 hướng trước**, có thể lên 8 sau | `south`, `west`, `east`, `north` |
| Animation nhân vật đầu tiên | idle, run, attack, cast, hurt, dodge, death | Chỉ làm idle/run cho mốc movement |
| Animation thử nghiệm | idle 4 frame, run 6 frame/hướng | Con số tham khảo, thay theo chất lượng |
| Texture filtering | **Nearest** cho sprite và tile pixel | UI/font có thể dùng cách render khác |

**Lưu ý pixel-perfect:** `640×360` với viewport scale nguyên rất sắc ở một số tỉ lệ màn hình, nhưng Android có nhiều tỉ lệ 16:9–20:9 và safe area khác nhau. Cần test `viewport`/`canvas_items`, `expand`/`keep`, integer scaling và độ lớn HUD thực tế; **không mặc định một cấu hình đúng cho mọi máy**. Chỉ chốt sau playtest M2.

### 2.4. Palette và nhận diện nguyên tố

| Nhóm | Màu gợi ý (không phải màu gameplay duy nhất) | Hình ngôn ngữ quan trọng hơn màu |
|---|---|---|
| Hỏa | cam, đỏ ấm, vàng | ngọn lửa răng cưa, vùng cháy, nhịp bùng nổ |
| Thủy | lam, xanh ngọc | dòng chảy, vòng nước, giọt và sóng |
| Lôi | vàng chanh, lam điện | tia gấp khúc, đường giật, chớp ngắn |
| Phong | xanh nhạt, trắng xám | lưỡi cong, vệt hút/đẩy, xoáy |
| Thổ | nâu, vàng đất | khối vuông, bụi, tường rắn |
| Bóng/khống chế | tím đen, xám | dải bóng nối đất, vùng trói, ấn khống chế |
| Hồi phục/hỗ trợ | xanh lá dịu | vòng hồi phục, dấu cộng/hoa văn |

**Không truyền thông tin bằng màu đơn độc.** Hình dạng, âm thanh, họa tiết telegraph và icon trạng thái phải vẫn hiểu được khi người chơi giảm độ bão hòa hoặc khó phân biệt màu.

---

## 3. Kiến trúc nhân vật: một base dùng cho nhiều gia tộc

### 3.1. Nhân vật chia lớp (modular character)

Thay vì vẽ 10 gia tộc × 7 animation × 4 hướng từ đầu, xây **một ninja base** dùng chung animation và tách các lớp:

```text
NinjaVisual
├── GroundShadow        # ellip tối giản theo vị trí chân
├── BodySprite          # cơ thể + cử động base
├── OutfitOverlay       # áo/giáp/áo choàng nếu đồng bộ frame
├── HairHeadbandOverlay # tóc, băng, phụ kiện
├── WeaponOverlay       # kunai/kiếm/nhẫn cụ
├── ClanVFX             # thức tỉnh/năng lực đang bật
└── StatusMarker        # trạng thái rõ ngay cả khi zoom xa
```

Đây là **đề xuất cấu trúc scene**, chưa phải scene đã tồn tại. Không tạo nhiều layer nếu việc canh lại toàn bộ animation tốn công hơn lợi ích; giai đoạn đầu có thể gộp base + outfit vào cùng một sprite và dùng overlay cho vài bộ phận thật sự thay đổi.

### 3.2. Quy tắc animation

- Các frame của **một animation** có **cùng canvas** và chân đứng tại **cùng pivot cố định**; không crop từng frame khiến ninja giật lên xuống.
- Tên hướng thống nhất: `south`, `west`, `east`, `north` (chỉ số hàng khi dùng spritesheet cũng theo thứ tự này).
- Hỗ trợ lật `east ↔ west` **chỉ** với sprite không có vũ khí/trang phục bất đối xứng quan trọng; kiểm tra hitbox và tay cầm khi mirror.
- Ưu tiên **anticipation → impact → recovery** cho cast/attack; animation không quyết định trực tiếp sát thương trong multiplayer.
- Kỹ năng đơn giản tái sử dụng animation `cast_generic`; kỹ năng biểu tượng mới tạo animation riêng khi gameplay đã hoàn thiện.
- Animation hit/hurt cần nhìn rõ ở kích thước chơi thật, không phải chỉ khi zoom 800% trong editor.

### 3.3. Nhận diện gia tộc

- Gia tộc tác động vào palette/trang phục/dáng vũ khí và **VFX riêng khi kích hoạt khả năng**, nhưng **không** mặc định rằng mọi người cùng gia tộc sở hữu tất cả nhãn thuật hiếm.
- Huyết kế nhãn thuật: dùng **icon/hiệu ứng quanh nhân vật** hoặc chỉ báo nhỏ, không chỉ dựa vào thay đổi pixel của mắt.
- Các nhánh Nara/Yamanaka/Akimichi/Aburame/Inuzuka cần nhận diện bằng **hình dạng kỹ năng** (bóng, sóng tâm thuật, bội hóa, đàn trùng, nhẫn khuyển), không chỉ một màu áo.
- Hình dùng để phát hành phải là **thiết kế gốc hoặc có quyền hợp lệ**, không xuất lại sprite Naruto/anime hay sao chép hình từ Wizard of Legend.

---

## 4. Hệ thống bản đồ và môi trường

### 4.1. Một bộ tileset chính trong vertical slice

Bắt đầu từ **rừng ninja**: ground (đất/cỏ), path, bụi, cây, đá, nước nông, vách, cầu nhỏ, điểm farm và khu elite/boss. Ưu tiên **tái sử dụng** các ô ghép, decal và palette biến thể hơn là vẽ nhiều map hoàn chỉnh.

**Quy tắc tileset:**

- `32×32 px/tile`, kết nối rõ giữa cỏ–đất–nước; tile cạnh/góc không tạo đường gãy vô lý.
- Layer tối thiểu: `Ground`, `Obstacles`, `Props`, `Overhang`, `CombatTelegraph`, `Characters`, `HUD`; thứ tự render chi tiết đối chiếu `ARCHITECTURE.md`.
- Cây và công trình cao phải có collision và vùng che được xử lý; không được tạo chỗ trốn nhìn không thấy nhưng vẫn trúng damage bất ngờ.
- Vật thể tương tác, loot và boss arena **nổi bật hơn props trang trí**.
- Vật liệu nước, đá, rừng hỗ trợ biểu hiện trạng thái như `WET`, `BURN`, `EARTH_WALL`; logic gameplay nằm ở hệ combat, không được suy từ màu pixel.

### 4.2. Asset pack bên ngoài

- Chỉ dùng asset có **giấy phép rõ ràng cho mục đích định phát hành**; ghi lại tác giả, URL, license, ngày tải, có cần attribution không.
- Không ghép các pack có tỷ lệ đầu/thân, góc nhìn hoặc tile size khác nhau trước khi được chỉnh về **visual bible**.
- Asset từ AI cũng cần kiểm tra điều khoản dịch vụ và nguy cơ mô phỏng nhân vật có bản quyền.

---

## 5. Quy chuẩn hiệu ứng nhẫn thuật (VFX bible)

### 5.1. Anatomy của một skill

Một nhẫn thuật có thể gồm tối đa những lớp sau, **không bắt buộc tất cả**:

```text
[telegraph / cảnh báo vùng nguy hiểm]
       ↓
[cast animation + âm thanh báo hiệu]
       ↓
[projectile / dash / area / trap / summon]
       ↓
[impact effect + trạng thái trúng đòn]
       ↓
[aftermath: vùng cháy / nước / sương / bóng ...]
```

- **Vùng hit và kết quả sát thương do combat/authority quyết định**, không lấy vị trí random particle làm hitbox.
- Telegraph phải nhìn thấy **trước tác động** đối với chiêu nguy hiểm; dùng vòng, đường, hình nón và pattern rõ trên cả nền nước/rừng.
- VFX **đồng đội/địch/bản thân** có quyền ưu tiên hiển thị khác nhau; đòn nguy hiểm từ địch không bị giản lược đến mức biến mất.
- Giới hạn camera shake, flash trắng, bloom và thời lượng hiệu ứng chiếm màn hình; có lựa chọn giảm hiệu ứng.

### 5.2. Phân biệt tiến hóa hình ảnh với rank sức mạnh

Ví dụ *Hỏa Cầu* (thiết kế game, tên nhánh chỉ là gợi ý):

| Tier minh họa | Hình ảnh | Thay đổi gameplay có thể có |
|---|---|---|
| T1 | 1 đạn lửa đơn, vệt ngắn | projectile một mục tiêu |
| T3-A | 3 đạn lửa nhỏ | multi-projectile, dễ né từng viên |
| T3-B | cầu lửa lớn, cảnh báo đường bay | AoE/cooldown cao hơn |
| T4 lai | hỏa cầu tương tác gió | lan lửa trong vùng/tương tác môi trường |
| T5 | biển lửa có vòng cảnh báo rõ | area denial trong thời gian giới hạn |

**Không mặc định:** VFX to hơn = sát thương cao hơn mọi trường hợp; T5 = màn hình trắng sáng không có counterplay. Thông số thật và điều kiện unlock nằm ở `SKILL_SYSTEM.md`/`skills.json`/runtime sau khi duyệt.

### 5.3. VFX dùng chung và biến thể

Tạo bộ thành phần tái sử dụng:

- `fire_core`, `ember_particles`, `burn_decal`, `fire_telegraph`;
- `lightning_arc`, `spark_impact`, `chain_indicator`;
- `water_splash`, `water_trail`, `wet_area`;
- `wind_slash`, `wind_swirl`, `knockback_ring`;
- `earth_fragment`, `dust_ring`, `earth_wall`;
- `status_icon`, `skill_unlock_flash`.

`LIGHT` trong ID skill cũ là tên data legacy cho **Lôi**, không được hiểu là hệ “ánh sáng” trong asset naming; nên dùng từ `lightning` cho VFX. **Không đổi ID của `skills.json` chỉ để khớp tên file VFX.**

---

## 6. Quy trình tạo asset bằng generate_image

### 6.1. Pipeline hiện hành

```text
Brief asset + profile/style card
 → điền MASTER PROMPT + JOB + negative constraints
 → gọi generate_image tích hợp, dùng reference thật
 → giữ output gốc + prompt/reference trong art_source/
 → crop/pad/nearest/alpha/atlas và metadata bằng xử lý kỹ thuật
 → structural checks + preview 1x/4x + xem animation/tiling
 → tự sửa prompt/ref/sinh lại khi lỗi
 → promote PNG + manifest agent_validated
 → import Godot, chạy rendered scene, kiểm input/VFX và lưu bằng chứng
 → tiếp tục batch/task; người dùng chơi nghiệm thu ở cuối
```

Không coi ảnh concept, ảnh đúng kích thước hoặc headless parse đạt là bằng chứng sprite/animation đạt. `generate_image` không bảo đảm grid/alpha/identity tuyệt đối; validator và xem ảnh thật là bắt buộc. Nếu không đạt, chia batch một animation/một hướng hoặc từng pose, không stretch ảnh sai vào sheet.

### 6.2. Tệp và nguồn gốc

| Tệp | Vai trò / quy tắc |
|---|---|
| `art_source/prompts/<asset_id>/<revision>.json` | Full prompt, tool schema dùng, reference paths/hash và kết quả gọi |
| `art_source/generated/<asset_id>/<revision>/` | Output gốc; không ghi đè revision cũ |
| `art_source/previews/` | Contact sheet, animation/tiling/alpha preview; được sinh lại |
| `art_source/pixelorama/*.pxo` | Nguồn thủ công nếu có; không tự overwrite |
| `assets/sprites/`, `assets/tilesets/`, `assets/vfx/`, `assets/ui/icons/` | PNG runtime do agent kiểm và promote |
| `data/art/asset_manifest.json` | Source → runtime, layout/FPS/anchor, nơi dùng, trạng thái kiểm |
| `tools/art_pipeline/` | Xử lý ảnh kỹ thuật và validator; không là công cụ tạo hình thay generate_image |

Tạo thư mục theo batch, không coi bảng là file đã tồn tại. Asset đã sửa tay lấy .pxo làm nguồn nếu có; asset từ generate_image lấy prompt/reference/raw + hậu xử lý làm nguồn. Không có hai pipeline âm thầm overwrite cùng PNG.

### 6.3. Metadata tối thiểu

```json
{
  "asset_id": "ninja_base_run_south",
  "revision": "v001",
  "source_tool": "generate_image",
  "prompt_record": "art_source/prompts/ninja_base_run_south/v001.json",
  "raw_source": "art_source/generated/ninja_base_run_south/v001/raw.png",
  "runtime_png": "res://assets/sprites/characters/ninja_base_run_south.png",
  "frame_size": [64, 64],
  "columns": 4,
  "rows": 1,
  "direction": "south",
  "animation": "run",
  "frame_count": 4,
  "fps": 8,
  "foot_anchor_px": [32, 55],
  "review_status": "agent_validated",
  "owner_accepted": false
}
```

Ví dụ này mô tả **riêng một animation/một hướng**, không là tuyên bố asset đã được tạo hoặc kiểm. Không dùng cùng layout cho idle/run có frame count khác nhau. Hash/output actual size/mode, mirror info, provenance và check results bổ sung theo ART_GENERATION_GUIDE. Không tự ghi model/seed nếu tool không trả.

### 6.4. Xử lý và nguồn sửa tay tùy chọn

Được crop/pad, giảm kích thước nearest-neighbor, xử lý alpha/palette có kiểm, đóng atlas và sinh preview. Không tạo pose giả hoặc thay creative image generation bằng code. Nền checkerboard được vẽ vào PNG không là alpha; cần sửa bằng tool hoặc xử lý nền đồng nhất có kiểm halo.

Pixelorama chỉ cần khi chỉnh tay về sau. Không yêu cầu cài/CLI/nguồn .pxo để Antigravity tiếp tục task. Nếu đã có .pxo, bảo vệ và dùng PNG export tương ứng; muốn thử biến thể do AI thì tạo path/revision khác, giữ nguyên nguồn người dùng.

## 7. Đặt tên, promotion và hồ sơ asset

### 7.1. Tên file

Dùng snake_case ASCII: `ninja_base_run_south.png`, `forest_ground_01.png`, `fire_impact_small.png`, `icon_fire_ball.png`. Skill ID không thay bằng asset ID; mapping rõ trong manifest/runtime config.

### 7.2. Promotion tự động trong quyền đã giao

Antigravity được tự promote/thay **asset do chính mình tạo trong batch hiện hành** sau structural + visual checks. Không cần người dùng duyệt từng PNG. Giữ raw/revision cũ, cập nhật metadata và chạy lại import/scene liên quan; asset owner_locked, .pxo hoặc nguồn người dùng sửa không được overwrite/xóa. Tạo variant mới nếu cần thay nguồn bị khóa.

Không tự xóa asset ngoài task, lấy ảnh tham chiếu có quyền sử dụng rõ; không commit/push hay giả ghi approved-by-owner. Agent tự kiểm không thay human acceptance cuối.

### 7.3. Hồ sơ tối thiểu

Ghi asset_id/revision, full prompt, references/hash, đường dẫn output thật, actual pixel size/mode/alpha, frame layout/FPS/anchor, runtime path/nơi dùng và kết quả từng check. Các trạng thái: `generated`, `needs_fix`, `agent_validated`, `owner_accepted`, `deprecated`. Chỉ chuyển owner_accepted sau người dùng chơi/duyệt thật.

---

## 8. Kiểm thử đồ họa & hiệu năng Android

### 8.1. Quality profiles (đề xuất, chưa phải benchmark)

| Thành phần | Low | Medium | High |
|---|---|---|---|
| Particle density | thấp, giới hạn emitter | trung bình | đủ để đẹp nhưng không che hitbox |
| Hit/impact flashes | ngắn, sáng vừa | mặc định | đẹp hơn nhưng vẫn có tùy chọn giảm |
| Glow/shader | tắt/bản thay thế nếu quá nặng | giới hạn | có chọn lọc |
| VFX đồng đội không quan trọng | giản lược mạnh | giản lược | gần đầy đủ |
| Telegraph địch | **luôn rõ** | **luôn rõ** | **luôn rõ** |
| Camera shake | tùy chọn tắt | mức thấp | mức thấp, có slider |

**Mục tiêu thử nghiệm:** 30 FPS ổn định trên nhóm thiết bị Android cấu hình thấp được chọn để test; 60 FPS trên nhóm máy khá hơn. Đây là **mục tiêu để đo**, không phải tuyên bố hiệu năng thực tế. Ghi thêm frametime/memory, số người/quái/particle, map và phiên bản build trong báo cáo.

### 8.2. Các trường hợp kiểm thử bắt buộc

- **Pixel sharpness:** nhân vật/tiles sắc, không mờ/lòe pixel ở tỉ lệ màn hình mục tiêu; UI đủ lớn.
- **Pivot:** ninja chạy 4 hướng không bị nhảy vị trí chân; bóng sát đất, hitbox không trượt theo tóc/vũ khí.
- **Animation:** không mất frame, sai thứ tự hàng, nhầm `north/south`, lệch thời gian impact.
- **Safe area:** joystick, 4 nút active + ultimate, thanh HP/Chakra, minimap không bị notch/gesture bar che trên landscape.
- **Combat clarity:** khi nhiều VFX nổ, vẫn thấy ninja của mình, skill quan trọng của địch, telegraph boss và vùng đường đi.
- **Performance:** kiểm tra trong cảnh stress test với quái + đạn + vùng cháy + triệu hồi + player; tránh nhân bản vô hạn node/particle.
- **Accessibility:** có thể giảm flash/shake; cảnh báo nguy hiểm có shape/pattern ngoài màu.
- **Asset origin:** file đã dùng trong game có provenance/giấy phép; không dùng trực tiếp asset Naruto/Wizard of Legend nếu không có quyền.

### 8.3. Validator tự động mà Antigravity cần xây

Validator đọc asset + metadata và trả báo cáo **PASS/FAIL**, tối thiểu kiểm:

1. PNG tồn tại, kích thước đúng; `RGBA`/alpha khi cần nền trong suốt.
2. Sprite sheet chia hết cho width/height từng frame; số cột/hàng trùng metadata.
3. Mỗi frame nằm trong vùng canvas; `foot_anchor_px` hợp lệ.
4. Runtime chỉ cập nhật từ promotion có manifest/checks trong quyền AUTOPILOT; nguồn thủ công/owner_locked không bị ghi đè.
5. Không có tên file trùng `asset_id` hoặc tham chiếu runtime tới đường dẫn không tồn tại.
6. Đối với sprite pixel: phát hiện cảnh báo màu bán trong suốt/antialiasing không mong muốn (không đánh fail đối với hiệu ứng intentionally alpha).
7. Manifest có prompt/raw/reference/provenance và trạng thái kiểm đúng thực tế; không giả owner_accepted.

Validator **không thể tự chấm được** nhân vật đẹp hay cử động tự nhiên. Antigravity phải xem preview/scene rendered để tự sửa; người dùng nghiệm thu bằng chơi ở cuối. Pixelorama không là bước bắt buộc.

---

## 9. Roadmap sản xuất đồ họa cho một người

Roadmap này **phụ thuộc** milestone kỹ thuật trong `DEVELOPMENT_ROADMAP.md`; không thêm trạng thái `DONE` vào roadmap chính khi chưa test.

| Mốc | Bộ đồ họa phải có | Không làm ở mốc này |
|---|---|---|
| **A0 — Visual baseline** | palette mẫu, 1 ninja 64×64 đứng, 1 icon, 1 tile 32×32, quy ước hướng/pivot | 10 gia tộc, 8 hướng |
| **A1 — Movement slice** | ninja idle/run 4 hướng, bóng chân, map rừng nhỏ, tường/đá | VFX ultimate |
| **A2 — Mobile slice** | joystick, nút đánh, HP/Chakra, camera/safe area, pixel quality test Android | HUD 100 kỹ năng |
| **A3 — Combat slice** | attack/cast/hurt, 2 quái, hiệu ứng mẫu Hỏa/Ảo thuật/Thế thân, loot icon | 162 kỹ năng, hệ ngoài allowlist |
| **A4 — Skill progression** | nút cây nhẫn thuật, locked/unlocked/available, icon T0–T2, 1 nhánh có tiến hóa VFX | tất cả thức tỉnh |
| **A5 — Vertical slice** | Uchiha/Hỏa, hai hướng Hỏa thuật/Ảo thuật, 1 boss, map loot/bo/PvP cho hai người | thêm clan/nature, bản đồ vô tận |
| **A6 — Scale after tests** | sprite atlas, VFX quality profiles, style guide mở rộng, batching phù hợp | sản xuất đại trà trước khi stress test |

### Bộ thử nghiệm nên làm ĐẦU TIÊN

- `ninja_base_idle_south.png` — frame 64×64, một ninja **thiết kế gốc**.
- `ninja_base_run_sheet.png` — run 4 hướng × 6 frame, cùng foot anchor; nếu làm chưa đẹp, cho phép placeholder 2–4 frame trước.
- `forest_ground_32.png` — nhóm tile 32×32, có cỏ/đất/đường.
- `fire_projectile_small.png` — một đạn lửa rõ hướng đi, có telegraph riêng nếu là đòn khó né.
- `skill_fire_icon_32.png` — icon 32×32 phân biệt với nền.

**Cổng tự kiểm đầu tiên:** đặt ninja vào map Godot có render, di chuyển/joystick, sprite không nhòe hoặc rung, một hiệu ứng lửa rõ mà không che màn hình. Có máy Android thì thử trực tiếp, chưa có thì ghi NOT_RUN_DEVICE và tiếp tục desktop/touch simulation/export. Không dừng để người dùng duyệt asset; không mở rộng clan ngoài baseline.

---

## 10. Prompt/brief thực hiện

### 10.1. Giao Antigravity

Đọc AGENTS + ANTIGRAVITY_AUTOPILOT + tài liệu này + ART_GENERATION_GUIDE. Đi từ identity master/idle/run đến scene có render, rồi tiếp tục các batch art theo task tới M8; gọi generate_image thật và giữ full prompt/reference/output. Tự xem preview, sửa lỗi, validate/promote và cập nhật manifest. Không dừng chờ duyệt A0 hoặc bắt người dùng sửa Pixelorama. Không thay công cụ tạo hình bằng Python generator.

### 10.2. Checklist tự review / Codex nếu sẵn có

Kiểm tool provenance, file paths/Windows Unicode, bảo vệ art thủ công, alpha/grid/frame/anchor, palette/identity/camera, runtime mapping, import Godot và rendered screenshot. Ghi ai thực sự đã xem ảnh; không kết luận chất lượng mỹ thuật từ validator. Review độc lập nếu có là bổ sung, không chặn task kế tiếp khi self-check đã đạt.

### 10.3. Brief mỗi asset

```text
Task / asset_id / revision:
Gameplay purpose / nơi dùng:
Reference image paths thật:
Identity/style/camera/palette phải giữ:
Logical frame size / count / directions / FPS / foot anchor:
Alpha / tiling / padding / runtime output:
MASTER PROMPT + JOB đã điền đủ:
Raw output + prompt record + manifest:
Structural + visual + rendered checks:
Kết quả / lỗi / thay đổi prompt / task kế tiếp:
```

Mẫu prompt có thể dùng trực tiếp và JOB cụ thể nằm trong [ART_GENERATION_GUIDE](ART_GENERATION_GUIDE.md). Không gọi tool khi còn biến chưa điền hoặc reference chưa tồn tại.

## 11. Decision log — những gì đã chốt và đang mở

| ID | Trạng thái | Quyết định |
|---|---|---|
| GFX-001 | **CHỐT** | 2D HD Pixel Art, MOBA top-down 3/4, Android landscape |
| GFX-002 | **CHỐT** | Godot 4 + GDScript, VS Code, Antigravity phát triển, Codex review chỉ đọc |
| GFX-003 | **ĐÃ CẬP NHẬT 2.1** | generate_image → raw/prompt → hậu xử lý kỹ thuật → tự kiểm/promote → PNG Godot; Pixelorama tùy chọn, vẫn bảo vệ art thủ công |
| GFX-004 | **CHỐT** | Solo-first, một ninja modular base, 4 hướng animation trước, VFX tái sử dụng |
| GFX-005 | **PROTOTYPE TARGET** | 32×32 tiles, 64×64 ninja frame, 640×360 world reference; phải test Android |
| GFX-006 | **PROTOTYPE TARGET** | 30/60 FPS theo phân khúc máy; không cam kết khi chưa đo |
| GFX-007 | **PROTOTYPE_DEFAULT** | Style card/palette khởi đầu trong ART_GENERATION_GUIDE; agent tự chọn font/HUD trong art direction và kiểm, không chờ duyệt từng asset |
| GFX-008 | **PROTOTYPE_DEFAULT / MỞ RỘNG ĐỂ SAU** | Bản đầu bốn hướng theo ART guide, atlas/glow tự kiểm theo thiết bị; tám hướng phát hành không thuộc scope hiện tại |
| GFX-009 | **CHỐT VỀ NGUYÊN TẮC** | Không sao chép asset của Naruto hay Wizard of Legend nếu không có quyền khai thác |
| GFX-010 | **CHỐT** | Theo hướng solo sinh tồn: HUD cuộn Thế thân bị động; không có nút dùng Thế thân, cứ điểm buff hoặc trụ hồi sinh solo; giữ camera top-down 3/4 |
| GFX-011 | **CHỐT THEO GAMEPLAY 2.0** | Asset bản đầu Uchiha/Hỏa cho hai người; hai hướng Hỏa thuật/Ảo thuật, thanh tẩy/stealth bị động, timer combat và pity chờ riêng; không mở rộng ba clan/ba nature trước nghiệm thu |
| GFX-012 | **CHỐT THEO YÊU CẦU 2026-10-16** | Dùng generate_image tích hợp Antigravity và prompt chung ART_GENERATION_GUIDE; agent tự kiểm/promote, người dùng chỉ nghiệm thu khi chơi được |

### 11.1. Cách duy trì tài liệu này

- `GAME_DESIGN.md` là nguồn chính cho **cảm giác chơi / rules**, `SKILL_SYSTEM.md` cho **kỹ năng / unlock**, file này cho **hình ảnh / pipeline asset**, `ARCHITECTURE.md` cho **Godot implementation**.
- Trong AUTOPILOT, Antigravity được điều chỉnh thông số art prototype/folder trong phạm vi đã giao khi có lý do/checks và cập nhật manifest/tài liệu; không dừng xin duyệt từng ảnh. Thay art direction cốt lõi hoặc overwrite nguồn người dùng vẫn ngoài quyền tự làm.
- `AGENTS.md` đã có mục tra cứu `GRAPHICS_DESIGN.md`; task sprite/UI/map/VFX/animation/asset generator cần đọc các phần liên quan của tài liệu này.
- Các link kỹ thuật nên tham khảo: [Pixelorama Import](https://pixelorama.org/user_manual/Import/), [Pixelorama Save/Export](https://pixelorama.org/user_manual/save_and_export/), [Pixelorama CLI](https://pixelorama.org/user_manual/cli/), [Godot – Multiple Resolutions](https://docs.godotengine.org/en/stable/tutorials/rendering/multiple_resolutions.html).

---

**Tiêu chuẩn thành công:** Antigravity biết tạo asset bằng generate_image, giữ nguồn/prompt, tự kiểm kỹ thuật và rendered output, đưa vào Godot rồi tiếp tục đến bản chơi được; người dùng kiểm cảm giác/độ rõ bằng chơi thực tế ở cuối. Source thủ công vẫn được bảo vệ.
