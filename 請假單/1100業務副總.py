# 判斷是否需要經過「業務副總」簽核關卡

# === 強制進入 (Pass Quick) ===

# 若為公差 (5) 或 工會會務假 (67, 165, 166)，且非屬工務副總督導 (plevel!=3)，且職級低於副總 (nlevel<900)，需由業務副總審核
if vaid in (5, 67, 165, 166) and plevel!=3 and nlevel<900:
    return True

# 彬鴻修改: 製證中心組流程設定-資通機電 (secondDept==3) 且職級為副單位主管(含)以下 (nlevel<=750)，申請公差 (5) 需審核
if secondDept==3 and nlevel<=750 and vaid==5:
    return True

# 職級在副單位主管(含)以下 (nlevel<=750)，且非屬一廠、二廠、工務副總督導，
# 只要「不屬於」一般較短天數之假別 (公出4/公假(本廠)7/各類補休/休假20/遞延休假21/事假12/病假14)，
# 「或者」請假時數 > 8 小時，
# 「或者」連續請假天數 > 1 天，就需要業務副總審核
if nlevel<=750 and plevel not in (1, 2, 3) and (vaid not in (4, 7, 12, 14, 20, 21, 35, 36, 37, 38, 109, 110, 111) or hours>8 or continueDays>1):
    return True

# === 排除條件 ===

# 業務企劃中心不經過此關卡
if plevel == 6: #業務企劃中心
    return False

# 假別為公假(本廠公務) (7) 或 公務 (6) 不經過此關卡
if vaid in (6, 7):
    return False

# 第一工廠 (1)、第二工廠 (2)、工務副總督導 (3) 的單，不經過業務副總
if plevel in (1, 2, 3):
    return False

# 一般人員 (100) 申請遞延休假 (21) 且請假時數小於8小時不進入此關卡
if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
    return False

# 職級在副單位主管(含)以下 (nlevel<=750)，且非屬一廠、二廠、工務副總督導，
# 申請公出 (4)、公假(本廠公務) (7)、或各類補休 (35加班, 36出差, 37值班, 38公務, 109行政值班, 110電機值班, 111警衛幹部值班) 不進入此關卡
if nlevel<=750 and plevel not in (1, 2, 3) and vaid in (4, 7, 35, 36, 37, 38, 109, 110, 111):
    return False

# 預設不經過此關卡
return False
