# 若簽核部門為 第一工廠(1) 或 第二工廠(2)，且職級為 副單位主管(750) 含以上，跳過此關卡
if plevel in (1, 2) and nlevel >= 750:
    return False

# 若為總經理室人員(4)，且為 13職等以上人員，跳過此關卡
if master == 4 and rankAbove13 == 1:
    return False

# 需簽核條件：
# 1. 職級在 副單位主管(750) 含以下
# 2. 且 非屬於「派駐二廠要給二廠人事名單」(secondDept != 1)
# 3. 且 簽核部門不是 第二工廠(2)
if nlevel <= 750 and secondDept != 1 and plevel != 2:
    return True

# 預設行為：其他情況跳過此關卡
return False
