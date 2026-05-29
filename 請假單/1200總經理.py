# 判斷是否需要經過「總經理」簽核關卡

# === 強制進入 (Pass Quick) ===

# 職級為單位主管 (800) 或 副總 (900)，請假需經過總經理
if nlevel in (800, 900):
    return True

# 職級為副單位主管 (750) 且所屬部門為第一工廠 (1) 或第二工廠 (2)，
# 只要假別「不是」公假(本廠公務) (7)，就需經過總經理
if nlevel==750 and plevel in (1, 2) and vaid!=7:
    return True

# === 排除條件 ===

# 若假別為工會會務假 (67, 165, 166)，不經過總經理
if vaid in (67, 165, 166):
    return False

# 一般人員 (100) 申請遞延休假 (21) 且請假時數小於8小時不進入此關卡
if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
    return False

# 預設不經過此關卡
return False
