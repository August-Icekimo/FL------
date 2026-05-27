# --- 預設不予審核 ---
# --- 進入審核條件 (Quick Pass) ---

# 若職級為副單位主管(750)或以下，且符合二廠人事相關業務(second=3 或 onlySecond=2 或 secondDept=1)，需進入審核
if nlevel <= 750 and (second == 3 or onlySecond == 2 or secondDept == 1):
    return True

# 若職級為組長/課長(700)或以下(即<750)，且簽核部門為第二工廠(2)，需進入審核
if nlevel < 750 and plevel == 2:
    return True

# --- 不予審核條件 (Quick Fall / 排除條件) ---

# 跳過總經理室(master=4) 13等以上人員(rankAbove13=1)
if master == 4 and rankAbove13 == 1:
    return False

# 若上述條件皆不滿足，預設跳過此關卡
return False
