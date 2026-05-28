# 需簽核條件1：
# 職級為 副單位主管(750) 含以下，且 簽核部門為 工務副總督導(3)
if nlevel <= 750 and plevel == 3:
    return True

# 需簽核條件2：
# 職級為 組長/課長(700) 含以下 (即小於 750)，且 簽核部門為 第一工廠(1) 或 第二工廠(2)
if nlevel < 750 and plevel in (1, 2):
    return True

# 需簽核條件3：
# 簽核部門為 業務企劃中心(6) (不分職級)
if plevel == 6:
    return True

# 預設行為：其他情況跳過此關卡
return False
