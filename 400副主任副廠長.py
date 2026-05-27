# 【副主任/副廠長 (督導1) 審核邏輯】 (與 450副主任副廠長 互補)

# === 強制跳過 (Quick Fail) ===

# --- 全局假別排除條件 ---
# 已簽准之公假(7)不需此關卡審核
if vaid == 7:
    return False

# # 工會理監事會務假(67) 預設不進入此關卡審核 (下方有特殊例外)
# if vaid == 67:
#     return False

# --- 遞延休假時數判斷 ---
# 一班人員(100)申請遞延休假(21)小於8小時，不進入審核
if nlevel == 100 and vaid == 21 and hours < 8: #一般人員申請遞延休假小於8HR不進入
    return False

# --- 督導身分與職級 排除條件 ---
# 排除「副主任2督導」(second=2) 的人員 (這些人交由 450副主任副廠長 審核)
if second == 2: #非指定督導
    return False

# 職級為副單位主管(750)含以上者，不需本關審核 (僅審核組長/課長以下)
if nlevel >= 750:
    return False

# --- 針對一/二廠副主管以下 短假排除條件 ---
# 針對一廠或二廠(plevel=1,2)的副組長/副課長以下(nlevel<=650)人員：
# 若是請「單日或更短(連續天數<=1)」的特定假別，不需副主任審核：
# 1. 一天以內(時數<=8) 的 事假(12)、休假(20)、病假(14)
# 2. 或 公出(4)、已簽准公假(7)、各種補休(35-38, 109-111)
if plevel in (1, 2) and nlevel <= 650 and ((vaid in (12, 14, 20) and hours <= 8) or vaid in (4, 7, 35, 36, 37, 38, 109, 110, 111)) and continueDays <= 1:
    return False

# === 進入條件 ===

# --- 特定部門/流程 強制審核條件 ---
# 製證中心組流程設定-資通機電 (secondDept=3) 且 職級為副組長/副課長以下 (nlevel<=650) 者，需審核
if secondDept == 3 and nlevel <= 650: #彬鴻修改
    return True

# 製證及品檢封裝股流程-空白 (secondDept=4) 者，不分條件直接進入審核
if secondDept == 4: #彬鴻修改
    return True

# 製證及品檢封裝股流程-品檢封裝製證 (secondDept=5) 且 符合特定假別或長天數條件者，需審核
# 條件為：請假時數>8、連續天數>1、或 特定假別(婚假13,喪假16,家庭照顧18,流產26,娩假27,產檢28,非本廠公假31,生理假93)
if secondDept == 5 and (hours > 8 or continueDays > 1 or vaid in (13, 16, 18, 26, 27, 28, 31, 93)): #彬鴻修改
    return True

# --- 一/二廠與總部 特定審核條件 ---
# 針對一廠或二廠(plevel=1,2)，廠長室人員(master=1)，副組長/副課長以下(nlevel<=650)
# 且 屬於「副主任1督導」(second=1 或 <=1)，則進入審核
if plevel in (1, 2) and master == 1 and nlevel <= 650 and second == 1:
    return True

# 針對總部/非廠區(plevel=0)，秘書室(master=2)，職級剛好為副組長/副課長(nlevel=650)
# 若是請「單日以內(<=8HR)」的特定假別 (事假12/休假20/病假14 或 公出4/公假7/各種補休)，需進入審核
if plevel == 0 and master == 2 and nlevel == 650 and ((vaid in (12, 14, 20) and hours <= 8) or vaid in (4, 7, 35, 36, 37, 38, 109, 110, 111)) and continueDays <= 1:
    return True

# 特殊政風流程 (linkuncheng=1) 者，需審核
if linkuncheng == 1:
    return True

# --- 特殊情況進入審核 (這段似乎與最上方的 vaid==67 衝突，若走到這代表前段條件沒擋下或這是另一種邏輯分支，保留原邏輯) ---
# 工會會務假(67, 165, 166)：若職級為組長/課長(700)，或職級為副組長/副課長(650)且身分標記為「只有副組長(onlySecond=1)」，則需審核
if vaid in (67, 165, 166) and (nlevel == 700 or (nlevel == 650 and onlySecond == 1)): #and master!=2 and master!=4:
    return True
# 需求中有人事室人員還要經過總經理室管理師

# 若通過上述所有排除條件，預設進入副主任/副廠長(督導1)審核
return True
