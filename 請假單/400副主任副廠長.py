# 【副主任/副廠長 (督導1) 審核邏輯】 (與 450副主任副廠長 互補)

# === 假別常數定義 ===
# 補休類假別
vaid_makeups = (35, 36, 37, 38, 109, 110, 111)
# 短期假別（8小時以內）
vaid_short_term = (12, 14, 20)
# 公出、公假、補休（短假排除用）
vaid_short_exclude = (4, 7, 35, 36, 37, 38, 109, 110, 111)
# 工會假
vaid_meeting = (67, 165, 166)
# 製證中心特殊假別
vaid_special = (13, 16, 18, 26, 27, 28, 31, 93)

# === 快速全局排除（優先檢查）===
# 公假、指定督導身分排除、職級過高、一般人員遞延休假短時數
if vaid == 7 or second == 2 or nlevel >= 750 or (nlevel == 100 and vaid == 21 and hours < 8):
    return False

# 一二廠副組長以下的單日短假
if plevel in (1, 2) and nlevel <= 650 and continueDays <= 1 and (vaid in vaid_short_term and hours <= 8 or vaid in vaid_short_exclude):
    return False

# === 強制進入條件 ===

# --- 製證流程特定部門 ---
# 資通機電部門或品檢封裝空白部門
if secondDept == 3 and nlevel <= 650:
    return True

if secondDept == 4:
    return True

# 品檢封裝製證部門的長天數或特殊假別
if secondDept == 5 and (hours > 8 or continueDays > 1 or vaid in vaid_special):
    return True

# --- 廠長室人員 ---
if plevel in (1, 2) and master == 1 and nlevel <= 650 and second == 1:
    return True

# --- 秘書室副組長特定短假 ---
if plevel == 0 and master == 2 and nlevel == 650 and continueDays <= 1 and (vaid in vaid_short_term and hours <= 8 or vaid in vaid_short_exclude):
    return True

# --- 政風流程 ---
if linkuncheng == 1:
    return True

# --- 工會假特定職級 ---
if vaid in vaid_meeting and (nlevel == 700 or (nlevel == 650 and onlySecond == 1)):
    return True

# 預設進入副主任/副廠長(督導1)審核
return True
