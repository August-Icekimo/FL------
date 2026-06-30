# 【人事承辦 審核邏輯】

# === 假別常數定義（減少重複檢查）===
# 補休類假別
vaid_makeups = (35, 36, 37, 38, 109, 110, 111)
# 非特殊假別（常規）- 不需要特別審核
vaid_common = (4, 12, 14, 20, 21) + vaid_makeups
# 公出、公假、補休 - 用於副主管以下排除
vaid_exclude_with_makeups = (4, 7) + vaid_makeups
# 防疫假別
vaid_pandemic = (117, 118, 119, 120)
# 快速排除假別
vaid_quick_exclude = (7, 5, 21)
# 工會會務假
vaid_meeting = (67, 165, 166)

# === 快速全局排除（優先執行）===
#  二廠人事業務督導單位 或 二廠人員(含廠房、駐警、業務企劃中心)  或 高職級 或 快速排除假別
if second == 3 or plevel in (2, 5, 6) or nlevel >= 800 or vaid in vaid_quick_exclude:
    return False

# === 強制進入 (Pass Quick) ===

# --- 特定防疫假強制審核 ---
if vaid in vaid_pandemic:
    return True

# --- 工會會務假特殊邏輯 ---
# 審核工會會務假假別
if vaid in vaid_meeting:
    return True

# --- 副主管以下 + 總廠人員(3,4) 的特殊審核邏輯 ---
if nlevel <= 750 and plevel in (3, 4):
    # 副單位主管(750) 的特定排除條件
    if nlevel == 750:
        if (vaid in (12, 20, 21, 15) and hours <= 8) or vaid in vaid_exclude_with_makeups:
            return False

    # 此人群的強制進入條件：特殊假別或長天數
    if vaid not in vaid_common or hours > 8 or continueDays > 1:
        return True

# --- 非一/二廠副主管以下特定假別排除 ---
if nlevel <= 750 and plevel not in (1, 2) and vaid in vaid_exclude_with_makeups:
    return False

# --- 特定職級與假別審核 ---
# 組長/課長以下(nlevel<=700) 申請公務(6) 且非二廠時進入
if nlevel <= 700 and vaid == 6 and plevel != 2:
    return True

# 預設：不進入人事承辦審核
return False