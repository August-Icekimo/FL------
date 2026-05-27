# --- 不予審核條件 (Quick Fall / 排除條件) ---

# 若簽核部門為第一工廠(1)或第二工廠(2)，且職級為副單位主管(750)或以上，跳過不予審核
if plevel in (1, 2) and nlevel >= 750:
    return False

# 若為總經理室人員(master=4)且為13職等以上人員(rankAbove13=1)，跳過不予審核
if master == 4 and rankAbove13 == 1:
    return False

# --- 進入審核條件 (Quick Pass) ---

# 若職級為副單位主管(750)或以下，需進入審核
if nlevel <= 750:
    return True

# --- 預設不予審核 ---

# 若上述條件皆不滿足，預設跳過此關卡
return False
