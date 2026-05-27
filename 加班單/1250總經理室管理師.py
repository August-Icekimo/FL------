# --- 預設不予審核 ---
# --- 進入審核條件 (Quick Pass) ---

# 若職級在組長/課長(700)以下(即<700)，且人員群組-主「非」總經理室人員(4)，需進入審核
if nlevel < 700 and master != 4:
    return True

if onlyHRDept==1: 
    # 針對人事室人員中，職級在「副單位主管」(750)(含)以下，經過總經理室管理師簽核
    if nlevel<=750: 
        return True
    # 人事室人員未符合上述條件的假單，則跳過此關
    return False 

# 若上述條件皆不滿足，預設跳過此關卡
return False
