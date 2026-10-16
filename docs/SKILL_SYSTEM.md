# SKILL_SYSTEM.md — Đồ thị nhẫn thuật, chakra và kết hợp

**Phiên bản:** 1.0 • **Ngày:** 2026-10-16 • **Trạng thái:** `DESIGN_SPEC / NOT YET IMPLEMENTED`.

**Dữ liệu đi kèm:** `../data/skills/skills.json` (tính từ thư mục docs: `../data/skills/skills.json`). Dữ liệu kế thừa thiết kế `naruto_skill_graph_v1.json`: **162 node / 29 tree / 12 synergy**. Đây là **đồ thị thiết kế**, chưa phải 162 ability hoàn thiện.

> **Lore vs gameplay:** `source_label=canon_adapted` là khái niệm/tên có nguồn Naruto nhưng yêu cầu, sát thương và lộ trình trong trận đã được thích nghi; `source_label=game_design` là nội dung sáng tạo riêng. Không tự khẳng định kỹ năng mới xuất hiện trong nguyên tác. Việc sử dụng IP có bảo hộ cần giải quyết trước phát hành.

## 1. Khái niệm và các trục phân loại KHÔNG đồng nhất

**Đồ thị kỹ năng** là tập node, cạnh tiên quyết `AND/OR`, gate điều kiện, ngoại lệ và cầu nối lai. Không phải cây tuyến tính: một node có thể mở nhiều hướng; các nhánh khác nhau có thể gặp nhau để tạo build.

| Khái niệm | Ví dụ | Sử dụng |
|---|---|---|
| **Nhóm thuật** | Ninjutsu / Taijutsu / Genjutsu / phong ấn / y / triệu hồi | loại gameplay hoặc archetype |
| **Chakra nature** | FIRE, WIND, LIGHTNING, EARTH, WATER | tương khắc, trigger môi trường |
| **Rank lore** | E, D, C, B, A, S hoặc null | thông tin độ khó; **không** quyết định tier/damage |
| **Tier game** | T0..T5 | mốc level tối thiểu và chi phí mở |
| **Nguồn năng lực** | gia tộc, Hiden, Kekkei Genkai, huấn luyện, bí quyển | điều kiện học hợp lệ |
| **Kiểu node** | root, unlock, passive, active, ultimate, bridge | cách trang bị/thực thi (chưa gắn cho tất cả node) |
| **Combat role** | sát thương, phòng thủ, trinh sát, cơ động, khống chế, hỗ trợ | hướng chiến thuật/build |

**Lore restrictions bắt buộc:**

- **Sharingan** và **Byakugan** là huyết kế, không phải cuộn ai cũng học được; cùng mang Mangekyō chưa đồng nghĩa cùng năng lực.
- **Hiden** của Nara/Yamanaka/Akimichi là truyền dạy có gate hợp lệ, không hoàn toàn khóa vào huyết thống như Kekkei Genkai.
- **Hỏa + Phong** khuếch đại lửa, **Thủy + Lôi** dẫn điện, **Thổ + Thủy** làm bùn: là tương tác game; **không** tạo Mộc Độn/Băng Độn chỉ từ nguyên tố.
- **Mộc Độn** (trường hợp hiếm kiểu Hashirama), Băng Độn, Từ Độn, Phí Độn, Trần Độn yêu cầu gate riêng.
- **Tiên thuật** cần trải qua training/energy gate, **Vĩ thú** là tình huống riêng, không phải nút clan phổ thông.
- **Bát Môn** cần trade-off, không cho trạng thái tăng chỉ số vĩnh viễn; **Ảnh Phân Thân** chia tài nguyên và giới hạn entity.

## 2. Thuộc tính chakra và nguyên lý khắc chế

Chu trình được dùng trong game:

```text
HỎA > PHONG > LÔI > THỔ > THỦY > HỎA
```

`>` biểu thị lợi thế khi **hai chakra nature va chạm trực tiếp**, không phải sát thương nhân vô điều kiện cho mọi hit. Hệ khắc phải mang tính situational và có counterplay; tránh chọn một hệ là tự thắng đối phương.

| Nature | Vai trò tiêu biểu | Khắc chế môi trường | Root ID |
|---|---|---|---|
| FIRE | AoE, burn, ép địa hình | nước dập lửa | `FIRE_ROOT` |
| WIND | hướng/đẩy, lưỡi gió, mobility | lửa tận dụng gió | `WIND_ROOT` |
| LIGHTNING (ID `LIGHT_`) | burst, điện lan, dash | cần wet area để chain mạnh | `LIGHT_ROOT` |
| EARTH | wall, trap, chịu đòn | bị xuyên/phá tùy thuật | `EARTH_ROOT` |
| WATER | zone, mist, prison, support | có thể bị điện lan | `WATER_ROOT` |

**Lưu ý ID:** dữ liệu gốc dùng prefix `LIGHT_` cho **Lôi**, không tự đổi ID thành `LIGHTNING_` nếu chưa có migration. Trong `element_tokens`, `LIGHT` là token data cũ được chuẩn hóa thành `LIGHTNING` ở runtime. Không đồng nhất với ánh sáng/light rendering.

## 3. Tier/kinh tế/khoảng trống gameplay

| Tier | Level tối thiểu | SP | Ryō đề xuất | Ý nghĩa |
|---|---:|---:|---:|---|
| T0 | 1 | 0 | 0 | nền tảng có sẵn khi spawn |
| T1 | 1 | 1 | 100 | khai mở root/chuyên môn/gia tộc |
| T2 | 4 | 1 | 180 | chiến đấu nền |
| T3 | 8 | 1 | 280 | chuyên sâu, có thể có gate huấn luyện/loot |
| T4 | 12 | 1 | 450 | kết hợp hoặc chuyên môn mạnh |
| T5 | 17 | 1 | 700 | tối thượng/thức tỉnh giới hạn |

- **Max level 20**, ngân sách **12 SP** cho một trận đủ dài. T0 được grant tự động theo chính sách mặc định (6 node gốc). Chi phí là thiết kế tham khảo; **chưa phải đủ logic combat**.
- Cần tránh trường hợp player level đủ nhưng thiếu SP do đường tốn tài nguyên không cân đối. UI phải cho xem tổng chi phí **đường đi tới một node**.
- Chỉ **1 ultimate** active, 4 active, 3 passive, 1 clan trait, 1 ninja tool và 1 **Thế thân riêng** (sau khi hệ loadout ra đời).
- Có thể đặt 2 nguyên tố chính; nguyên tố thứ ba phải là sự kiện hiếm hạn chế. Gốc `FIRE_ROOT` ... `WATER_ROOT` **không có nghĩa** cùng người có thể mua cả năm theo mặc định.
- Các node có `implementation_status=design_only` **chưa thể cast**; chỉ khi hệ runtime đã định nghĩa archetype, cost, cooldown, hit shape và animation mới đặt trạng thái triển khai tương ứng.

## 4. Hệ thống gia tộc (10 gia tộc target)

### 4.1 Bảng tổng quan

| Clan | Gate gốc | Vai trò cốt lõi | Đường lai mở | Counterplay |
|---|---|---|---|---|
| Uchiha | huyết kế Sharingan | phản công, ảo thuật, shuriken | Thể thuật / Hỏa / Lôi | bị che tầm nhìn, tốn chakra |
| Hyūga | huyết kế Byakugan | điểm huyệt, chống tiếp cận, cận chiến | Lôi, phòng thủ | kite / tấn công từ xa |
| Nara | Hiden truyền bóng | giữ vùng, bẫy | Phong ấn | né bóng / áp sát caster |
| Yamanaka | Hiden tâm thuật | control, tình báo, teamwork | Trinh sát | body gốc dễ bị tấn công |
| Akimichi | Hiden bội hóa | tank, AoE cận chiến | Thổ, hồi phục | mục tiêu lớn, dễ kiting |
| Aburame | cộng sinh côn trùng | hút chakra, scout | Y thuật, Thổ | AoE / thiêu đốt |
| Inuzuka | nhẫn khuyển/truyền thụ | tracking, dive | Phong | chia tách đôi người/chó |
| Uzumaki | sinh lực, truyền thống phong ấn | support, seal, tank | Y thuật, kết giới | thiếu cơ động |
| Yuki | huyết kế Băng | zone, ngăn đường | Thủy, Ảo thuật | phá băng/kết giới |
| Hōzuki | hóa lỏng dòng máu | né, di chuyển, đánh theo nước | Thủy | Lôi Độn, phong ấn |

**Clans không tự kế thừa mọi kỹ năng của người nổi tiếng:** Sasuke dùng Thiên Điểu nhưng nó không biến thành huyết kế Uchiha; không cho mọi Uchiha mặc định Hắc Viêm/Kamui; không cho mọi Uzumaki dây xích. Thiên phú và gói thức tỉnh có gate độc lập.

### 4.2 Cây gia tộc theo ID thực tế

**Uchiha – 11 node**

```text
UCH_EYE1 → UCH_EYE2 → UCH_EYE3
                            ├─ UCH_GEN (ảo thuật)
                            ├─ UCH_COPY (copy kỹ năng phổ thông, giới hạn)
                            └─ UCH_MANGEKYO (T5, nhiệm vụ + huyết kế)
                                  ├─ UCH_SUSANOO (điều kiện 2 mắt / gói)
                                  ├─ UCH_FLAME (gói Hắc viêm)
                                  └─ UCH_SPACE (gói Không gian; loại trừ Hắc viêm)
UCH_FIRE (truyền thống Hỏa) → kết nối FIRE_ROOT/FIRE_BALL theo thiết kế node
UCH_SHURIKEN → lai với Thể thuật/Nhẫn cụ
```

Đồ thị ASCII mô tả hướng, **không thay thế các trường `requires_all` trong JSON**. Gói Mangekyō phải chỉ xuất hiện qua nhiệm vụ thức tỉnh hư cấu, không yêu cầu làm hại người chơi khác. Các gói nhãn thuật loại trừ lẫn nhau cần **quy tắc exclusivity máy** trước khi mở runtime.

**Hyūga – 7 node**

```text
HYG_EYE → HYG_GENTLE → HYG_POINT → HYG_64
                          ├─ HYG_ROTATION / HYG_AIRPALM
                          └─ HYG_LION (gate tu luyện riêng)
```

Lai mục tiêu `FUSE_BYAKU_LIGHT` cần `HYG_POINT` + Lôi hợp lệ. Nhu Quyền khóa chakra theo hit có báo rõ, thời gian và khả năng giải.

**Nara – 6 node**

```text
NARA_SHADOW → NARA_RANGE → NARA_BIND → NARA_NECK / NARA_SEW → NARA_MULTI
```

Lai `FUSE_SHADOW_TRAP` = thuật bóng + `SEAL_TRAP`. Bóng là vùng gameplay server xác nhận; không giả lập ánh sáng động để tính hit thật.

**Yamanaka – 5 node:** `YAM_MIND`, `YAM_SIGNAL`, `YAM_SWITCH`, `YAM_DISTURB`, `YAM_NETWORK`. Chuyển tâm có điểm yếu thân gốc, network ally communication có giới hạn.

**Akimichi – 5 node:** `AKI_EXPAND`, `AKI_PART`, `AKI_ROLL`, `AKI_MEGA`, `AKI_BUTTERFLY`. Bội hóa tăng hitbox và bị định vị dễ hơn, không miễn sát thương.

**Aburame – 5 node:** `ABU_INSECT`, `ABU_DRAIN`, `ABU_SCOUT`, `ABU_COCOON`, `ABU_SWARM`. Đàn trùng là **một vùng/cluster có entity budget**, không spawn 500 con độc lập.

**Inuzuka – 5 node:** `INU_PARTNER`, `INU_FOUR`, `INU_CLONE`, `INU_FANG`, `INU_WOLF`. Nhẫn khuyển có HP/AI budget riêng và tình trạng tách chủ.

**Uzumaki – 5 node:** `UZU_VITAL`, `UZU_SEAL`, `UZU_REGEN`, `UZU_CHAIN`, `UZU_BARRIER`. `UZU_CHAIN` là tương thích huyết thống hiếm, không auto cho mọi người mang họ Uzumaki.

**Yuki – 4 node:** `YUKI_ICE`, `YUKI_NEEDLE`, `YUKI_WALL`, `YUKI_MIRROR`. `YUKI_ICE` yêu cầu huyết kế; chỉ có `WATER_ROOT + WIND_ROOT` là chưa đủ.

**Hōzuki – 4 node:** `HOZ_LIQUID`, `HOZ_WATERGUN`, `HOZ_ESCAPE`, `HOZ_BODY`. Hóa lỏng bị Lôi khắc chế rõ; không cho tránh mọi kỹ năng vô hạn.

## 5. Nhóm chung / nguyên tố / chuyên môn

### 5.1 Nền tảng — 14 node

- **T0 mặc định:** `BASE_CHAKRA`, `BASE_MOVE`, `BASE_SUB`, `BASE_TRANSFORM`, `BASE_CLONE`, `BASE_WEAPON`.
- **Di chuyển:** `BASE_WALL`, `BASE_WATERWALK`, `BASE_DODGE`.
- **Phân thân:** `BASE_SHADOWCLONE` (Ảnh Phân Thân cần cuộn/training), `BASE_MULTI_CLONE` (cấm thuật, cap entity/cost).
- **Nhẫn cụ/trinh sát:** `BASE_TOOLWIRE`, `BASE_THROW`, `BASE_SENSOR`.

T0 chứa sáu node **nhận miễn phí**, nhưng trên HUD ban đầu không nhất thiết có sáu nút riêng; chúng có thể là tutorial/action context.

### 5.2 Ngũ Độn — mỗi nhóm 7 node

| Hệ | Root | Sát thương | Control / Zone | Phòng thủ / Cơ động |
|---|---|---|---|---|
| Hỏa | `FIRE_ROOT` | `FIRE_BALL`, `FIRE_PHOENIX`, `FIRE_DRAGON` | `FIRE_WALL`, `FIRE_ZONE`, `FIRE_TRAP` | bẫy và vị trí |
| Phong | `WIND_ROOT` | `WIND_BLADE`, `WIND_VACUUM`, `WIND_SHURIKEN` | `WIND_GUST`, `WIND_STORM` | `WIND_STEP` |
| Lôi | `LIGHT_ROOT` | `LIGHT_SPARK`, `LIGHT_CHIDORI`, `LIGHT_RAIRI` | `LIGHT_CHAIN`, `LIGHT_FIELD` | `LIGHT_ARMOR` |
| Thổ | `EARTH_ROOT` | `EARTH_PROJECTILE`, `EARTH_GRAB` | `EARTH_BOG`, `EARTH_FORT` | `EARTH_WALL`, `EARTH_MOLE` |
| Thủy | `WATER_ROOT` | `WATER_BULLET`, `WATER_DRAGON` | `WATER_PRISON`, `WATER_MIST`, `WATER_SURGE` | `WATER_WALL` |

**Chiêu dụ người chơi:** mỗi nguyên tố có thể nâng theo `damage / control / mobility-defense`. Không buộc mỗi người học toàn bộ 7 node của hệ đó. Học nhiều hệ tạo được synergy, nhưng tiêu tốn SP nên phải đánh đổi.

### 5.3 Chuyên môn — 31 node (tổng)

| Nhóm | ID node chính | Đặc trưng |
|---|---|---|
| Thể thuật (6) | `TAI_ROOT`, `TAI_COMBO`, `TAI_LOTUS`, `TAI_GATE_1`, `TAI_GATE_3`, `TAI_GATE_6` | combo, dash, Bát Môn có hậu quả |
| Ảo thuật (4) | `GEN_ROOT`, `GEN_MIRAGE`, `GEN_SNARE`, `GEN_DOMAIN` | đánh lừa, khống chế có cách giải |
| Y thuật (5) | `MED_ROOT`, `MED_PALM`, `MED_ANTIDOTE`, `MED_PRECISION`, `MED_FIELD` | sustain, giải độc, hỗ trợ |
| Phong ấn (4) | `SEAL_ROOT`, `SEAL_TRAP`, `SEAL_BARRIER`, `SEAL_SUPPRESS` | bẫy, áp chế chakra, khu vực |
| Khôi lỗi (4) | `PUP_ROOT`, `PUP_WEAPON`, `PUP_POISON`, `PUP_DUO` | summon logic, vũ khí, độc |
| Triệu hồi (5) | `SUM_ROOT`, `SUM_TOAD`, `SUM_SNAKE`, `SUM_SLUG`, `SUM_GREAT` | pact; chọn ít nhất 1 loài cho đại triệu hồi |
| Hình thái chakra (3) | `SHAPE_ROOT`, `SHAPE_RASENGAN`, `SHAPE_RASENSHURIKEN` | Rasengan không thuộc độc quyền Uzumaki |

Các nguyên tác như `SHAPE_RASENSHURIKEN` vẫn yêu cầu cửa huấn luyện; game cần gate thiết kế riêng thay vì tự động mở khi người chơi có một hệ.

### 5.4 Nhánh đặc biệt — 10 node

| Cụm | IDs | Khóa bắt buộc |
|---|---|---|
| Tiên thuật (3) | `SAGE_ROOT`, `SAGE_MODE`, `SAGE_FROGKATA` | training/năng lượng tự nhiên/khế ước phù hợp |
| Cấm thuật (1) | `FORBIDDEN_SEAL` | chìa khóa sự kiện và trade-off |
| Huyết kế hiếm (4) | `RARE_WOOD`, `RARE_MAGNET`, `RARE_BOIL`, `RARE_DUST` | huyết kế tương thích, không từ mix nguyên tố |
| Không gian (1) | `RARE_SPACE` | nhiệm vụ/biểu tượng thời-không hiếm |
| Vĩ thú (1) | `RARE_JINCHU` | sự kiện/chế độ riêng, không auto ai cũng học |

**Giới hạn độ hiếm trong chế độ chính:** các nhánh hiếm ảnh hưởng cân bằng T5; có thể giữ **disabled trong vertical slice**. Không nên coi việc có node T5 trong catalog là cam kết chúng cùng tồn tại trong ranked.

## 6. Lai nhánh — 15 node có ID riêng

| ID | Hướng lai gameplay | Vai trò |
|---|---|---|
| `FUSE_FIRE_WIND` | Hỏa + Phong tăng diện lửa | AoE/zone |
| `FUSE_WATER_LIGHT` | Thủy + Lôi dẫn điện | chain-control |
| `FUSE_WATER_EARTH` | Thủy + Thổ tạo bùn | slow |
| `FUSE_WIND_TOOL` | Phong + nhẫn cụ | ranged |
| `FUSE_SHADOW_TRAP` | Nara + bùa trói | trap/control |
| `FUSE_EYE_KEN` | Sharingan + thể thuật | counter |
| `FUSE_BYAKU_LIGHT` | Byakugan/Nhu Quyền + Lôi | hybrid melee |
| `FUSE_ABU_MED` | Côn trùng + Y thuật | support |
| `FUSE_PUP_POISON` | Khôi lỗi + độc | zone control |
| `FUSE_CLONE_SEAL` | Phân thân + phong ấn | trap/deception |
| `FUSE_WATER_MIST_GEN` | Thủy sương + ảo thuật | stealth/control |
| `FUSE_WIND_FIRE_TOAD` | Cóc + Hỏa + Phong | team AoE |
| `FUSE_SEAL_RASENGAN` | phong ấn + Rasengan | impact control |
| `FUSE_EARTH_ABU` | Thổ + Aburame | stealth/zone |
| `FUSE_INU_WIND` | Inuzuka + Phong | dive |

**Lưu ý:** có **15 node lai trong catalog** nhưng chỉ **12 công thức synergy `SY01..SY12`** được lưu riêng. **Không** coi hai danh sách là 1–1: ba loại world reaction/bloodline/team synergy có thể không trùng node lai. Để code, `nodes[].requires_all` là cạnh đồ thị; `synergies[]` là trigger/event design. Khi thêm synergy phải quyết định rõ có tạo node mua hay không.

## 7. 12 synergy được định nghĩa trong JSON

| Mã | Inputs (nguồn hiện tại) | Type | Ý nghĩa / cảnh báo |
|---|---|---|---|
| SY01 | `FIRE`, `WIND` | world_reaction | gió khuếch đại lửa; không phải huyết kế |
| SY02 | `WATER`, `LIGHT` | world_reaction | vùng nước dẫn điện |
| SY03 | `EARTH`, `WATER` | world_reaction | bùn làm chậm; không tạo Mộc |
| SY04 | `WIND`, `BASE_WEAPON` | build_fusion | phi tiêu lưỡi gió |
| SY05 | `HYG_POINT`, `LIGHT_SPARK` | build_fusion | Lôi Nhu Quyền, game design |
| SY06 | `UCH_EYE3`, `TAI_COMBO` | build_fusion | đọc đòn và phản kích |
| SY07 | `WATER_MIST`, `GEN_MIRAGE` | build_fusion | ảo cảnh trong sương |
| SY08 | `NARA_BIND`, `SEAL_TRAP` | build_fusion | Ảnh ấn phục kích |
| SY09 | `ABU_SCOUT`, `MED_PALM` | build_fusion | côn trùng hỗ trợ |
| SY10 | `SUM_TOAD`, `FIRE_DRAGON`, `WIND_GUST` | team_fusion | hợp kích Cóc/Hỏa/Phong |
| SY11 | `WATER_ROOT`, `WIND_ROOT`, `YUKI_ICE` | bloodline | yêu cầu `YUKI_ICE` không thể thay bằng 2 hệ |
| SY12 | `WATER_ROOT`, `EARTH_ROOT`, `RARE_WOOD` | bloodline | yêu cầu `RARE_WOOD` tuyệt đối |

**Loại input:** phần tử có trong `nodes[].id` là **skill ref**; `FIRE`, `WIND`, `WATER`, `EARTH`, `LIGHT` là **element token**, không phải missing skill ref. JSON mới có `input_refs` với `kind` để tránh agent nhầm `FIRE` là ID skill.

### Ví dụ bốn trường hợp

1. **World reaction (không mua):** người A gây `WET` trên khu vực, người B đánh Lôi; phản ứng khi các điều kiện không gian/thời gian hợp lệ. Dự đoán/telegraph vẫn đủ rõ.
2. **Build fusion (phải mua):** Nara có `NARA_BIND` + `SEAL_TRAP` → unlock `FUSE_SHADOW_TRAP`, trả SP/Ryō, trang bị một slot active nếu có runtime def.
3. **Team fusion:** người có khế ước Cóc + Hỏa + Phong phối hợp, yêu cầu window tương tác, giới hạn tầm/burst; không nhất thiết một người sở hữu cả ba nhánh.
4. **Bloodline:** `WATER_ROOT + WIND_ROOT + YUKI_ICE` mở biến thể; **điều kiện cuối không được bỏ**.

## 8. Unlock gate: hai lớp và chính sách fail-closed

### 8.1 Điều kiện bắt buộc

```text
A. skill_id hợp lệ; chưa học; được enable trong mode hiện tại
B. actor.level >= tier min level
C. tất cả requires_all đã học
D. với từng group trong requires_any: có ít nhất 1 đã học
E. không vi phạm nhóm mutual exclusion / slot / chỉ số nguyên tố
F. điều kiện đặc biệt (clan, bloodline, mentor, training, pact, item, event) đã có rule máy
G. đủ SP và Ryō (sau cùng kiểm inventory item tiêu thụ)
H. authority thực hiện transaction một lần, không bị race
```

`requires_any` là **AND của các nhóm OR**: `[[A,B],[C,D]]` nghĩa là **(A OR B) AND (C OR D)**; `[]` nghĩa là không yêu cầu thay thế nào. Điều này quan trọng khi agent hiện thực hóa validator.

### 8.2 Trạng thái dữ liệu 162 node hiện tại

- `requires_all`, `requires_any`, `tier`, `id`, `tree`, `source_label` là **dữ liệu máy kiểm được**.
- `unlock_gate` là văn bản **mô tả yêu cầu**, chưa phải executable predicate; `gate_id` ổn định để sau này gắn resolver. **Tồn tại `unlock_gate` nghĩa là không được auto-unlock**.
- `access.gate_state=requires_implementation` nghĩa là gate chưa được cài và test; engine **phải khóa** nếu chưa resolve.
- `implementation_status=design_only` nghĩa là chưa có combat runtime definition. Cho xem graph trong UI nhưng **không cho trang bị/cast**.
- `combat_runtime.* = null` có chủ ý; **không điền số ngẫu nhiên để coi như cân bằng**.
- Chỉ khi có test/approval mới bật `implemented` cho node cụ thể và map sang `ability_archetype`.

### 8.3 Định dạng rule mới khuyến nghị cho milestone unlock

Không phá format catalog cũ; tạo `gate_rules.json` hoặc trường `gate_rules` với predicate có kiểu và validator, ví dụ **minh họa tương lai**:

```json
{
  "id": "GATE_UCH_EYE1",
  "all": [
    {"op": "clan_is", "value": "Uchiha"},
    {"op": "flag_is_true", "value": "training.sharingan_awakened"}
  ]
}
```

Nara Hiden có thể cần cấu trúc `any` = `clan_is Nara` **hoặc** `mentor_training_completed nara_shadow`, trong khi Sharingan thì **không có đường mentor thay huyết thống**. `RINNEGAN`, Jinchūriki và đặc biệt không nằm trong item shop phổ thông.

### 8.4 Exclusivity

- `UCH_FLAME` vs `UCH_SPACE` là **hai gói Mangekyō mẫu loại trừ**, không mặc định mọi Uchiha sở hữu cả hai; gate gameplay chỉ được đóng sau khi thiết kế gói cá nhân đầy đủ.
- Một trận có **một gói thức tỉnh**; không stack tất cả T5 hoặc nhiều Bát Môn/tiên thuật xung đột.
- Một loại triệu hồi/pact lớn có thể giới hạn trong loadout. Cần xác định rõ khi vào runtime, không mặc định loại bỏ mọi lựa chọn từ gốc.

## 9. Vật phẩm mở nhánh / nhận tài nguyên

### 9.1 Tầng loot

| Nguồn | Reward | Ví dụ item gate | Độ bảo đảm |
|---|---|---|---|
| Quái thường | XP + Ryō + vật tư nhỏ | — | income ổn định |
| Elite | nhóm mảnh bí quyển/tu luyện | cuộn loại hệ/phong ấn | RNG có pity |
| Boss vùng | khế ước, ấn, mảnh T3/T4 | `scroll_summoning_toad` | có quyền chọn nhóm theo mode |
| World boss / contest | chìa thức tỉnh / lõi hiếm T5 | `awakening_memory` | giới hạn và cạnh tranh rõ |

**Ví dụ item ID minh họa, chưa nằm trong `skills.json`:** `scroll_fire`, `scroll_shadow_clone`, `training_seal`, `scroll_summoning_toad`, `awakening_memory`, `sage_essence`. Cần tạo `items.json` và `loot_tables.json` riêng trong milestone Loot; chưa tuyên bố runtime đã xử lý.

### 9.2 Pity và tính công bằng

- Counter theo `(player_id, loot_group_id, match_id)`.
- Sau **4 lượt hợp lệ** cùng loot group không được mảnh tương thích mục tiêu, lần nhận thưởng tiếp theo cho phép **chọn một mảnh** phù hợp group; quy tắc exact trigger phải có unit test trước khi release.
- Pity không bảo đảm **huyết kế không tương thích** hoặc ultimate hiếm trái luật. Loot group chỉ chứa tài nguyên player có thể sử dụng hoặc chuyển đổi hợp lệ.
- Có đường T4 ổn định mà không phụ thuộc world boss; thay boss bằng rèn luyện cũng phải có đánh đổi.
- **Không ghi tỷ lệ drop %** trong bản thiết kế này vì chưa đo/duyệt. Không cho Codex/Antigravity tự coi một con số đoán là canonical.

### 9.3 Transaction mua skill

`check → reserve SP/Ryō/item → apply node → emit notification` phải atomic trên authority; trùng request id không thể tiêu/mua hai lần. Khi lỗi xảy ra, hoàn trả đầy đủ hoặc fail sạch.

## 10. Combat slots và cân bằng kỹ năng

### 10.1 Equipment

- `active_slots=4`, `ultimate_slots=1`, `passive_slots=3`, `signature_trait_slots=1`, `tool_slots=1`, `substitution_slots=1`.
- Một node `root` không phải active skill; một node học được không tự thêm nút HUD.
- Nút chưa có `runtime_definition` có thể hiển thị trong đồ thị debug, **không thể gắn nút và không thể cast**.
- `upgrade_level`: giới hạn tối đa 3 theo gợi ý, chỉ khi có cấu hình riêng và test economy.

### 10.2 Field combat cần khi hiện thực hóa mỗi ability

- Identity: `skill_id`, `ability_archetype`, `slot_type`, `is_ultimate`, `element_tags`.
- Balance: `base_damage`, `scaling`, `chakra_cost`, `cooldown_seconds`, `startup_seconds`, `active_seconds`, `recovery_seconds`, `cc_type`, `cc_duration_seconds`, `duration_seconds`.
- Hit/targeting: `range_world_units`, `radius_world_units`, `max_targets`, `collision_mask`, `target_filter`, `line_of_sight_required`, `aim_style`.
- Visual/audio: `animation_name`, `vfx_id`, `telegraph_id`, `sfx_id`, `visibility_priority`.
- Network: `server_authoritative=true`, `request_validation`, `snapshot_replication_class`.

**Không suy diễn** `base_damage`, `cooldown` hoặc `cc` chỉ từ mô tả tiếng Việt. Khi thiết kế runtime, một đơn vị `world_units` dùng đúng tọa độ world của Godot để tránh lẫn pixel tài nguyên với metre ngoài đời.

### 10.3 Quy tắc cân bằng

- Tier cao tăng sự **đa dạng cơ chế**, không nhất thiết chỉ tăng damage. 1 ultimate/từng loadout, có startup và phản khắc chế.
- CC chain bị diminishing returns; nhãn thuật bị ép tài nguyên/visibility; Bát Môn có hậu quả; hóa lỏng có điện khắc; triệu hồi có cap entity.
- Không cho summon chiến đấu thay player sau khi team bị loại; object pool/VFX độc lập với server hit logic.

## 11. Skill UI trên mobile

1. Filter theo **Tree / Clan / Element / Tier / Role**; không chỉ có ô tìm kiếm văn bản.
2. **Nút có thể học:** sáng; **đủ tier nhưng thiếu Ryō/SP:** vàng; **thiếu một requirement:** biểu tượng lock + lý do; **không tương thích huyết kế:** khóa vĩnh viễn trong trận; **design-only:** nhãn dev chỉ ở bản debug.
3. Click/touch node mở bảng thông tin: role, effect description, tier, total path cost, điều kiện trước, item gate và nguồn farm, combo tạo ra, slot và counterplay.
4. Nút `Plan Path` đánh dấu các nút tiền đề, tổng SP/Ryō và item cần; không auto-purchase tất cả.
5. Cho phép xem đồ thị khi di chuyển nhưng chặn thao tác tiêu tiền lúc combat nguy hiểm nếu UI gây bất công; quyết định mode có thể chọn khi playtest.
6. Nếu player nhận được mảnh hiếm, hiển thị **3 nhánh ứng viên hợp lệ** hoặc lý do không sử dụng được.

## 12. Tám ví dụ build và counterplay

| Build | Gia tộc/chuyên môn | Node/nhánh nổi bật | Mạnh ở | Đối trọng |
|---|---|---|---|---|
| Lôi Sát | Uchiha + Lôi/Thể | `UCH_EYE3`, `LIGHT_CHIDORI`, `FUSE_EYE_KEN` | ám sát/phản công | Thổ tường, AoE, đọc dash |
| Hỏa Ảo | Uchiha + Hỏa/Gen | `FIRE_BALL`, `UCH_GEN`, `FIRE_ZONE` | burst/zone | Thủy, giải ảo, đánh xa |
| Nhu Quyền | Hyūga + Thể | `HYG_POINT`, `HYG_64`, `HYG_ROTATION` | đánh gần, khóa chakra | kite, zoning |
| Ảnh Ấn | Nara + Phong ấn | `NARA_BIND`, `SEAL_TRAP`, `FUSE_SHADOW_TRAP` | giữ boss, trap | áp sát, phá bẫy |
| Băng Ảo | Yuki + Gen/Thủy | `YUKI_WALL`, `YUKI_MIRROR`, `GEN_MIRAGE` | zone & escape | phá gương, AoE |
| Trùng Hộ | Aburame + Y thuật | `ABU_SCOUT`, `MED_PALM`, `FUSE_ABU_MED` | hỗ trợ và vision | diện rộng/thiêu đốt |
| Khôi Lỗi Độc | Khôi lỗi + Phong ấn | `PUP_POISON`, `FUSE_PUP_POISON` | cầm chân khu vực | phá rối, flank |
| Phong Nha | Inuzuka + Phong | `INU_FANG`, `WIND_GUST`, `FUSE_INU_WIND` | đuổi bắt | bẫy, slow, phá thú |

Các build là minh họa về **hướng**, có thể không mua đủ toàn bộ đường trong ngân sách 12 SP nếu gate điều chỉnh; khi code cần test đường đi tối thiểu bằng validator `build_budget_test`.

## 13. Hợp đồng JSON `skills.json` (v1.1-design)

**Top-level:** `metadata`, `match_config_proposal`, `tier_rules`, `element_tokens`, `gate_rule_templates_proposal`, `source_label_definitions`, `nodes`, `synergies`, `unlock_logic`, `drop_rules_proposal`.

**Mỗi node:**

| Field | Type | Vai trò |
|---|---|---|
| `id` | string unique | khóa bất biến dùng trong save/equip |
| `name` | string | tên hiển thị tiếng Việt |
| `tree` | string | một trong 29 nhóm |
| `tier` | integer 0..5 | level/SP/Ryō theo tier_rules |
| `requires_all` | string[] | tất cả phải đã học |
| `requires_any` | string[][] | mỗi nhóm cần ≥1 skill |
| `unlock_gate` | string|null | mô tả gate do con người đọc |
| `gate_id` | string|null | khóa resolver tương lai, null nếu không có gate |
| `access.gate_state` | enum | `none` hoặc `requires_implementation` |
| `combat_roles` | string[] | role để lọc, không tự map vào ability |
| `source_label` | enum | `canon_adapted` hoặc `game_design` |
| `canonical_rank` | E/D/C/B/A/S/null | nhãn lore, không nhân damage |
| `gameplay_effect` | string | mô tả ý định gameplay |
| `level_requirement`, `cost_proposal` | number/object | proposal derived by tier |
| `implementation_status` | enum | `design_only` mặc định |
| `combat_runtime` | object | fields `null` khi chưa approved |

**`gate_rule_templates_proposal`:** 7 mẫu predicate có kiểu cho Uchiha, Hyūga, Nara, 3 hệ khởi đầu và Phong ấn. Đây là **proposal chưa executable**, dùng để agent làm milestone M4; ngoài các mẫu này, gate của 55 node vẫn được khóa cho đến khi resolver được cài và duyệt.

**Synergy:** `id`, `inputs` (source), `input_refs[] {kind, value}`, `outcome`, `type ∈ {world_reaction,build_fusion,team_fusion,bloodline}`, `note` tùy chọn.

**IMPORTANT:** thêm `combat_runtime` với null là minh bạch về trạng thái, **không** làm JSON tự sinh kỹ năng chiến đấu. Khi agent triển khai một tập node, nên tách `runtime_abilities.json` được validate và map theo ID thay vì điền bừa stats cho toàn catalog.

### 13.1 Điều kiện validator bắt buộc

- `id` unique; `tier` hợp lệ; mọi `requires_all`/`requires_any` trỏ node tồn tại; không có cycle.
- Tất cả synergy `skill_id` hợp lệ, `element_token` thuộc list; không hiểu `FIRE` là node id.
- `requires_any` là danh sách các danh sách, các nhóm không trống.
- `gate_state` và `gate_id` nhất quán với `unlock_gate`.
- `implementation_status=design_only` không có handler được đăng ký; nếu `implemented` phải có runtime def đã test.
- Gate huyết kế hoặc clan không được bypass chỉ bằng material. `UCH_FLAME` và `UCH_SPACE` không cùng tồn tại trong một build nếu rule độc quyền đã bật.
- Stats chưa biết = `null`; không có giá trị âm, `NaN`, infinite khi bổ sung runtime.

## 14. Dữ liệu và danh mục: số đếm chuẩn

| Phân nhóm | Số nhóm cây | Số node |
|---|---:|---:|
| Nền tảng | 1 | 14 |
| Ngũ Độn | 5 | 35 |
| Chuyên môn | 7 | 31 |
| 10 gia tộc | 10 | 57 |
| Đặc biệt | 5 | 10 |
| Lai nhánh | 1 | 15 |
| **Tổng** | **29** | **162** |

Số đếm này là **invariant** khi giữ dataset v1.1; nếu cập nhật nội dung phải sửa expected count sau khi có yêu cầu/approval. Vui lòng không tự tạo thêm ID cho đẹp bảng hoặc đổi tiền tố `LIGHT_` giữa chừng.

## 15. Quy trình thêm một skill mới

1. **Thiết kế**: xác định game/canon label, vai trò, tree, counterplay, tier, gate hợp lệ và nguồn mở.
2. **Graph**: tạo ID mới, khai báo prerequisites AND/OR, đảm bảo không cycle và không bypass bloodline.
3. **Economy**: kiểm SP/Ryō tối thiểu để đến node; đảm bảo build viable khi chưa có drop hiếm.
4. **Gameplay runtime**: thêm archetype/config, hit shape, cooldown/chakra, telegraph, audio + mobile input; unit tests.
5. **Authority**: validate cast/unlock, tránh duplicate item, replay/spam RPC; offline và multiplayer dùng chung rule.
6. **Balance**: playtest phản khắc chế, mobile readability, combo abuse, FPS; ghi số liệu thay vì cảm tính.
7. **Review/merge**: Antigravity code → Codex review diff → owner chấp thuận → version data được tăng phù hợp.

### Acceptance scenarios quan trọng

| Test | Kết quả kỳ vọng |
|---|---|
| Uchiha có `UCH_EYE1` khi đã thỏa clan và awakening gate | hợp lệ |
| Ninja clan khác sở hữu cuộn Hỏa | có thể học `FIRE_ROOT` nếu các gate nguyên tố đã giải, **không được có Sharingan** |
| Người chơi chỉ có Thủy + Thổ | **không** mở `RARE_WOOD` |
| Người chơi chỉ có Thủy + Phong | **không** mở `YUKI_ICE` |
| Ninja không có học Nara nhưng nhặt mảnh bí thuật bóng | không bypass Hiden mentor/clan gate |
| `requires_any = [[A,B],[C,D]]` và người có A+D | hợp lệ phần OR |
| Player thiếu một node trong `requires_all` | từ chối, không trừ SP/Ryō |
| Hai request học cùng ID gửi cùng lúc | chỉ học/tiêu 1 lần |
| Node chưa có runtime ability | không thể equip/cast; UI báo trạng thái phù hợp |
| T5 ở lv1 với vật phẩm hiếm | từ chối vì gate tier |
| Bắn Lôi lên vùng ướt | world reaction có cap chain, đúng thuộc tính và TTL |
| Người có mọi combo nhưng không có bloodline | không tự có quyền huyết kế |

## 16. Những điểm cần chốt trước khi code đại trà

- Phạm vi chiêu đầu tiên cho vertical slice: **tối đa 24–36 node implemented** nhưng chú trọng 8–12 ability thật đầu tiên để thấy vui, thay vì triển khai toàn bộ node root.
- Sát thương, cooldown, mana, range của **từng ability** và hit shape trên Pixel Art mobile.
- Contract typed cho cổng clan/mentor/event/bloodline; dữ liệu gate text hiện **chưa executable**.
- Cơ chế `UCH_FLAME` vs `UCH_SPACE` exclusive và tổng SP đủ cho Mangekyō trong 42 phút.
- Trùng côn trùng, rối, phân thân và triệu hồi tính entity budgets.
- Quy tắc chính xác pity, loot ownership/reconnect, tỷ lệ rơi và prize bias.

### Change Log

| Ngày | Phiên bản | Thay đổi |
|---|---|---|
| 2026-10-16 | 1.0 | Tách hệ thống skill khỏi GDD, chuẩn hóa 162 node/29 nhóm/12 synergy, chỉ ra gate chưa executable và runtime còn thiếu |

## 17. Tài liệu đối chiếu lore và kỹ thuật (tham khảo)

Các nguồn dưới đây giúp agent **kiểm chứng khái niệm Naruto**, không biến thông số game đề xuất thành sự thật nguyên tác:

- Naruto Official — chakra natures: https://naruto-official.com/en/news/01_2492
- Naruto Official — Neji / Byakugan / Gentle Fist: https://naruto-official.com/en/news/01_1296
- Naruto Official — Shikamaru / shadow arts: https://naruto-official.com/en/news/01_1910
- Naruto Official — Sage training: https://naruto-official.com/en/news/01_1321
- Naruto Official — Mangekyō: https://naruto-official.com/en/news/01_2424
- Naruto Official — Hashirama / Wood Release: https://naruto-official.com/en/news/01_1627
- Godot stable official docs để xác thực GDScript/API theo version project: https://docs.godotengine.org/en/stable/

Không tự lấy hình, âm thanh, thiết kế UI hoặc mã nguồn từ các nguồn này mà không có quyền sử dụng.
