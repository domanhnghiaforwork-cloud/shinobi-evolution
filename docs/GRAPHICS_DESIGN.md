# GRAPHICS_DESIGN.md — Thiết kế đồ họa & quy trình sản xuất asset bằng AI

> **Dự án:** Shinobi Evolution (tên nội bộ)  
> **Phiên bản:** 1.0 — 2026-10-16  
> **Trạng thái:** `ART_DIRECTION_APPROVED_FOR_PROTOTYPE` / các thông số kích thước và ngân sách hiệu năng là **đề xuất cần thử trên điện thoại**  
> **Phạm vi:** 2D HD Pixel Art, góc nhìn MOBA, Android landscape; quy trình làm asset dành cho **một người phát triển**.  
> **Tài liệu liên quan:** `GAME_DESIGN.md` (luật chơi, trải nghiệm); `ARCHITECTURE.md` (Godot và đường dẫn code); `SKILL_SYSTEM.md` (nhẫn thuật); `DEVELOPMENT_ROADMAP.md` (milestone); `../AGENTS.md` (quy tắc AI).

---

## 1. Mục tiêu và các quyết định đã chốt

### 1.1. Mục tiêu hình ảnh

- Game hành động PvPvE survival × MOBA × RPG, **2D HD Pixel Art**, camera **top-down 3/4**; tương phản, tốc độ và độ rõ đòn đánh **lấy cảm hứng từ *Wizard of Legend***, nhưng **không sao chép asset, nhân vật, hoạt ảnh hay VFX** của trò chơi đó.
- Địa hình rừng, sông, hang, làng và khu boss có chiều sâu như game pixel RPG; nhưng chi tiết nền phải tiết chế để người chơi đọc được đòn đánh.
- Nhẫn thuật có nhận diện nguyên tố/gia tộc rõ; khi kỹ năng tiến hóa **hình dạng, nhịp animation và thông tin gameplay** cũng phát triển.
- Camera là 2D nhìn chéo xuống, **không phải** camera 3D sau lưng và **không bắt buộc isometric lưới kim cương 2:1**.
- Ưu tiên **điện thoại Android chạy ngang**, thao tác hai ngón, nhìn rõ nhân vật và telegraph dù nhiều người/quái giao tranh.
- Là dự án **solo**, tối đa hóa tái sử dụng nhân vật gốc, animation chung, tileset, shader và VFX; không bắt đầu bằng việc vẽ hàng trăm kỹ năng.

### 1.2. Bộ công cụ tối giản

| Công cụ | Vai trò | Có bắt buộc không? |
|---|---|---|
| **Godot 4 + GDScript** | Lắp scene, TileMapLayer, AnimatedSprite2D, UI, hiệu ứng, camera, xuất Android | **Có** |
| **VS Code** | Quản lý project, xem source, Git diff, tài liệu | **Có** |
| **Antigravity** | AI chính: viết generator Python, script kiểm tra asset, code import/VFX trong Godot | **Có trong workflow** |
| **Codex** | Review độc lập, mặc định chỉ đọc: logic import, format asset, hiệu năng, không tự sửa | **Có trong workflow** |
| **Pixelorama** | Chỉnh pixel thủ công, tổ chức layer/frame, animation, lưu nguồn `.pxo` | **Khuyên dùng** |
| **Python 3 + Pillow** | Tạo ảnh PNG/spritesheet **theo thuật toán và cấu hình JSON** | **Có khi xây generator** |
| **Git/GitHub** | Giữ phiên bản recipe, file `.pxo`, PNG được chấp thuận; rollback | **Có** |
| AI tạo ảnh tham chiếu | Phác thảo concept nhân vật, địa hình, VFX nếu cần | **Tùy chọn**, không phải nguồn sprite hoàn chỉnh mặc định |

**Chưa cần:** Blender, Photoshop, Spine, công cụ VFX đắt tiền, phần mềm tilemap riêng, plugin Pixelorama AI tự phát triển. Chỉ bổ sung khi một nhu cầu đã được kiểm chứng.

### 1.3. Ranh giới nhiệm vụ giữa các công cụ

- **Antigravity không phải họa sĩ tự động biết vẽ đẹp.** Nó giỏi sinh file code, biến thể theo quy tắc, kiểm tra kích thước/palette/frame và tích hợp vào Godot.
- **Pixelorama không trực tiếp hiểu JSON tùy ý như lệnh tạo hình** và không chạy Python như một trình thông dịch. Generator phải tạo **PNG** (hoặc format import được khác), rồi Pixelorama nhập để sửa. Pixelorama có hỗ trợ nhập **SVG** và **OpenRaster `.ora`**, nhưng **PNG là chuẩn trung gian mặc định**.
- **Pixelorama lưu nguồn chỉnh sửa là `.pxo`**; file dùng trong Godot là PNG/spritesheet đã xuất. Không yêu cầu Godot đọc `.pxo` như texture runtime.
- **Codex review code, dữ liệu, pipeline và rủi ro hiệu năng**; cảm giác thẩm mỹ, tư thế diễn hoạt và độ dễ đọc cuối cùng do **bạn duyệt bằng mắt và thiết bị thật**.

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

## 6. Quy trình tạo asset bằng code + AI + Pixelorama

### 6.1. Pipeline đã chọn

```text
Bạn mô tả asset + tiêu chí chất lượng
  ↓
Antigravity tạo recipe JSON + Python/Pillow generator
  ↓
Sinh PNG / sprite sheet / metadata JSON (BẢN NHÁP)
  ↓
Bạn xem ở kích thước thật → nếu chưa đẹp, chỉnh recipe hoặc Pixelorama
  ↓
Pixelorama: sửa nét pixel, palette, pose, frame, layers → lưu .pxo
  ↓
Export PNG spritesheet từ Pixelorama → asset ĐÃ DUYỆT
  ↓
Godot: import nearest, tạo SpriteFrames / TileSet / VFX scene
  ↓
Antigravity kiểm tra kỹ thuật → Codex review → bạn test Android
```

**Quan trọng:** code generator tạo hình theo quy tắc, không bảo đảm tự sinh ra sprite chất lượng như artist. **AI tạo ảnh tham chiếu** dùng để tìm dáng, màu và phong cách; khi chuyển sang pixel art phải kiểm tra grid, silhouette, các frame và pivot. Không yêu cầu AI sinh ngay 8 hướng × hàng chục animation rồi đưa thẳng vào game.

### 6.2. Tệp và “nguồn sự thật” cho đồ họa

| Tệp | Chứa gì | Ai sửa? | Có được tự ghi đè? |
|---|---|---|---|
| `tools/asset_generator/recipes/*.json` | Thông số màu, kích thước, outfit, frame | Bạn phê duyệt; Antigravity đề xuất | Có qua diff/duyệt |
| `tools/asset_generator/*.py` | Thuật toán sinh pixel, spritesheet, kiểm tra | Antigravity; Codex review | Có qua diff/duyệt |
| `art_source/pixelorama/*.pxo` | Nguồn nghệ thuật chỉnh tay có layer/frame | **Bạn/Pixelorama** | **Không** cho generator ghi đè |
| `art_source/references/*` | Concept, nguồn tham chiếu + license | Bạn/AI tạo ảnh hợp lệ | Không tự xóa |
| `assets/sprites/.../*.png` | Sprite runtime đã duyệt cho Godot | Xuất từ `.pxo` hoặc generator nếu được duyệt | Không ghi đè tự động |
| `assets/vfx/.../*.png` | Sprite/spritesheet VFX runtime | Pixelorama / generator được duyệt | Không ghi đè tự động |
| `tools/asset_generator/output_preview/*` | PNG thử nghiệm | Generator | **Được** ghi đè, không xem là nguồn gốc nghệ thuật |

**Nguồn ưu tiên:** đối với asset **đã chỉnh tay**, `.pxo` được xem là bản gốc để chỉnh sửa tiếp; PNG dưới `assets/` là bản build từ `.pxo`. Với asset **thuần sinh bằng code chưa sửa tay**, script + recipe là nguồn gốc và PNG là file build. **Không để hai nguồn cùng âm thầm quản lý một PNG.**

### 6.3. Cấu trúc thư mục mở rộng đề xuất

Tổ chức bổ sung, **không làm mất** các thư mục project đã có:

```text
shinobi-evolution/
├── AGENTS.md
├── docs/
│   ├── GAME_DESIGN.md
│   ├── ARCHITECTURE.md
│   ├── SKILL_SYSTEM.md
│   ├── GRAPHICS_DESIGN.md        # FILE NÀY
│   └── DEVELOPMENT_ROADMAP.md
├── art_source/
│   ├── pixelorama/              # .pxo chỉnh tay, giữ trong Git
│   ├── references/              # reference + license.txt
│   └── palettes/                # .gpl/.json (tùy công cụ)
├── tools/
│   └── asset_generator/
│       ├── generate.py          # chỉ triển khai khi được giao task
│       ├── validate.py          # kiểm tra asset tự động
│       ├── recipes/
│       └── output_preview/      # output nháp, không dùng runtime
├── assets/
│   ├── sprites/
│   │   ├── characters/
│   │   └── enemies/
│   ├── tilesets/
│   ├── vfx/
│   └── ui/
└── project.godot
```

`tools/...` là **spec cho agent**, không phải tuyên bố các script đã có sẵn. Cấu trúc `assets/` giữ tương thích với `ARCHITECTURE.md`.

### 6.4. Recipe JSON ví dụ (schema đề xuất, không phải format Pixelorama)

```json
{
  "schema_version": "0.1",
  "asset_id": "ninja_base",
  "kind": "character",
  "target_format": "png_rgba",
  "frame_size": [64, 64],
  "directions": ["south", "west", "east", "north"],
  "animations": {
    "idle": { "frames": 4, "fps": 6 },
    "run": { "frames": 6, "fps": 10 }
  },
  "foot_anchor_px": [32, 55],
  "palette_id": "shinobi_default_v1",
  "style": "top_down_3_4_hd_pixel_art",
  "outfit": { "base": "dark_blue", "scarf": "burnt_orange" },
  "transparent_background": true,
  "allow_anti_aliasing": false,
  "output_status": "preview_only"
}
```

**Chưa được tự suy ra các frame idle/run thật từ JSON:** Antigravity phải viết renderer/generator có thể thực hiện yêu cầu và chứng minh kết quả; nếu không thể sinh chuyển động chất lượng thì tạo placeholder với nhãn rõ ràng để bạn chỉnh trong Pixelorama.

### 6.5. Metadata xuất ra để Godot và validator đọc

Ví dụ `ninja_base.meta.json` (schema nội bộ dự án, **không phải** format import mặc định của Godot hay Pixelorama):

```json
{
  "asset_id": "ninja_base",
  "source_type": "pixelorama_curated",
  "runtime_png": "res://assets/sprites/characters/ninja_base.png",
  "frame_size": [64, 64],
  "columns": 6,
  "rows": 4,
  "row_directions": ["south", "west", "east", "north"],
  "animations": { "run": { "frames_per_direction": 6, "fps": 10 } },
  "foot_anchor_px": [32, 55],
  "license": "original_project_art",
  "review_status": "approved"
}
```

**Ghi chú:** ví dụ metadata này mô tả riêng sprite sheet `run` (6 cột × 4 hàng); animation `idle` sẽ được xuất file khác hoặc theo atlas layout được quy định rõ. Không dùng một metadata `6×4` để đọc cả idle 4 frame và run 6 frame.

### 6.6. Ba hướng nhập vào Pixelorama

1. **PNG/spritesheet:** ưu tiên; Pixelorama `File > Open` → chọn import spritesheet nếu nhiều frame, khai báo đúng cột/hàng; sửa rồi lưu `.pxo`.
2. **SVG:** dùng khi AI tạo hình vector theo khối vuông; Pixelorama có thể import SVG thành raster, sau đó **kiểm xem có pixel lẻ/mờ**. Không dùng SVG làm runtime sprite mặc định.
3. **OpenRaster `.ora`:** hữu ích nếu generator/AI xuất nhiều layer có cấu trúc; phải kiểm thử bảo toàn layer với bản Pixelorama đang sử dụng.

Pixelorama có chức năng xuất PNG dạng sprite sheet và CLI trên desktop để tự động hóa xuất từ project đã lưu. Chỉ tích hợp CLI **sau** khi đã chốt quy ước layout và kiểm tra phiên bản thật. Không mở rộng ngay sang plugin AI trong Pixelorama.

---

## 7. Quy tắc đặt tên, xuất bản và kiểm soát thay đổi

### 7.1. Tên file

- Thư mục/file dùng `snake_case` ASCII; không viết khoảng trắng, không nhúng version bằng tên quá dài.
- Ví dụ: `ninja_base_idle_south.png`, `ninja_base_run_sheet.png`, `fire_projectile_small.png`, `forest_ground_32.png`.
- Các key asset **không tự thay thế** `skill_id` trong `data/skills/skills.json`; lập mapping riêng nếu có nhiều VFX dùng chung.
- Khi thay đổi pixel art đã được phê duyệt, không cập nhật source `.pxo` mà quên xuất lại PNG runtime tương ứng.

### 7.2. Không phá hủy asset thủ công

- Generator mặc định **chỉ viết `output_preview/`**. Muốn ghi vào `assets/` phải yêu cầu promotion/export **tường minh**, tạo diff và được bạn duyệt.
- Không tự ghi đè `.pxo`. Nếu asset có bản chỉnh tay thì **ưu tiên `.pxo`**, không chạy lại Python tạo PNG rồi ghi lên file runtime.
- Không auto xoá asset không sử dụng trừ khi có yêu cầu và danh sách được duyệt.
- Commit các asset được duyệt và recipe vào Git; bỏ qua file tạm lớn nếu được phân loại rõ; **không commit ảnh tham chiếu bên thứ ba không được phép lưu/phân phối**.

### 7.3. Mỗi asset cần có hồ sơ tối thiểu

`asset_id`, loại asset, pixel size, frame layout/FPS nếu có, nguồn tác giả/giấy phép, trạng thái `preview / curated / approved / deprecated`, nơi dùng trong Godot và ghi chú ảnh hưởng hiệu năng. Hồ sơ có thể ở JSON manifest hoặc bảng quản lý do Antigravity tạo, chưa cần database.

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
4. Không có file runtime được ghi đè ngoài luồng promotion được duyệt.
5. Không có tên file trùng `asset_id` hoặc tham chiếu runtime tới đường dẫn không tồn tại.
6. Đối với sprite pixel: phát hiện cảnh báo màu bán trong suốt/antialiasing không mong muốn (không đánh fail đối với hiệu ứng intentionally alpha).
7. Manifest có license/provenance cho asset bên ngoài và trạng thái duyệt.

Validator **không thể tự chấm được** nhân vật đẹp hay cử động tự nhiên; đó là tiêu chí xem trực quan trong Pixelorama, Godot và trên điện thoại.

---

## 9. Roadmap sản xuất đồ họa cho một người

Roadmap này **phụ thuộc** milestone kỹ thuật trong `DEVELOPMENT_ROADMAP.md`; không thêm trạng thái `DONE` vào roadmap chính khi chưa test.

| Mốc | Bộ đồ họa phải có | Không làm ở mốc này |
|---|---|---|
| **A0 — Visual baseline** | palette mẫu, 1 ninja 64×64 đứng, 1 icon, 1 tile 32×32, quy ước hướng/pivot | 10 gia tộc, 8 hướng |
| **A1 — Movement slice** | ninja idle/run 4 hướng, bóng chân, map rừng nhỏ, tường/đá | VFX ultimate |
| **A2 — Mobile slice** | joystick, nút đánh, HP/Chakra, camera/safe area, pixel quality test Android | HUD 100 kỹ năng |
| **A3 — Combat slice** | attack/cast/hurt, 2 quái, 3 hiệu ứng mẫu Hỏa/Lôi/Thế thân, loot icon | 162 kỹ năng |
| **A4 — Skill progression** | nút cây nhẫn thuật, locked/unlocked/available, icon T0–T2, 1 nhánh có tiến hóa VFX | tất cả thức tỉnh |
| **A5 — Vertical slice** | 3 gia tộc có nhận diện, 3 nguyên tố, 1 boss, bản đồ có khu boss/PvP | bản đồ vô tận |
| **A6 — Scale after tests** | sprite atlas, VFX quality profiles, style guide mở rộng, batching phù hợp | sản xuất đại trà trước khi stress test |

### Bộ thử nghiệm nên làm ĐẦU TIÊN

- `ninja_base_idle_south.png` — frame 64×64, một ninja **thiết kế gốc**.
- `ninja_base_run_sheet.png` — run 4 hướng × 6 frame, cùng foot anchor; nếu làm chưa đẹp, cho phép placeholder 2–4 frame trước.
- `forest_ground_32.png` — nhóm tile 32×32, có cỏ/đất/đường.
- `fire_projectile_small.png` — một đạn lửa rõ hướng đi, có telegraph riêng nếu là đòn khó né.
- `skill_fire_icon_32.png` — icon 32×32 phân biệt với nền.

**Cổng chấp thuận đầu tiên:** đặt ninja vào map Godot, chạy được bằng joystick trên Android; sprite không nhòe, chạy không rung, 1 hiệu ứng lửa nhìn rõ và không che màn hình. Khi đạt mới mở rộng asset generator và nhiều gia tộc.

---

## 10. Prompt/brief tiêu chuẩn giao Antigravity và Codex

### 10.1. Brief cho Antigravity — tạo generator đầu tiên

> Đọc `AGENTS.md`, `docs/ARCHITECTURE.md`, `docs/GAME_DESIGN.md` mục art direction và **toàn bộ** `docs/GRAPHICS_DESIGN.md`. Chỉ triển khai **A0**: tạo script Python 3 + Pillow để sinh một sprite ninja **thiết kế gốc** kích thước 64×64 và một `recipe.json`, xuất vào `tools/asset_generator/output_preview/`. Tạo validator kiểm kích thước/alpha/pivot và lệnh chạy có thể tái lập. **Không** ghi đè `assets/`, `.pxo` hoặc file người dùng sửa. Trước khi code nêu file sẽ thêm/sửa; sau khi chạy ghi lệnh, kết quả và nơi mở file để duyệt.

### 10.2. Brief cho Codex — review asset pipeline

> Review **chỉ đọc** diff của task asset generator. Kiểm tra: xử lý đường dẫn Windows/Unicode, không ghi đè asset curated, lặp lại cho kết quả ổn định (determinism), PNG RGBA/frame size, metadata và dependency Pillow, import Godot 4, rủi ro lộ license/asset bên ngoài. Ghi finding theo P0–P3 có file/dòng/kịch bản tái hiện. Không sửa code, không kết luận chất lượng mỹ thuật dựa vào validation script.

### 10.3. Khi cần sản xuất asset tiếp theo

Mỗi yêu cầu phải ghi tối thiểu:

```text
Asset ID / loại asset:
Mục đích gameplay và tình huống xuất hiện:
Reference hợp lệ / bảng màu:
Canvas size / tile size:
Hướng + animation + FPS:
Pivot / vị trí mặt đất:
Đầu ra cần tạo (recipe, preview PNG, .pxo, runtime PNG, metadata):
Quality target / thiết bị thử:
Cách nghiệm thu bằng mắt và trong Godot:
Những file AI KHÔNG được ghi đè:
```

---

## 11. Decision log — những gì đã chốt và đang mở

| ID | Trạng thái | Quyết định |
|---|---|---|
| GFX-001 | **CHỐT** | 2D HD Pixel Art, MOBA top-down 3/4, Android landscape |
| GFX-002 | **CHỐT** | Godot 4 + GDScript, VS Code, Antigravity phát triển, Codex review chỉ đọc |
| GFX-003 | **CHỐT** | Pipeline AI/code → PNG nháp → Pixelorama `.pxo` → PNG Godot; không overwrite art thủ công |
| GFX-004 | **CHỐT** | Solo-first, một ninja modular base, 4 hướng animation trước, VFX tái sử dụng |
| GFX-005 | **PROTOTYPE TARGET** | 32×32 tiles, 64×64 ninja frame, 640×360 world reference; phải test Android |
| GFX-006 | **PROTOTYPE TARGET** | 30/60 FPS theo phân khúc máy; không cam kết khi chưa đo |
| GFX-007 | **CHƯA CHỐT** | Bảng màu HEX chuẩn, style của trang phục/gia tộc, font và HUD cuối cùng |
| GFX-008 | **CHƯA CHỐT** | 4 hay 8 hướng ở bản phát hành; atlas/batching cuối cùng; mức độ glow theo thiết bị |
| GFX-009 | **CHỐT VỀ NGUYÊN TẮC** | Không sao chép asset của Naruto hay Wizard of Legend nếu không có quyền khai thác |

### 11.1. Cách duy trì tài liệu này

- `GAME_DESIGN.md` là nguồn chính cho **cảm giác chơi / rules**, `SKILL_SYSTEM.md` cho **kỹ năng / unlock**, file này cho **hình ảnh / pipeline asset**, `ARCHITECTURE.md` cho **Godot implementation**.
- Khi Antigravity muốn sửa tiêu chuẩn pixel/pivot, asset folder hoặc shader policy, phải đề xuất diff tài liệu và được duyệt; không tự sửa im lặng.
- Khuyên **bổ sung `docs/GRAPHICS_DESIGN.md` vào bảng tài liệu phải đọc trong `AGENTS.md` khi task liên quan sprite, UI, map, VFX, animation hoặc asset generator**. Việc cập nhật `AGENTS.md` là task riêng có duyệt; file mới này chưa tự sửa file cũ.
- Các link kỹ thuật nên tham khảo: [Pixelorama Import](https://pixelorama.org/user_manual/Import/), [Pixelorama Save/Export](https://pixelorama.org/user_manual/save_and_export/), [Pixelorama CLI](https://pixelorama.org/user_manual/cli/), [Godot – Multiple Resolutions](https://docs.godotengine.org/en/stable/tutorials/rendering/multiple_resolutions.html).

---

**Tiêu chuẩn thành công:** sau khi đọc file này, một agent phải biết **tạo asset gì, tạo ở đâu, xuất định dạng nào, không được ghi đè file nào, đưa vào Godot ra sao, cần test gì trên Android**; còn bạn có thể kiểm tra nhanh bằng mắt và duyệt từng asset trước khi đưa vào game.
