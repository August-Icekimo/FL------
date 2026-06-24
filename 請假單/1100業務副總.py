# 判斷是否需要經過「業務副總」簽核關卡

# === 假別常數定義（減少重複檢查）===
# 補休類假別
vaid_makeups = (35, 36, 37, 38, 109, 110, 111)
# 常規假別
vaid_common = (4, 7, 12, 14, 20, 21) + vaid_makeups
# 公出、公假、補休
vaid_exclude_with_makeups = (4, 7) + vaid_makeups
# 快速排除假別
vaid_quick_exclude = (6, 7)


# === 快速全局排除（優先執行）===
# 部門排除、特定假別或一般人員遞延休假
if plevel in (1, 2, 3, 6) or vaid in vaid_quick_exclude or (nlevel == 100 and vaid == 21 and hours < 8):
    return False

# === 強制進入 (Pass Quick) ===
# --- 公差（業務副總督導的公差） ---
if plevel == 4 and vaid == 5:
    return True
# --- 工會理監事會務假（工務副總督導且低於副總） ---
if vaid == 67 and plevel == 4 and nlevel < 900:
    return True

# --- 製證中心資通機電的公差 ---
if secondDept == 3 and nlevel <= 750 and vaid == 5:
    return True

# --- 副主管以下 + 非一二三廠的長天數或特殊假別 ---
if nlevel <= 750 and plevel not in (1, 2, 3):
    if vaid not in vaid_common or hours > 8 or continueDays > 1:
        return True

# === 排除條件 ===

# --- 副主管以下 + 非一二三廠的補休及公出排除 ---
if nlevel <= 750 and plevel not in (1, 2, 3) and vaid in vaid_exclude_with_makeups:
    return False

# 預設不經過此關卡
return False
