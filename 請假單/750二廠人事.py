# 【二廠人事 審核邏輯】 (與 700人事承辦 互補的 "另一端")

# === 假別常數定義（減少重複檢查）===
# 補休類假別
vaid_makeups = (35, 36, 37, 38, 109, 110, 111)
# 常規假別（不需特殊審核）
vaid_common = (4, 7, 12, 14, 20, 21) + vaid_makeups
# 公出、公假、補休 - 用於副主管排除
vaid_exclude_with_makeups = (4, 7) + vaid_makeups
# 快速排除假別
vaid_quick_exclude = (7, 5, 21)
# 副主管(750)短期假別
vaid_750_short_term = (12, 20, 21, 15)

# === 快速全局排除（優先執行）===
# 快速排除假別或高職級
if vaid in vaid_quick_exclude or nlevel >= 800:
    return False

# === 強制進入 (Pass Quick) ===

# --- 理監事會務假特殊邏輯 ---
# vaid=67：若身分屬於二廠相關（second=3 或 派駐二廠），則交由二廠人事審核
if vaid == 67 and (second == 3 or onlySecond == 2 or secondDept == 1):
    return True

# --- 公務(6) 審核 ---
# 第二工廠(plevel=2) 或 二廠人事業務範圍(second=3) 的組長/課長以下(nlevel<=700)
if vaid == 6 and (plevel == 2 or second == 3) and nlevel <= 700:
    return True

# --- 業務企劃中心(plevel=6) 特殊假別或長天數審核 ---
if plevel == 6 and (vaid not in vaid_common or hours > 8 or continueDays > 1):
    return True

# --- 二廠人事管轄(second=3) 的長天數或特殊假別審核 ---
# second=3 且 副主管以下(nlevel<=750) 且 非第一/二工廠
if second == 3 and nlevel <= 750 and plevel not in (1, 2):
    if vaid not in vaid_common or hours > 8 or continueDays > 1:
        return True

# === 排除條件 ===

# --- 非一/二廠 副主管以下的補休及公出排除 ---
if nlevel <= 750 and plevel not in (1, 2) and vaid in vaid_exclude_with_makeups:
    return False

# --- 副單位主管(750) 特定短天數/假別排除 ---
if nlevel == 750 and ((vaid in vaid_750_short_term and hours <= 8) or vaid in vaid_exclude_with_makeups):
    return False

# 預設：不進入二廠人事審核
return False
