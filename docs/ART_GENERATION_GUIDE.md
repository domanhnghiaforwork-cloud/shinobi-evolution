# ART_GENERATION_GUIDE.md — Prompt và quy trình dùng generate_image

**Phiên bản:** 1.0 • **Ngày:** 2026-10-16 • **Người thực hiện:** Antigravity. **Công cụ tạo hình:** `generate_image` tích hợp sẵn trong Antigravity.

## 1. Hợp đồng sử dụng công cụ

Đọc [GRAPHICS_DESIGN](GRAPHICS_DESIGN.md) và [ANTIGRAVITY_AUTOPILOT](ANTIGRAVITY_AUTOPILOT.md) trước sản xuất. `generate_image` tạo concept, sprite, tile, icon và texture VFX; code chỉ xử lý ảnh kỹ thuật, đóng gói và dựng hành vi trong Godot. Không thay yêu cầu này bằng Python vẽ ninja hoặc tải asset pack bên ngoài. Pixelorama là công cụ sửa nguồn thủ công **tùy chọn**, không là cổng phải chờ người dùng thao tác.

Tài liệu chính thức liệt kê các trường `Prompt`, `ImageName`, `ImagePaths` tùy chọn: [Antigravity supported tools](https://antigravity.google/docs/hooks#supported-tools). Kiểm schema tool thực tế của phiên; không tự bịa API/CLI `generate_image`, không cài tool trùng tên hoặc gọi một script shell thay cho tool tích hợp.

Ví dụ cấu trúc gọi tool — phải thay prompt đầy đủ và đường dẫn thật trước gọi:

```json
{
  "Prompt": "[MASTER PROMPT đã điền toàn bộ biến + JOB cụ thể + NEGATIVE PROMPT]",
  "ImageName": "ninja_base_run_south_v001",
  "ImagePaths": ["[đường dẫn tuyệt đối đến ảnh mẫu đã tồn tại]"]
}
```

Khi tạo style board đầu tiên chưa có reference thì bỏ `ImagePaths`. Khi tạo biến thể/frame tiếp theo phải dùng reference identity đã chọn qua trường tool hỗ trợ, không chỉ nhắc một filename trong prompt. Output có thể nằm trong artifact folder của Antigravity: lấy đúng đường dẫn tool trả, kiểm file tồn tại rồi copy vào nguồn dự án; không đoán tool đã viết thẳng `assets/`.

Không giả có ảnh nếu tool lỗi/quota hết. Được sửa prompt, giảm lô và thử lại có lý do, không lặp mù. Tiếp tục code/test không phụ thuộc; nếu vẫn không tạo được art bắt buộc, ghi blocker cụ thể, không gọi hình khối placeholder là art hoàn chỉnh.

## 2. Style card dùng chung

| Thuộc tính | Chuẩn khởi đầu cho bản chơi thử |
|---|---|
| Thể loại | 2D HD pixel art; world top-down 3/4, thấy mặt trước/đỉnh đầu theo hướng; không isometric kim cương |
| Nội dung | Ninja thiết kế gốc, nội bộ gắn scope Uchiha/Hỏa; không sao chép mặt, trang phục, huy hiệu hoặc ảnh Naruto |
| Kích thước logic | Character 64×64/frame, tile 32×32, icon 32×32; world tham chiếu 640×360 |
| Foot anchor | Nhân vật đứng/chạy đặt chân tại (32,55), tính từ góc trên trái frame, cùng scale mọi frame |
| Hướng | `south`, `west`, `east`, `north`; full body, hướng mặt và chuyển động khớp nhau |
| Chất pixel | Cạnh sắc, cụm pixel có chủ đích, outline 1 logical pixel, shading 2–3 mức, không anti-alias/blur |
| Ánh sáng | Ánh sáng trên-trái nhất quán; shadow gameplay tách riêng bằng Godot |
| Palette | Outline #171923; navy #26334F; skin #D9A066/#FFD39A; accent #A53637; fire #F47B35/#FFD166; illusion #9B7BD4; grass #425943/#667C4C |
| Nền | Character/icon/VFX PNG RGBA trong suốt thật; tile ground phủ kín, seamless khi yêu cầu |
| UI | Godot vẽ text/số/cooldown và nút hoạt động; ảnh chỉ làm icon/panel skin, không tạo cả HUD thành một bitmap |

Lập một style board và một ninja identity master trước; tự kiểm silhouette/palette/tỉ lệ ở kích thước game rồi dùng làm reference cho cả batch. Không cần dừng xin duyệt style board. Đây là style khởi đầu trong art direction đã chọn; ghi thay đổi có lý do vào manifest, giữ nhận diện đồng nhất.

## 3. Master prompt bắt buộc

Prompt tiếng Anh dưới đây dùng chung cho model tạo ảnh. Chỉ thay biến, không bỏ camera, scale, identity hoặc output constraints. Trước gọi, kiểm không còn chuỗi `{...}` chưa điền.

```text
PROJECT: Shinobi Evolution, original-art 2D mobile survival prototype.
ASSET ID: {asset_id}. REVISION: {revision}.
JOB: {asset_kind_and_exact_gameplay_purpose}.

REFERENCE CONTRACT:
Use the attached identity/style references as visual constraints.
Preserve {identity_traits_to_preserve}: silhouette, proportions, outfit,
palette, hair, face, handedness and equipment. Do not redesign the subject.
For a new identity, follow the project style card below and establish one
consistent subject for all requested frames.

STYLE:
Production game pixel art, crisp intentional pixel clusters, limited
palette, 1-logical-pixel outline, 2-3 shading steps, top-left lighting.
Camera: {camera_and_facing}. World assets match 2D top-down three-quarter
gameplay; UI icons are flat orthographic symbols, not scene illustrations.
No side-scrolling character view, diamond-grid isometric or 3D render.
Palette and material restrictions: {palette_and_materials}.
Subject: {original_subject_description}.

TECHNICAL COMPOSITION:
Logical canvas {logical_width} x {logical_height} pixels.
{layout_and_frame_count}. {frame_dimensions_and_order}.
Keep each subject fully inside its cell with the same scale and framing.
Character foot anchor: {foot_anchor_or_not_applicable}.
Background: {true_transparency_or_opaque_tile_requirement}.
Output only the requested asset, no presentation board, labels or mockup.
If output is higher resolution, use a clean integer pixel enlargement of
the logical grid, not added painted microdetails. Do not crop feet,
weapons, glow, telegraph edges or the first/last animation cell.

ACTION / READABILITY:
{poses_or_animation_frames_or_seamless_edges}.
At native game size the viewer must read {silhouette_or_gameplay_signal}.
Danger area and decorative glow must remain visually distinct.

NEGATIVE CONSTRAINTS:
No text, letters, numbers, logo, watermark, franchise emblem, recognizable
copyrighted character, UI screenshot, photorealism, painted concept art,
3D model, anti-aliasing, soft brush, blur, bloom wash, perspective drift,
inconsistent anatomy, duplicate poses presented as animation, cut-off
limbs, baked checkerboard, grid labels, contact shadow baked into sprites.
```

Tên job phải nói rõ **asset dùng ở đâu**, hình dáng/tương phản cần truyền đạt và định dạng đầu ra. Không gửi prompt chung kiểu “vẽ ninja đẹp” rồi dùng kết quả như sprite runtime.

## 4. JOB mẫu đã điền

Các JOB sau đi cùng MASTER PROMPT và reference thực tế; không gửi riêng JOB rồi bỏ ràng buộc chung.

### A. Ninja identity master

```text
ASSET ID: ninja_base_identity. REVISION: v001.
JOB: One original playable ninja sprite, neutral standing pose, facing south.
CAMERA: top-down three-quarter gameplay, full body visible, head seen slightly
from above; character faces the lower edge of the image.
SUBJECT: a compact adult ninja, short dark hair, plain navy tunic, muted red
waist cloth, neutral arm wraps and sandals; symmetrical practical equipment.
No headband emblem, no clan crest, no named anime character likeness.
LAYOUT: one 64x64 logical frame. Feet anchored at (32,55). Transparent RGBA.
READABILITY: distinct head/torso/arms/legs at 1x, clear silhouette on green
forest terrain. No attack, weapon swing, smoke or environmental background.
```

Giữ identity output làm ảnh mẫu cho hướng/frame kế tiếp. Nếu ảnh sinh không thể thu về 64×64 mà còn đọc được, sửa prompt/reference và sinh lại; không chấp nhận một concept lớn chỉ vì resize được.

### B. Một hàng chạy, một hướng

```text
ASSET ID: ninja_base_run_south. REVISION: v001.
JOB: A four-frame looping running animation of the attached ninja identity.
CAMERA AND FACING: south, top-down three-quarter, same camera as reference.
LAYOUT: exactly one horizontal row of 4 equal 64x64 logical cells, total
256x64 logical pixels, left-to-right frame order, no gutters or labels.
POSES: 1 left foot contact, 2 passing, 3 right foot contact, 4 passing.
Keep the character centered at the same (32,55) foot anchor in each cell.
Run in place; no horizontal drift across cells. Keep body volume, face,
outfit, color and limb lengths constant; genuine alternating leg/arm poses.
Transparent RGBA; no motion blur or streaks hiding the legs.
```

Sau khi đạt south, lặp JOB với `west`, `east`, `north`, sửa mô tả hướng mặt tương ứng và truyền master + frame hướng đã chọn. Không sinh một sheet chứa nhiều hướng/animation mơ hồ cùng lúc. Nếu tool không giữ grid, chuyển sang sinh từng pose có reference rồi đóng sheet bằng code; không stretch một ảnh méo vào grid để qua validator.

### C. Tile nền rừng

```text
ASSET ID: forest_ground_01. REVISION: v001.
JOB: One seamless repeating 32x32 logical ground tile for a ninja forest.
CAMERA: flat ground viewed from top-down three-quarter gameplay.
PALETTE: muted #425943 and #667C4C with dark soil accents.
COMPOSITION: opaque ground filling the entire square; subtle small grass
clusters and soil variation. No trees, rocks, characters, shadows or text.
All four edges must tile without visible seams. Keep contrast low enough
for actors, red-orange fire telegraphs and purple illusion effects to read.
```

Đóng preview lặp 3×3 để kiểm seam. Cây/đá/prop là asset riêng có alpha, không vẽ collision vào texture; Godot quản lý collision theo metadata/scene.

### D. Icon kỹ năng

```text
ASSET ID: icon_fire_ball. REVISION: v001.
JOB: A 32x32 logical pixel-art skill icon: one compact orange fireball with
a short directional tail, readable on a dark mobile skill button.
COMPOSITION: centered silhouette, transparent background, 2 logical pixels
of safe padding, no button frame, no badge, no letters or numerals.
Use #F47B35 and #FFD166 with #171923 outline. Strong shape at 1x.
```

Tạo một icon cho mỗi khả năng cần phân biệt; không yêu cầu AI viết tên hoặc số cooldown lên icon. Khung nút/disabled/cooldown mask do UI xử lý.

### E. Texture VFX và vùng cảnh báo

```text
ASSET ID: fire_impact_small. REVISION: v001.
JOB: Four distinct stages of a small fire impact: ignition, expansion,
peak, dissipation. One horizontal row, four equal 64x64 logical cells.
STYLE: crisp red-orange pixel clusters, brighter center, sparse edges,
transparent background. Stable effect origin at cell center; no character.
Do not paint a full-screen white flash or an opaque circular floor.
The damage telegraph is a separate engine-drawn shape; this texture is
decorative feedback and must not imply a larger collision radius.
```

VFX Ảo thuật dùng shape/palette riêng, không chỉ đổi màu lửa. Thế thân cần dấu thanh tẩy/tan biến đọc rõ nhưng không giống khiên miễn sát thương. Vùng bo/telegraph chính xác vẽ bằng Godot từ dữ liệu hit/zone, không lấy biên tranh AI làm collider.

## 5. Animation và batch tối thiểu

Ninja bốn hướng, mỗi animation xuất file/metadata riêng:

| Animation | Frame khởi đầu / FPS | Điều kiện |
|---|---|---|
| idle | 2 / 4 | Hai pose có khác biệt nhẹ, không nhảy pivot |
| run | 4 / 8 | Nhìn thấy luân phiên chân/tay, không trượt pose đứng |
| attack | 3 / 10 | anticipation → strike → recovery; damage theo domain |
| cast | 3 / 8 | chuẩn bị → tung thuật → kết thúc |
| hurt | 1 / giữ ngắn | feedback nhận hit, không đổi hitbox theo pose |
| death | 4 / 6, không loop | kết thúc ở pose chết; cleanup theo match |

Đây là profile art prototype, agent được điều chỉnh sau kiểm rendered và ghi metadata; không thay timing hit/cooldown chỉ vì animation khác số frame. Có thể mirror west/east nếu thiết kế thực sự đối xứng và đã kiểm, phải ghi `mirror_of`; không nói đã sinh bốn hướng riêng khi dùng mirror.

Batch: identity → idle/run → đưa vào arena → attack/cast/hurt/death → hai quái → boss → ground/props → icon → VFX. Hoàn thành lô nhỏ dùng được trước khi sinh lô lớn. Reuse sprite qua behavior của clone, không tạo một ảnh mới cho mỗi entity instance.

Bản bàn giao phải có ninja animated, hai loại quái và boss phân biệt, ground/obstacle/loot, icon khả năng thực sự dùng và VFX Hỏa/Ảo/Thế thân. Node ngoài scope không cần sản xuất art. Nút trống/disabled là trạng thái UI thật, không phải lý do sinh 162 icon.

## 6. Lưu nguồn, xử lý kỹ thuật và promotion

```text
art_source/prompts/<asset_id>/<revision>.json   # prompt đầy đủ, references, tool result
art_source/generated/<asset_id>/<revision>/   # output gốc, giữ nguyên
art_source/previews/                          # contact sheet / alpha / tiling preview
art_source/pixelorama/                        # chỉ khi có nguồn sửa tay, được bảo vệ
assets/sprites/characters/                    # PNG runtime đã kiểm
assets/sprites/enemies/
assets/tilesets/
assets/vfx/
assets/ui/icons/
data/art/asset_manifest.json                  # map asset → source/runtime/animation
tools/art_pipeline/                          # xử lý PNG, atlas, validate; không thay tool tạo hình
```

Không giả các đường dẫn này đã tồn tại. Antigravity tạo theo batch khi code. Manifest tối thiểu: `asset_id`, `revision`, `source_tool=generate_image`, full prompt path, reference paths/hash, raw output path/hash, actual dimensions/mode, runtime path, frame size/count/layout/FPS, foot anchor, mirror info, nơi dùng, check result và `review_status=agent_validated` hoặc `needs_fix`. Chỉ ghi `owner_accepted` sau nghiệm thu thật. Model/seed chỉ ghi nếu tool trả; không hứa sinh lại ảnh giống từng pixel.

Được crop, pad, giảm kích thước nearest-neighbor, kiểm alpha, giảm palette có kiểm soát, tách frame, ghép atlas, tạo preview và metadata. Không làm méo tỉ lệ hoặc tự suy các pose không có. Nếu ảnh nền không alpha, ưu tiên edit lại bằng `generate_image` với reference; chỉ xử lý nền bằng code khi nền đồng nhất và không cắt mất pixel chủ thể, rồi kiểm halo trên nền sáng/tối.

Antigravity tự promote asset do mình tạo sau structural + visual checks và cập nhật mapping, không chờ người dùng duyệt từng PNG. Giữ raw/revision trước đó để phục hồi; không overwrite nguồn người dùng chỉnh tay, `.pxo` hoặc asset `owner_locked`. Khi cần thay asset bị khóa, tạo variant đường dẫn mới và ghi mapping/diff, không xóa bản gốc.

## 7. Checklist tự kiểm trước khi dùng

1. File output thật tồn tại, decode được, kích thước/mode/alpha đúng; không có checkerboard được vẽ vào nền.
2. Xem 1× và 4×: silhouette rõ, không viền mờ/halo, camera/palette/identity nhất quán.
3. Sheet chia đúng cell, frame count khớp metadata, pose khác nhau thật; kiểm foot anchor và bbox từng frame, không cắt/méo chi.
4. Preview animation loop đúng tốc độ, không rung/đổi kích cỡ; chưa xem preview thì chưa ghi animation visual PASS.
5. Tile 3×3 không seam; icon rõ trên nút nhỏ; VFX không che telegraph hoặc tạo cảm giác miễn damage.
6. Import vào Godot, kiểm nearest world texture, scale và layer/y-sort; chạy scene rendered và lưu screenshot/video thật có asset.
7. Không tạo script/scene reference mất file; manifest còn truy được raw/prompt/reference; chưa có human acceptance thì không ghi approved-by-owner.

Lỗi structural phải sửa trước import. Lỗi identity/pose/perspective phải chỉnh prompt/ref và sinh lại; validator PNG không thể chứng minh asset đẹp. Sau hai lần sửa không cải thiện, đổi cách chia batch/reference thay vì gửi cùng prompt mãi. Nếu quota hết, lưu blocker và tiếp tục phần độc lập; không âm thầm chuyển sang generator vẽ hình hoặc đợi người dùng sửa Pixelorama từng asset.
