# 需簽核條件1：
# 職級為 副單位主管(750) 含以下，且符合下列任一二廠人事相關屬性：
# - second == 3: 二廠人事業務範圍
# - onlySecond == 2: 派駐二廠(與second有重疊)
# - secondDept == 1: 派駐二廠要給二廠人事名單
if nlevel <= 750 and (second == 3 or onlySecond == 2 or secondDept == 1):
    return True

# 若為總經理室人員(4)，且為 13職等以上人員(rankAbove13=1)，跳過此關卡
if master == 4 and rankAbove13 == 1:
    return False

# 需簽核條件2：
# 職級為 組長/課長(700) 含以下 (即小於 750)，且 簽核部門為 第二工廠(2)
if nlevel < 750 and plevel == 2:
    return True

# 預設行為：其他情況跳過此關卡
return False
