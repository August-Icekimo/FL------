# 【副主任/副廠長 審核邏輯】

# === 強制跳過 (Block Quick) ===

# --- 假別與身分直接排除條件 ---
# 已簽准之公假(7)不需副主任審核
if vaid==7:
    return False

# 一廠或二廠的工會會務假(67, 165, 166)不需副主任審核
if plevel in (1, 2) and vaid in (67, 165, 166):
    return False

# 非「副主任2督導」(second!=2)的人員，一律不需審核
if second!=2: #非指定督導
   return False

# 職級為副單位主管(750)含以上者，不需副主任審核 (僅審核組長/課長以下)
if nlevel>=750:
    return False

# --- 時數與天數排除條件 ---
# 一班人員(100)申請遞延休假(21)小於8小時，不進入審核
if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
    return False

# 針對一廠或二廠的副組長/副課長以下(nlevel<=650)人員，若是請「單日或更短(連續天數<=1)」的特定假別，不需副主任審核：
# 1. 一天以內(時數<=8) 的 事假(12)、休假(20)、病假(14)
# 2. 或 公出(4)、已簽准公假(7)、各種補休(35-38, 109-111)
if plevel in (1, 2) and nlevel<=650 and ((vaid in (12, 14, 20) and hours<=8) or vaid in (4, 7, 35, 36, 37, 38, 109, 110, 111)) and continueDays<=1:
    return False

# === 進入條件 ===

# --- 特定條件直接進入審核 ---
# 針對一廠或二廠的廠長室人員(master=1)，職級副組長/副課長以下(nlevel<=650)，且屬於「副主任2督導」(second=2)者，只要不是工會會務假(67, 165, 166)，皆需審核
if plevel in (1, 2) and master==1 and nlevel<=650 and second==2 and vaid not in (67, 165, 166):
    return True

# --- 特殊情況進入審核 ---
# 工會會務假(67, 165, 166)：若職級為組長/課長(700)，或職級為副組長/副課長(650)且身分標記為「只有副組長(onlySecond=1)」，則需審核
if vaid in (67, 165, 166) and (nlevel==700 or (nlevel==650 and onlySecond==1)):
    return True

# 若通過上述所有排除條件，預設進入副主任/副廠長審核
return True
