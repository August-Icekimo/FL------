# --- 進入審核條件 (Quick Pass) ---

# 若職級為副單位主管(750)或以下，且簽核部門為工務副總督導(3)，需進入審核
if nlevel <= 750 and plevel == 3:
    return True

# 若職級為組長/課長(700)或以下(即<750)，且簽核部門為第一工廠(1)或第二工廠(2)，需進入審核
if nlevel < 750 and plevel in (1, 2):
    return True

# 若簽核部門為業務企劃中心(6)，需進入審核
if plevel == 6:
   return True

# --- 預設不予審核 ---

# 若上述條件皆不滿足，預設跳過此關卡
return False
