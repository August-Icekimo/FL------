# 判斷是否需要經過「工務副總」簽核關卡

# === 假別常數定義（減少重複檢查）===
# 補休類假別
vaid_makeups = (35, 36, 37, 38, 109, 110, 111)
# 常規假別
vaid_common = (4, 7, 12, 14, 20, 21) + vaid_makeups
# 公出、公假、補休
vaid_exclude_with_makeups = (4, 7) + vaid_makeups
# 防疫假
vaid_pandemic = (117, 118, 119, 120)
# 快速排除假別
vaid_quick_exclude = (5, 6, 7)
# 工會假
vaid_meeting = (67, 165, 166)
# 製證中心資通機電的特殊假別
special_vaids_3 = (13, 16, 18, 26, 27, 28, 31, 93)

# === 快速全局排除（優先執行）===
# 工會假或快速排除假別或一般人員遞延休假
if vaid in vaid_meeting or vaid in vaid_quick_exclude or (nlevel == 100 and vaid == 21 and hours < 8):
    return False

# === 強制進入 (Pass Quick) ===

# --- 防疫假強制進入 ---
if vaid in vaid_pandemic:
    return True

# --- 業務企劃中心長天數 ---
if plevel == 6 and (hours > 8 or continueDays > 1):
    return True

# --- 工務副總督導的公差 ---
if plevel == 3 and vaid == 5:
    return True

# --- 製證中心資通機電的特殊假別或長天數 ---
if secondDept == 3 and nlevel <= 750 and (hours > 8 or continueDays > 1 or vaid in special_vaids_3):
    return True

# --- 製證品檢封裝股長天數公假(非本廠) ---
if secondDept in (4, 5) and hours > 8 and vaid == 31:
    return True

# --- 副主管以下 + 工務副總督導的長天數或特殊假別 ---
if nlevel <= 750 and plevel == 3:
    if vaid not in vaid_common or hours > 8 or continueDays > 1:
        return True

# === 排除條件 ===

# --- 副主管以下 + 工務副總督導的補休及公出排除 ---
if nlevel <= 750 and plevel == 3 and vaid in vaid_exclude_with_makeups:
    return False

# 預設不經過此關卡
return False
