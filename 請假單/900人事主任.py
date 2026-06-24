# 判斷是否需要經過「人事主任」簽核關卡

# === 假別常數定義（減少重複檢查）===
# 補休類假別
vaid_makeups = (35, 36, 37, 38, 109, 110, 111)
# 常規假別（不需特殊審核）
vaid_common = (4, 7, 12, 14, 20, 21) + vaid_makeups
# 公出、公假、補休 - 用於副主管排除
vaid_exclude_with_makeups = (4, 7) + vaid_makeups
# 防疫假及會務假
vaid_meeting_pandemic = (67, 117, 118, 119, 120, 165, 166)
# 副主管(750)短期假別
vaid_750_short_term = (12, 15, 20, 21)
# 快速排除假別（包含公務6）
vaid_quick_exclude = (5, 6, 7, 21)

# === 快速全局排除（優先執行）===
# 規則1：快速排除假別
if vaid in vaid_quick_exclude:
    return False

# 規則2：部門/職級排除（但防疫會務假例外）
if (plevel in (1, 2) or nlevel >= 800) and vaid not in vaid_meeting_pandemic:
    return False

# === 強制進入 (Pass Quick) ===

# --- 防疫及工會會務假強制進入 ---
if vaid in vaid_meeting_pandemic:
    return True

# --- 副主管以下 + 總廠人員(3,4) 的長天數或特殊假別 ---
if nlevel <= 750 and plevel in (3, 4):
    if vaid not in vaid_common or hours > 8 or continueDays > 1:
        return True

# === 排除條件 ===

# --- 副單位主管(750) 特定短天數/假別排除 ---
if nlevel == 750 and ((vaid in vaid_750_short_term and hours <= 8) or vaid in vaid_exclude_with_makeups):
    return False

# --- 非一/二廠副主管以下的補休及公出排除 ---
if nlevel <= 750 and plevel not in (1, 2) and vaid in vaid_exclude_with_makeups:
    return False

# 預設跳過此關卡
return False