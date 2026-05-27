# --- 預設不予審核 ---
# --- 進入審核條件 (Quick Pass) ---

# 若簽核部門為數位身分識別證製作中心(7)，且職級在單位主管(800)以下，需進入審核
if plevel == 7 and nlevel < 800:
    return True

# --- 不予審核條件 (Quick Fall / 排除條件) ---

# 若職級為單位主管(800)或以上，跳過此關卡不予審核
if nlevel >= 800:
    return False

# 若為總經理室人員(master=4)，跳過此關卡不予審核
if master == 4:
    return False

# 若為13職等以上人員(rankAbove13=1)，跳過此關卡不予審核
if rankAbove13 == 1:
    return False

# 若上述條件皆不滿足，預設跳過此關卡
return False
