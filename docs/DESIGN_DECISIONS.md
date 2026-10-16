# DESIGN_DECISIONS.md — Sổ quyết định thiết kế

**Phiên bản:** 2.1 • **Ngày:** 2026-10-16 • **Trạng thái:** `OFFICIAL_DESIGN_BASELINE`.

> Hồ sơ quyết định cho baseline solo hai người: các lựa chọn đã được Product Owner duyệt, lịch sử thay thế và phần đặc tả cần chuẩn bị trước từng task. Luật hiện hành nằm trong GAME_DESIGN/SKILL_SYSTEM; bản này giúp tra lý do và phạm vi áp dụng.

## 1. Thẩm quyền và cách đóng quyết định

- `GAME_DESIGN.md` giữ luật trận và kinh tế; `SKILL_SYSTEM.md` giữ luật kỹ năng/loot; `ARCHITECTURE.md` giữ hợp đồng kỹ thuật; `GRAPHICS_DESIGN.md` giữ hình ảnh. File này là **sổ theo dõi**, không thay thế các nguồn đó.
- `OPEN`: chưa giao quyền/chọn phương án; `PROPOSED`: ứng viên; `APPROVED`: Product Owner chấp thuận lựa chọn cụ thể; `DELEGATED`: chi tiết triển khai/thông số thử đã giao Antigravity tự đặc tả/kiểm, không cần xin duyệt lại từng mục; `SUPERSEDED`: đã thay thế; `DEFERRED`: ngoài solo baseline.
- Bảng §2 ghi trạng thái hiện hành. Chế độ chính đã chuyển sang solo sinh tồn; luật đội lưu tham chiếu, luật cứ điểm buff đã bị thay thế. Các đoạn ghi "đề xuất" vẫn là ứng viên để trao đổi.
- Khi duyệt: ghi lựa chọn + ngày + phạm vi mode/milestone + người duyệt; cập nhật nguồn chính và Change Log, rồi mới chuẩn bị task code liên quan. Nếu cần đổi dữ liệu, chuẩn bị diff riêng và validator.
- Một quyết định mở chỉ chặn task phụ thuộc nó. Không bắt chốt toàn bộ luật beta để cho phép task di chuyển sau này.
- Điều kiện bàn giao bản chính thức: các luật vận hành cốt lõi được chốt, tài liệu nguồn đồng bộ, roadmap có task/phụ thuộc/tiêu chí nghiệm thu và không còn mâu thuẫn ảnh hưởng task mở đầu. Thông số cân bằng cần đo được ghi riêng với phạm vi thử và tiêu chí điều chỉnh; không dùng nhãn "đã triển khai" cho một bản đặc tả được duyệt.

## 2. Danh sách quyết định

| ID | Trạng thái | Cần xác định | Nguồn chính | Phải giải trước |
|---|---|---|---|---|
| WIN-01 | DEFERRED | Đội cuối cùng sống sót thắng, chỉ lưu cho mode đội | GAME_DESIGN §3.5 | Khi mở mode đội |
| SEAL-01 | SUPERSEDED | Quyền sở hữu phong ấn theo đội đã bị OBJECTIVE-01 thay thế | GAME_DESIGN §3.1 | Không áp dụng |
| REVIVE-01 | DEFERRED | Cứu đồng đội/mục tiêu hồi sinh, chỉ lưu cho mode đội | GAME_DESIGN §3.5 | Khi mở mode đội |
| ZONE-01 | APPROVED | Vùng an toàn thu hẹp, sát thương ngoài vùng; thời lượng cập nhật theo MATCH-04 | GAME_DESIGN §3.2, §3.4 | Đã chọn 2026-10-16 |
| SEAL-02 | SUPERSEDED | Cứ điểm/phong ấn buff đã bị OBJECTIVE-01 bỏ | GAME_DESIGN §3.1 | Không áp dụng |
| ELIM-01 | DEFERRED | Cả ba chết hẳn loại đội, chỉ lưu cho mode đội | GAME_DESIGN §3.5 | Khi mở mode đội |
| BUILD-02 | APPROVED | Giữ node đã học, không hoàn điểm; đổi hướng bằng SP còn lại và kỹ năng sở hữu | SKILL_SYSTEM §3, §10 | Đã chọn 2026-10-16 |
| BUILD-03 | APPROVED | Chỉ học node ngoài giao tranh; trong giao tranh được xem cây, chưa mua | SKILL_SYSTEM §10.1 | Đã chọn 2026-10-16 |
| NATURE-01 | APPROVED | Hai hệ thường; hệ thứ ba qua sự kiện hiếm, vẫn kiểm gate huyết kế | GAME_DESIGN §2.1; SKILL_SYSTEM §3 | Đã chọn 2026-10-16 |
| LOADOUT-01 | APPROVED | Đổi kỹ năng chỉ ngoài giao tranh, mọi vị trí; giữ cooldown khi đổi ô | SKILL_SYSTEM §10.1 | Đã chọn 2026-10-16 |
| REWARD-01 | DEFERRED | Chia đều trong đội nhận quỹ XP/Ryō, chỉ lưu cho mode đội | GAME_DESIGN §3.5 | Khi mở mode đội |
| LOOT-02 | APPROVED | Cuộn/mảnh hiếm elite/boss rơi công khai, mọi người chơi tranh nhặt | GAME_DESIGN §4; SKILL_SYSTEM §9.1 | Đã chọn 2026-10-16 |
| PITY-02 | APPROVED | Nếu lượt thứ tư cũng trượt, được chọn ngay trong reward thứ tư | SKILL_SYSTEM §9.2 | Đã chọn 2026-10-16 |
| PITY-03 | APPROVED | Tham gia hợp lệ nhưng không nhận mảnh mục tiêu, kể cả bị cướp, tính trượt | SKILL_SYSTEM §9.2 | Đã chọn 2026-10-16 |
| LOOT-03 | APPROVED | Mảnh chọn pity vào thẳng túi người có quyền chọn, không bị cướp | SKILL_SYSTEM §9.2 | Đã chọn 2026-10-16 |
| LOOT-04 | APPROVED | Chết rơi toàn bộ vật tư kể cả cuộn còn lại; không rơi XP/SP/Ryō/node đã học | GAME_DESIGN §3.3; SKILL_SYSTEM §9.1 | Đã chọn 2026-10-16 |
| LOOT-05 | APPROVED | Tư liệu chung túi giới hạn; đầy thì pity chờ nhận riêng, không bị cướp | GAME_DESIGN §4; SKILL_SYSTEM §9 | Đã chọn 2026-10-16 |
| REWARD-02 | APPROVED | Quỹ XP/Ryō thuộc bên kết liễu; solo là người kết liễu | GAME_DESIGN §2.2 | Đã chọn nguyên tắc kết liễu 2026-10-16 |
| IDENTITY-01 | APPROVED | Sinh tồn là trọng tâm; cảm hứng MOBA chỉ ở farm quái lấy XP | GAME_DESIGN §1 | Đã chọn 2026-10-16 |
| MODE-01 | APPROVED | Ưu tiên solo nhiều người, mỗi người một phe, người cuối cùng sống sót thắng | GAME_DESIGN §1, §3.2 | Đã chọn 2026-10-16 |
| MATCH-02 | APPROVED | Phạm vi hiện tại hai người solo/trận; tăng số người để sau | GAME_DESIGN §3 | Đã chọn 2026-10-16 |
| MATCH-03 | APPROVED | Chọn vùng trước trận, spawn ngẫu nhiên trong vùng với khoảng cách an toàn | GAME_DESIGN §3.1 | Đã chọn 2026-10-16 |
| MATCH-04 | APPROVED | Thời lượng mục tiêu 20–25 phút, không là timeout | GAME_DESIGN §3 | Thay mục tiêu 42 phút cũ |
| MATCH-05 | APPROVED | Cả hai chết sau giải quyết toàn bộ damage/Thế thân cùng tick thì hòa | GAME_DESIGN §3.2 | Đã chọn 2026-10-16 |
| MATCH-06 | APPROVED | Disconnect đứng yên, vẫn nhận damage; không timeout tự loại; reconnect actor cũ | GAME_DESIGN §3.2 | Đã chọn 2026-10-16 |
| OBJECTIVE-01 | APPROVED | Bỏ chiếm giữ cứ điểm/phong ấn để nhận buff | GAME_DESIGN §3.1 | Thay SEAL-01/SEAL-02 |
| SOLO-LIFE-01 | APPROVED | Solo chết thì bị loại, không hồi sinh | GAME_DESIGN §3.2, §3.3 | Đã chọn 2026-10-16 |
| SOLO-SUB-01 | APPROVED | Mỗi người một cuộn Thế thân khởi đầu; cuộn có thể rơi thêm | GAME_DESIGN §3.3 | Đã chọn 2026-10-16 |
| SOLO-SUB-02 | APPROVED | Bị động tiêu cuộn trước đòn làm HP về 0, không phải critical hit | SKILL_SYSTEM §10.4 | Đã chọn 2026-10-16 |
| SOLO-SUB-03 | APPROVED | Kích hoạt hồi một phần HP theo config rồi tàng hình chạy thoát | SKILL_SYSTEM §10.4 | Đã chọn 2026-10-16 |
| SOLO-SUB-04 | APPROVED | Sát thương vòng bo gây chết cũng kích hoạt cuộn | SKILL_SYSTEM §10.4 | Đã chọn 2026-10-16 |
| SOLO-SUB-05 | APPROVED | Mang tối đa hai cuộn, chỉ có một cuộn khởi đầu | SKILL_SYSTEM §10.4 | Đã chọn 2026-10-16 |
| SOLO-SUB-06 | APPROVED | Có cooldown nội tại; lethal hit trong cooldown vẫn giết dù còn cuộn | SKILL_SYSTEM §10.4 | Đã chọn 2026-10-16 |
| SOLO-SUB-07 | APPROVED | Tàng hình vẫn nhận damage, gây hoặc nhận damage làm lộ thân | SKILL_SYSTEM §10.4 | Đã chọn 2026-10-16 |
| SOLO-SUB-08 | APPROVED | Kích hoạt xóa CC/hiệu ứng bất lợi đang có; hiệu ứng mới vẫn áp ngay được | SKILL_SYSTEM §10.4 | Đã chọn 2026-10-16 |
| SOLO-SUB-09 | APPROVED | Cấu hình thử: HP về 25% max, ẩn tối đa 3s, cooldown 60s | SKILL_SYSTEM §10.4 | Đã chọn cho prototype 2026-10-16 |
| COMBAT-02 | APPROVED | Thoát combat sau 5s không gây/nhận damage hoặc dùng đòn/skill tấn công, cả PvE/PvP | SKILL_SYSTEM §10.1 | Đã chọn 2026-10-16 |
| PITY-04 | APPROVED | Ngưỡng thử 5% max HP mục tiêu/30s cuối, còn sống trong vùng tham gia lúc mục tiêu chết | SKILL_SYSTEM §9.2 | Đã chọn cho prototype 2026-10-16 |
| PITY-05 | APPROVED | Settle một lần khi toàn bộ mảnh hiếm lượt đó được nhặt hoặc hết hạn | SKILL_SYSTEM §9.2 | Đã chọn 2026-10-16 |
| PITY-06 | APPROVED | Counter theo nhóm; nhận mảnh mục tiêu/bảo hiểm hoặc đổi mục tiêu cùng nhóm thì về 0 | SKILL_SYSTEM §9.2 | Đã chọn 2026-10-16 |
| SLICE-02 | APPROVED | Bản hai người: một clan, một nature, hai hướng build; mở rộng sau khi đạt | GAME_DESIGN §11 | Đã chọn 2026-10-16 |
| SLICE-03 | APPROVED | Uchiha + Hỏa; hai hướng Hỏa thuật và Ảo thuật | GAME_DESIGN §2.1, §11 | Đã chọn 2026-10-16 |
| ZONE-02 | APPROVED | Bo cuối hết vùng an toàn, damage tăng để buộc kết thúc bằng sống sót | GAME_DESIGN §3.4 | Đã chọn 2026-10-16 |
| AUTO-01 | APPROVED | Antigravity tự triển khai/test/sửa liên tục đến bản M8 chơi được, không chờ duyệt từng task | ANTIGRAVITY_AUTOPILOT | Yêu cầu 2026-10-16 |
| ART-01 | APPROVED | Dùng generate_image tích hợp Antigravity, có master prompt/JOB/reference và tự kiểm/promote | ART_GENERATION_GUIDE | Yêu cầu 2026-10-16 |
| ACCEPT-01 | APPROVED | Người dùng chỉ nghiệm thu bằng chơi thực tế cuối; VERIFIED cho phép agent tiếp tục, không tự DONE | AGENTS; ANTIGRAVITY_AUTOPILOT | Yêu cầu 2026-10-16 |
| ECON-02 | APPROVED | Giữ XP/SP/Ryō, học node cần đủ SP và Ryō | GAME_DESIGN §2.2 | Đã chọn 2026-10-16 |
| SLICE-01 | DELEGATED | Danh sách ID/handler, stat chiêu mẫu và bài thử hai hướng Uchiha/Hỏa đã chốt | GAME_DESIGN §11 | M3-01 / M4-02 theo phạm vi |
| MATCH-01 | DELEGATED | Bán kính spawn an toàn, xử lý cùng chọn vùng, bản đồ và lịch/damage vòng bo | GAME_DESIGN §3 | M6A-02 |
| LIFE-01 | DELEGATED | Phân loại effect/shield, làm tròn HP và cleanup effect sau chết; luật/thông số thử đã chốt | GAME_DESIGN §3.3; SKILL_SYSTEM §10.4 | M3-02; M6A-02 cho match |
| ECON-01 | DELEGATED | XP/lịch SP, thu nhập/sink và số nguyên payout; không rơi XP/SP/Ryō đã chốt | GAME_DESIGN §2.2 | M4-02 |
| LOOT-01 | DELEGATED | Số ô/stack, range pickup/participation, TTL, loot table và tỉ lệ cuộn Thế thân thử | SKILL_SYSTEM §9, §10.4 | M5-01 |
| PITY-01 | DELEGATED | Nhóm/mảnh cụ thể, event ledger, target revision, thứ tự settle/claim và fixture | SKILL_SYSTEM §9.2 | M5-02 |
| BUILD-01 | DELEGATED | Vòng đời buff/summon khi tháo và contract learn/equip/hit; timer combat 5s đã chốt | SKILL_SYSTEM §10 | M4-03 |
| SKILL-01 | DELEGATED | Kiểu node, allowlist, quyền tiến trình và runtime binding | SKILL_SYSTEM §8, §13 | M4-01 / M4-03 |
| FUSE-01 | DEFERRED | Binding synergy mới thuộc nhánh mở rộng; không là điều kiện bản Uchiha/Hỏa đầu tiên | SKILL_SYSTEM §7 | Khi duyệt M6B-02 |
| COMBAT-01 | DELEGATED | Chiêu mẫu, timing, targeting, ngắt cast, CC/Thế thân | GAME_DESIGN §5 | M3-01 |
| VIEW-01 | DELEGATED | Bố cục touch, vùng nhìn, thông tin trinh sát/ẩn | GAME_DESIGN §5, §8 | M2-01 cho HUD; M7-01 cho visibility |
| TECH-01 | DELEGATED | Binary/build engine, renderer, thiết bị và tiêu chí spike | ARCHITECTURE §1, §9 | M0-01; phần mạng trước M3-NET-01 |

**Chủ luật cốt lõi:** Product Owner. Theo AUTO-01, Antigravity tự hoàn thành mục DELEGATED trong brief trước code, dùng profile khởi đầu và kiểm chứng rồi tiếp tục, không hỏi lại từng số liệu. Số agent chọn là PROTOTYPE_DEFAULT/IMPLEMENTATION_DECISION, không ghi Product Owner đã duyệt cân bằng cuối. Codex kiểm tính nhất quán nếu sẵn có; không là cổng bắt người dùng chuyển diff từng task.

### 2.1 Các lựa chọn đã chốt ngày 2026-10-16

- **WIN-01 / REVIVE-01 / ELIM-01 — DEFERRED:** lựa chọn cũ cho mode đội, lưu trong GAME_DESIGN §3.5; không áp vào solo.
- **SEAL-01 / SEAL-02 — SUPERSEDED:** lựa chọn cũ về phong ấn/cứ điểm buff đã bị OBJECTIVE-01 thay thế.
- **ZONE-01 — CHỐT:** vùng an toàn thu hẹp dần, bên ngoài gây sát thương; solo kết thúc khi xác định người cuối cùng sống sót. Mục tiêu 42 phút trước đây đã được MATCH-04 thay bằng 20–25 phút. Lịch vòng bo và damage cụ thể cần cấu hình thử được duyệt.
- **MATCH-02/03/04 — CHỐT:** hiện tại chỉ hai người/trận; chọn vùng trước trận rồi spawn ngẫu nhiên trong vùng với khoảng cách an toàn; mục tiêu 20–25 phút, không phải timeout. Tăng số người để sau, không là điều kiện nghiệm thu hiện tại.
- **BUILD-02 — CHỐT:** giữ node đã học trong trận, không hoàn điểm; đổi hướng bằng SP còn lại và kỹ năng đã sở hữu. Đổi preset không làm thay đổi tiến trình hoặc hoàn chi phí.
- **BUILD-03 — CHỐT:** chỉ học node khi còn sống và ngoài giao tranh, tương tự equip; trong giao tranh được xem cây nhưng chưa mua. Request bị từ chối không trừ tài nguyên, không tự mua sau khi thoát combat.
- **NATURE-01 — CHỐT:** hai hệ chakra cơ bản thông thường; hệ thứ ba chỉ qua sự kiện hiếm có điều kiện riêng. Gate huyết kế được kiểm độc lập.
- **LOADOUT-01 — CHỐT:** thay kỹ năng đã học vào ô sử dụng chỉ khi ngoài giao tranh, ở bất kỳ vị trí nào; cooldown vẫn giữ khi đổi ô.
- **REWARD-01 — DEFERRED / REWARD-02 — CHỐT:** người dùng chọn đội kết liễu nhận quỹ rồi chia đều trong đội. Quy đổi sang solo (một người một phe): người kết liễu nhận quỹ XP/Ryō; không chia thưởng đồng đội trong mode chính.
- **LOOT-02 — CHỐT:** cuộn/mảnh bí thuật hiếm elite/boss rơi ra đất, mọi người chơi có thể tranh nhặt. Người hạ boss không độc quyền vật phẩm rơi; mảnh pity là ngoại lệ riêng theo LOOT-03.
- **PITY-02 / PITY-03 / LOOT-03 — CHỐT:** tham gia hợp lệ nhưng không nhận mảnh mục tiêu tính trượt, kể cả bị cướp. Miss thứ tư được chọn mảnh phù hợp, trả thẳng túi cá nhân, không bị cướp. Tiêu chí tham gia/settle/reset còn cần đặc tả.
- **IDENTITY-01 / MODE-01 / OBJECTIVE-01 — CHỐT:** tập trung solo sinh tồn; farm quái lấy XP, loot và vòng bo; bỏ cứ điểm buff. Solo là nhiều người mỗi người một phe, khác với prototype offline một nhân vật.
- **SOLO-LIFE-01 — CHỐT:** solo không hồi sinh; trụ hồi sinh chỉ lưu ý tưởng cho mode đội tương lai.
- **LOOT-04 — CHỐT:** chết hẳn rơi toàn bộ vật tư đang mang, gồm cuộn Thế thân chưa dùng; không rơi XP/SP/Ryō hoặc node đã học. Thế thân ngăn chết thành công không làm rơi đồ; giao dịch rơi vật tư chỉ chạy một lần.
- **SOLO-SUB-01..07 — CHỐT:** một cuộn khởi đầu, cap hai; bị động tự tiêu cuộn trước damage gây chết khi cooldown sẵn sàng, hồi HP theo config, tàng hình và bắt đầu cooldown. Vòng bo gây chết cũng kích hoạt. Trong cooldown vẫn có thể chết dù còn cuộn; tàng hình vẫn nhận damage và lộ khi gây/nhận damage. Không có nút kích hoạt thủ công hoặc miễn damage ngầm.
- **SOLO-SUB-08 — CHỐT:** xóa CC và hiệu ứng bất lợi đang có, kể cả DOT, khi kích hoạt. Không miễn CC/DOT/reveal mới; hit/nguồn khác có thể áp lại ngay. Đòn kích hoạt không được áp lại debuff sau bước thanh tẩy; vòng bo vẫn tiếp tục gây damage.
- **ECON-02 — CHỐT:** giữ XP/SP/Ryō, học node cần đủ SP và Ryō. Không bỏ tiền Ryō khi chuyển trọng tâm sang sinh tồn.
- **Yêu cầu bàn giao:** sau khi trao đổi và cập nhật xong, bộ tài liệu là bản chính thức làm cơ sở bắt đầu code. Sổ này lưu lịch sử và lý do lựa chọn; luật được duyệt phải xuất hiện trong tài liệu nguồn.

**Chốt bổ sung cho baseline 2.0:**

- **COMBAT-02:** timer ngoài combat 5 giây áp dụng PvE/PvP; kiểm trên authority khi commit learn/equip.
- **SOLO-SUB-09:** HP sau kích hoạt bằng 25% max HP, stealth tối đa 3s và cooldown 60s; đây là bộ số thử đã duyệt, không là cân bằng cuối.
- **MATCH-05/06:** chết cùng tick thì hòa; disconnect đứng yên, không timeout tự loại, vẫn xét bo/damage/Thế thân, reconnect tiếp tục cùng actor.
- **PITY-04/05/06:** ngưỡng thử 5% max HP/30s cuối, sống trong vùng khi mục tiêu chết; settle sau nhặt/hết hạn mảnh hiếm; reset từng nhóm khi nhận mục tiêu/bảo hiểm hoặc đổi mục tiêu.
- **SLICE-02/03:** Uchiha + Hỏa, hai hướng Hỏa thuật/Ảo thuật cho bản hai người. Thêm clan/nature/synergy để sau.
- **ZONE-02:** bo cuối không còn vùng an toàn, damage tăng theo config; Thế thân vẫn áp dụng, chết cùng tick vẫn hòa.
- **LOOT-05:** túi chung giới hạn ô, pity chờ riêng khi đầy; không bị cướp lúc chờ/giao, item đã vào túi vẫn rơi khi chết.

### 2.2 Đặc tả trước từng task trong baseline

Các dòng DELEGATED do Antigravity tự hoàn thành trước task tương ứng theo AUTOPILOT và [profile](../data/prototypes/solo_first_playable.json); không đưa luật đội/cứ điểm/số người lớn trở lại scope hoặc dừng chờ người dùng duyệt từng brief. Tập khởi đầu 22 ID và hai preset đã có trong profile, các giá trị thử được ghi nguồn, không tự gọi cân bằng canonical.

| Trước task | Hồ sơ cần chuẩn bị |
|---|---|
| M0-01 | Audit binary/build/thiết bị, cấu hình debug/Compatibility trong quyền AUTOPILOT; không tạo lại project hoặc đổi release signing |
| M1/M2 | Camera/FOV, hình học arena, input/aim và HUD thử trên Android |
| M3 | ID/handler chiêu mẫu, damage/chakra/timing, phân loại effect và fixture; dùng Thế thân 25%/3s/60s đã duyệt |
| M4 | Allowlist/tiên quyết/gate, lịch XP/SP/Ryō và vòng đời effect khi thay slot |
| M5 | Số ô/stack, radius/TTL, nhóm loot/target, bảng drop thử và ledger bảo đảm xử lý một lần |
| M6A | Map/spawn và lịch/damage bo cho mục tiêu 20–25 phút; kiểm không trụ vô hạn |
| M3-NET/M7 | Godot server riêng + ENet local/LAN theo mặc định AUTOPILOT; đặc tả command/replication/visibility, thử profile rồi điều chỉnh; backend dịch vụ DEFERRED |

## 3. SLICE-01 — Phạm vi kiểm chứng đầu tiên

**CHỐT SLICE-02/03:** M6A kiểm chứng Uchiha/Hỏa với hai hướng Hỏa thuật/Ảo thuật, một boss, loot/farm, bo, Thế thân và kết quả solo. M7/M8 hoàn thiện hai người online, mục tiêu 20–25 phút. M6B ba clan/24–36 node là hướng mở rộng `DEFERRED`, không bắt xong mới thử hai người. Danh sách ID và stat thử phải có brief M3/M4; không tự bật toàn bộ Uchiha hoặc T5.

Trước M3, chỉ cần duyệt các chiêu mẫu và stat thử của chúng. Trước M4, chọn clan/hệ/tiền đề được đưa vào allowlist; không cần bật đủ bộ ba clan. Chuẩn bị mỗi build với:

- Node mục tiêu + toàn bộ tiền đề, gate và nguồn tài nguyên; tách node tiến trình khỏi các slot thực sự sử dụng.
- Mốc bắt đầu chơi được, mốc chuyên sâu và phương án khi không nhận tư liệu hiếm.
- Counterplay và tình huống dùng; hai build khác nhau về quyết định/hành vi có thể quan sát, không chỉ tên hoặc VFX.

**Nghiệm thu quyết định:** xác định được nội dung nào enable trong từng mode, chiêu nào là fixture và tiêu chí giữ/mở rộng/thu nhỏ slice. Không đặt số node là thước đo duy nhất của độ vui.

## 4. MATCH-01 và LIFE-01 — Trạng thái trận và sinh tồn

**Khung trạng thái đề xuất, chưa phải luật runtime:**

| Đối tượng | Trạng thái ứng viên | Cần xác định trước code |
|---|---|---|
| Trận | preparing, running, resolving, finished | Thời điểm bắt đầu đồng hồ; ưu tiên điều kiện kết thúc; result phát một lần |
| Nhân vật solo | alive, eliminated; spectating là trạng thái xem | Thế thân xử lý trước khi chết; không có death → respawn |
| Thế thân | số cuộn + effect/cooldown theo policy | Tự kích hoạt, tiêu cuộn, HP hồi, ẩn, chain và nhiều hit cùng tick |
| Vòng bo | waiting, shrinking, settled theo phase | Biên, thông báo, damage và trạng thái vùng cuối |
| Loot/pity | pending, settled, choice_pending, delivered | Khi nào hết tranh nhặt, chốt miss, chọn và giao vật phẩm một lần |

Với mỗi cạnh chuyển trạng thái, phải ghi `event`, điều kiện, authority, tài nguyên bị ảnh hưởng và event kết quả. Các tên tiếng Anh trên là ứng viên để viết spec, không tự thêm enum vào code.

**Đặc tả còn cần cho task match:** bán kính spawn an toàn/vùng hợp lệ, lịch bo/damage và phân loại effect/shield. HP/ẩn/cooldown đã chốt 25%/3s/60s cho thử nghiệm; cả hai chết cùng tick thì hòa; disconnect không tự loại. Hit khác sau kích hoạt xét HP mới/cooldown đã chạy, không tạo miễn damage.

**Kịch bản bắt buộc:**

1. Người kết liễu nhận XP/Ryō, người khác tranh được loot; pity của từng người đủ điều kiện được xét riêng.
2. Spawn nhận đúng một cuộn; hết cuộn thì chết/bị loại; không tạo hồi sinh hoặc nút Thế thân thủ công.
3. Lethal hit từ combat/vòng bo: còn cuộn và cooldown sẵn sàng thì tiêu, hồi HP/tàng hình rồi bắt đầu cooldown trước kill; event trùng không tiêu lại. Cooldown đang chạy thì hit gây chết vẫn giết dù còn cuộn.
4. Hai người chết cùng tick; cả hai còn sống sau 25 phút; disconnect và yêu cầu nhận result lặp. Mốc mục tiêu không tự phân thắng thua.
5. Nhiều hit khác nhau cùng tick, DOT, reveal/CC và damage vòng bo sau kích hoạt theo policy được duyệt; summon của người bị loại không tiếp tục chiến đấu thay chủ.

**Đề xuất cho M6A:** map nhỏ với loot/farm, vòng bo và kịch bản đối thủ mô phỏng để kiểm các nhánh kết thúc solo. Mode đội và trụ hồi sinh không thuộc scope; không tái đưa cứ điểm buff vào mốc sau.

## 5. ECON-01 và LOOT-01 — Tiến trình và quyền thưởng

**Bảng cần duyệt:**

| Hợp đồng | Nội dung phải có |
|---|---|
| Level / XP | XP mỗi cấp, nguồn nhận, vùng/điều kiện tham gia, cách chia khi nhiều người; XP dư ở cap |
| SP | SP lúc spawn, từng mốc cấp/trận, tổng ngân sách 12 SP mục tiêu; cấp bù khi nhảy nhiều level |
| Ryō | Thu nhập theo nguồn, sink mua node/đồ; solo không rơi hoặc chuyển tiền khi chết theo LOOT-04 |
| Vật phẩm | Chủ sở hữu cá nhân/đội/công khai, quyền nhặt và hết hạn; dùng/tiêu/chuyển đổi |
| Tham gia | Last-hit, damage, heal, CC, hỗ trợ mục tiêu, bán kính/cửa sổ thời gian; chết/disconnect trước payout |
| Payout | Reward event duy nhất và người nhận hợp lệ; reconnect/retry không tạo thưởng thêm |

**CHỐT ECON-02/REWARD-02/LOOT-02:** giữ XP/SP/Ryō; bên kết liễu nhận quỹ XP/Ryō (solo là một người), cuộn/mảnh hiếm rơi công khai cho mọi người tranh nhặt. Payout tiền/XP và sở hữu vật phẩm world là hai hợp đồng riêng. Chia thưởng trong đội lưu làm policy tương lai.

**Đề xuất:** M4 có kinh tế tối thiểu với nguồn thưởng cố định; M5 mới thêm elite, inventory và ngẫu nhiên. Trade giữa người chơi chưa thuộc phạm vi mặc định, chỉ mở khi có quyết định và task riêng.

**Kiểm chứng trước cân bằng:** mô phỏng thu nhập cho người farm, người hỗ trợ, đội đang thua và người chết; ghi time-to-T2/T3/T4, SP đã dùng và nguyên nhân bế tắc. Không dùng level theo đồng hồ để giả kết quả progression. Nguồn PvE ổn định cần được thử cả khi đội mạnh kiểm soát tài nguyên.

**Bất biến kế thừa:** authority tính thưởng; một reward không được nhận lặp cho cùng người; mua/consume phải atomic; client không quyết định drop hoặc số tiền. Định danh payout phải phân biệt một sự kiện có nhiều người nhận hợp lệ với nhận trùng của cùng một người.

## 6. PITY-01 — Chốt ranh giới bảo hiểm

**CHỐT PITY-02:** Product Owner chọn phương án mở quyền chọn ngay trong reward lượt thứ tư nếu ba lượt trước và lượt thứ tư đều không nhận mảnh mục tiêu. Diễn giải bản cũ "bốn lượt trượt, lượt thứ năm mới được chọn" đã được thay thế; GDD/SKILL_SYSTEM/catalog cùng theo ranh giới mới.

**CHỐT PITY-03/04/05/06 và LOOT-03/05:** tham gia đủ 5% max HP/30s cuối, sống trong vùng khi mục tiêu chết; không nhận mảnh mục tiêu, kể cả bị cướp, là miss. Settle sau khi toàn bộ mảnh hiếm lượt đó nhặt/hết hạn; reset theo nhóm khi nhận mục tiêu/bảo hiểm hoặc đổi mục tiêu. Mảnh chọn vào túi, đầy thì chờ riêng không bị cướp. Quyền pity độc lập với payout kết liễu.

**PITY-01 — brief M5:** xác định nhóm/mảnh cụ thể, bán kính/TTL, target revision, event ledger, thứ tự settle và lưu claim chờ. Không sửa kết quả cũ khi đổi mục tiêu, không dùng miss cũ cho mục tiêu mới, không nhân quyền khi đầy túi/reconnect. Nếu không có ứng viên hợp lệ, không tự bypass gate hoặc tự đổi thành tiền; báo lỗi cấu hình trong fixture trước khi bật nhóm loot đó.

**Chống thao tác UI ảnh hưởng RNG:** counter theo `(match_id, player_id, loot_group_id)`; đổi filter/preset không tự sinh lượt thưởng/reset. Chỉ thao tác đổi mục tiêu loot thực sự áp dụng reset theo PITY-06; đăng ký trước lượt và lưu cùng reward, không chọn mục tiêu sau khi thấy loot của lượt đó.

**Kiểm chứng:** miss liên tiếp tại ranh giới 3/4/5; trúng trước ngưỡng; nhóm A/B độc lập; hai người độc lập; retry cùng reward; reconnect khi đang chọn; không có mảnh hợp lệ; đổi mục tiêu. Chưa giải quyết PITY-01 thì task pity chưa `READY`; loot cố định vẫn có thể được xét riêng.

## 7. BUILD-01 và SKILL-01 — Học, trang bị và quyền thực thi

Tách ba thao tác trong spec: **learn** thay đổi tiến trình và trả chi phí; **equip** chọn node đã học vào slot; **cast** dùng ability theo điều kiện combat. Tier T5 không tự đồng nghĩa ultimate; node mở thức tỉnh có thể là tiền đề của một node T5 khác.

**CHỐT BUILD-02/LOADOUT-01:** không hoàn điểm trong trận; giữ node đã học, đổi hướng bằng SP còn lại và kỹ năng sở hữu. Đổi kỹ năng trang bị chỉ khi ngoài giao tranh ở bất kỳ vị trí nào, cooldown không bị reset do thay slot. Không yêu cầu tới điểm huấn luyện để equip. Hoàn trả một transaction mua thất bại không được hiểu thành quyền hoàn điểm.

**BUILD-01 — brief M4:** trạng thái buff/passive/summon khi tháo và cách biểu diễn transaction learn/equip/hit. COMBAT-02 đã chốt timer 5s; kiểm sau cập nhật combat của tick, BUILD-03 từ chối học trong combat hoặc sau bị loại. Đổi luật hoàn điểm cần quyết định thay thế BUILD-02, không tự làm bằng preset.

**CHỐT NATURE-01:** hai hệ thông thường; hệ thứ ba chỉ qua sự kiện hiếm, không tự được phép chỉ vì có cuộn thường. Cần predicate đếm hệ/quyền sự kiện, giữ khóa khi sự kiện chưa triển khai; không thay gate huyết kế bằng quyền nguyên tố.

**Schema tương lai cần phân biệt:**

- Kiểu node (`progression/root/passive/active/ultimate/trait/tool/substitution`) và loại slot; `node_kind_hint` hiện chỉ là gợi ý.
- Quyền xuất hiện/học theo mode; approval của tiến trình; gate resolver; binding effect/runtime đã triển khai cho kiểu node đó.
- Node tiến trình thuần không cần damage/hitbox/VFX; passive cần effect handler phù hợp; active cần ability definition. Mọi loại đều cần hành vi đã duyệt và kiểm chứng trước khi enable.
- `metadata.approved_for_runtime=false`, `implementation_status=design_only` và gate chưa resolve hiện không được bypass bằng allowlist. Cách xuất bản tập node approved phải được quyết định trước khi bật runtime; không sửa toàn catalog thành implemented.

**Bảng baseline tính từ catalog ngày 2026-10-16:**

| Tập node trong ví dụ SKILL_SYSTEM §12 | SP tối thiểu | Ryō theo giá catalog |
|---|---:|---:|
| Lôi Sát | 8 | 1.670 |
| Hỏa Ảo | 11 | 2.410 |
| Nhu Quyền | 6 | 1.120 |
| Ảnh Ấn | 5 | 840 |
| Băng Ảo | 6 | 1.290 |
| Trùng Hộ | 5 | 1.010 |
| Khôi Lỗi Độc | 6 | 1.290 |
| Phong Nha | 9 | 1.850 |

Tính hợp toàn bộ tiền đề, node dùng chung một lần, T0 miễn phí, mỗi nhóm OR chọn phương án chi phí thấp nhất. Đây là chi phí graph cho đúng tập node minh họa; **chưa xét gate/item, modifier chưa định nghĩa, slot hoặc sức mạnh**. Không yêu cầu các tập node khác nhau phải tốn bằng nhau. Task validator sau này cần fixture với nhiều nhóm OR dùng chung tiền đề để tránh cộng đường độc lập bị đếm trùng.

**Kiểm chứng:** ngân sách tại từng mốc SP; đủ/thiếu tài nguyên; exclusive packages; gate chưa triển khai; dependency bị tắt trong allowlist; đổi slot khi cooldown; đường T4 không RNG; tính hợp lệ của cả loadout, không chỉ một node đích.

## 8. FUSE-01 — Công thức và phản ứng

Mỗi synergy được đưa vào runtime phải có hợp đồng: `participant_scope`, prerequisites, trigger, kết quả/effect hoặc node kết quả, điều kiện phải learn/equip, team/target filter, chủ sở hữu damage/assist, thời hạn, cooldown và giới hạn chain. Đây là **field đề xuất**, chưa nằm trong schema catalog hiện hành.

- **World reaction:** xác định vùng/thời điểm chồng lấp và bên nào được hưởng/bị ảnh hưởng; không tự cấp node mua; không lặp kích hoạt vô hạn từ kết quả của chính phản ứng.
- **Build fusion:** xác định một actor sở hữu toàn bộ tiền đề và có cần mua/trang bị node kết quả. Các cặp ứng viên để duyệt là SY05 → FUSE_BYAKU_LIGHT, SY06 → FUSE_EYE_KEN, SY08 → FUSE_SHADOW_TRAP; không bật tự động chỉ vì tên giống nhau.
- **Team fusion:** xác định đóng góp được phân bố giữa đồng đội thế nào, ai kích hoạt và ai trả tài nguyên. SY10 và FUSE_WIND_FIRE_TOAD cần phân biệt quyền phối hợp của đội với điều kiện học một node của cá nhân.
- **Bloodline:** giữ gate huyết kế kể cả khi có đủ nature; không mở chỉ từ phản ứng nguyên tố.

**Trường hợp phải làm rõ:** SY04 dùng token WIND + BASE_WEAPON, còn FUSE_WIND_TOOL cần WIND_BLADE + BASE_WEAPON. Chọn hai biến thể riêng hoặc một binding có điều kiện mua rõ; không để hai handler cùng cấp một hiệu ứng ngoài ý muốn. Không ép 12 synergy phải khớp 1–1 với 15 node lai.

## 9. COMBAT-01 và VIEW-01 — Hợp đồng combat và thao tác

**Trước mỗi ability mẫu:** mô tả input/aim/target, startup-active-recovery, khi bắt đầu trừ chakra và cooldown, ngắt/cancel/hoàn tài nguyên, hit/LOS/team filter, số hit trên mỗi target và trạng thái caster chết. Tất cả stat thử phải có nhãn prototype, mục đích và người duyệt; không suy từ rank/tên thuật.

Với CC và Thế thân, cần bảng: effect nào chặn di chuyển/cast/Thế thân; nhóm DR, cửa sổ thoát, miễn nhiễm và quy tắc cộng dồn. Nếu cast nhận trước mà giải quyết sau khi mục tiêu chết/ra ngoài range, phải có kết quả xác định theo archetype.

**M2 dùng HUD placeholder đủ bố cục đích:** joystick, đánh thường, bốn active, ultimate, nhẫn cụ và indicator cuộn Thế thân bị động. Nút chưa có gameplay ghi disabled; không đòi triển khai đủ ability tại M2. Thử giữ joystick + kéo ngắm + hủy ngắm, thao tác ngoài nút, nhấc ngón, focus loss, notch và mở panel. Thế thân không có nút kích hoạt.

**Vùng nhìn còn mở:** chọn cách so sánh FOV 16:9/20:9, zoom và giới hạn camera; không để đổi setting tùy ý tạo lợi thế ngoài policy. Phân biệt camera thấy được, LOS, stealth/reveal và dữ liệu minimap. Trước online phải xác định state nào được gửi cho đối thủ và spectator; nếu chưa có fog/stealth trong mode thử, ghi rõ mode đó không kiểm chứng các mechanic này.

## 10. TECH-01 — Cấu hình thực tế và rủi ro chuyển online

**Quan sát chỉ đọc ngày 2026-10-16:** `project.godot` khai báo `config/features` chứa `4.7`, `Forward Plus`, driver Windows `d3d12`; chưa khai báo main scene. Đây không phải bằng chứng binary/build engine thực tế hoặc Android đã chạy. Tài liệu kiến trúc đề xuất Compatibility; renderer vẫn cần xác nhận.

**Đề xuất quy trình:** M0 kiểm executable/version đầy đủ, export templates tương ứng và thiết bị; ghi quyết định renderer trước thay cấu hình bằng Editor. Trong F0 giữ nguyên project. Dùng project đang có để kiểm, không tạo lại hoặc ghi đè để đáp ứng checklist.

**Network spike sớm M3-NET:** hai client, một authority thử, movement + một ability + HP. Đo latency/packet loss theo profile được duyệt và ghi tick/input/snapshot. Chưa cần tài khoản, database hoặc Nakama. Prototype offline vẫn là luồng nội dung chính; spike là cổng kiểm rủi ro trước khi mở rộng nội dung, không tự thay ADR backend.

**Trước M7:** duyệt transport/backend từ kết quả spike, command/event contract và reconnect; chốt simulation/snapshot policy, visibility và content version. M7 mới tích hợp progression, inventory, reward và objective đã có.

## 11. Hồ sơ duyệt và Change Log

```text
Decision ID / trạng thái:
Mode và milestone áp dụng:
Vấn đề / các phương án:
Phương án được chọn / lý do / đánh đổi:
Nguồn chính cần cập nhật / data migration nếu có:
Kịch bản kiểm chứng / tiêu chí thất bại:
Product Owner duyệt / ngày:
Bằng chứng kiểm thử / task thực hiện sau này:
```

| Ngày | Phiên bản | Thay đổi |
|---|---|---|
| 2026-10-16 | 1.0 | Tập hợp các câu hỏi thiết kế, phương án đối chiếu và baseline chi phí build để trao đổi |
| 2026-10-16 | 1.1 | Ghi WIN-01/SEAL-01/REVIVE-01 được Product Owner chọn, thay câu hỏi cũ theo hướng sinh tồn và xác định tiêu chí bàn giao bản đặc tả chính thức |
| 2026-10-16 | 1.2 | Ghi ZONE-01/SEAL-02/ELIM-01 được Product Owner chọn: vòng bo, lợi ích phong ấn tách hồi sinh và loại ngay khi cả đội chết hẳn |
| 2026-10-16 | 1.3 | Ghi BUILD-02/NATURE-01/LOADOUT-01 được Product Owner chọn: không hoàn điểm, giới hạn hệ thông thường và thời điểm đổi kỹ năng |
| 2026-10-16 | 1.4 | Ghi REWARD-01/LOOT-02/PITY-02 được Product Owner chọn: chia XP/Ryō, rơi công khai và chọn mảnh ngay lượt thứ tư; còn điều kiện pity trong tranh loot |
| 2026-10-16 | 1.5 | Theo steering mới: solo sinh tồn, bỏ cứ điểm buff, không hồi sinh; một cuộn Thế thân bị động khởi đầu, kích hoạt trước lethal hit kể cả vòng bo, hồi HP/tàng hình; giữ XP/SP/Ryō, chốt kết liễu/pity nhận cá nhân và tách luật đội |
| 2026-10-16 | 1.6 | Chốt SOLO-SUB-05..07: cap hai cuộn, hồi chiêu nội tại, tàng hình vẫn chịu damage và lộ khi gây/nhận damage |
| 2026-10-16 | 1.7 | Chốt MATCH-02/03/04: hai người/trận, chọn vùng/spawn ngẫu nhiên an toàn, mục tiêu 20–25 phút; thêm TASK_BACKLOG và tách mở rộng content/số người khỏi đường nghiệm thu hiện tại |
| 2026-10-16 | 1.8 | Chốt LOOT-04 vật tư rơi khi chết, SOLO-SUB-08 thanh tẩy và BUILD-03 học ngoài giao tranh; thu hẹp câu hỏi còn mở, đồng bộ nguồn luật và backlog |
| 2026-10-16 | 1.9 | Chốt COMBAT-02/SOLO-SUB-09/MATCH-05/06/PITY-04/05: timer 5s, bộ số Thế thân thử, hòa cùng tick, disconnect không tự loại và ngưỡng/settle pity |
| 2026-10-16 | 2.0 | Baseline chính thức Uchiha/Hỏa/hai hướng build cho hai người; reset pity theo nhóm, túi chung giới hạn và claim riêng khi đầy, bo cuối hết vùng an toàn; tách brief từng task khỏi scope mở rộng |
| 2026-10-16 | 2.1 | AUTO-01/ART-01/ACCEPT-01: tự làm/test/art đến M8, generate_image và nghiệm thu cuối; 11 brief kỹ thuật chuyển DELEGATED, thêm profile thử có nguồn, không thay luật gameplay đã chốt |
