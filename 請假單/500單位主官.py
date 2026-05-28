# 【500 單位主官 審核邏輯】
# 若符合以下任一「排除條件」，則回傳 False (跳過此關卡)；否則回傳 True (需經過審核)。

# 判斷是否為單日以內 (continueDays <= 1) 的短時數事假(12)/病假(14)/休假(20)，或是公出(4)/公假(7)/各種補休
is_short_leave = continueDays <= 1 and (
    (vaid in (12, 14, 20) and hours <= 8) or 
    vaid in (4, 7, 35, 36, 37, 38, 109, 110, 111)
)

exclude_conditions = (
    # 排除 1: 假別為「公假(本廠公務)」(vaid == 7)
    vaid == 7 or
    # 排除 2: 職級為「單位主管」(nlevel == 800) 含以上者 (僅審核副單位主管 750 以下)
    nlevel >= 800 or
    # 排除 3: 第一/二工廠 (plevel == 1, 2) 且為「副組長/副課長」以下 (nlevel <= 650) 的單日/短時數請假
    (plevel in (1, 2) and nlevel <= 650 and is_short_leave) or
    # 排除 4: 秘書室/總經理室 (master == 2, 4) 且為「組長/課長」以下 (nlevel <= 700) 的單日/短時數請假
    (master in (2, 4) and nlevel <= 700 and is_short_leave)
)

# 若未觸發任何排除條件 (包含原程式碼註記的製證中心、政風流程等特定人員)，皆依預設進入審核
return not exclude_conditions
