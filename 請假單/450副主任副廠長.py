# 【副主任/副廠長 (督導2) 審核邏輯】 (與 400副主任副廠長 互補)

# === 假別常數定義 ===
# 短期假別（8小時以內）
vaid_short_term = (12, 14, 20)
# 公出、公假、補休（短假排除用）
vaid_short_exclude = (4, 7, 35, 36, 37, 38, 109, 110, 111)
# 工會假
vaid_meeting = (67, 165, 166)

# === 快速全局排除（優先檢查）===
# 公假、非指定督導身分、職級過高、一般人員遞延休假短時數、一二廠工會假
if vaid == 7 or second != 2 or nlevel >= 750 or (nlevel == 100 and vaid == 21 and hours < 8) or (plevel in (1, 2) and vaid in vaid_meeting):
    return False

# 一二廠副組長以下的單日短假
if plevel in (1, 2) and nlevel <= 650 and continueDays <= 1 and (vaid in vaid_short_term and hours <= 8 or vaid in vaid_short_exclude):
    return False

# === 強制進入條件 ===

# --- 廠長室人員（非工會假） ---
if plevel in (1, 2) and master == 1 and nlevel <= 650 and vaid not in vaid_meeting:
    return True

# --- 工會假特定職級 ---
if vaid in vaid_meeting and (nlevel == 700 or (nlevel == 650 and onlySecond == 1)):
    return True

# 若通過上述所有排除條件，預設進入副主任/副廠長(督導2)審核
return True
