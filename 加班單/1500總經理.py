# --- 進入審核條件 (Quick Pass) ---

# 若職級為單位主管(800)或業務副總/工務副總(900)，需進入總經理關卡審核
if nlevel in (800, 900):
    return True

# 若職級為副單位主管(750) 且 簽核部門屬於第一工廠(1)或第二工廠(2)，需進入總經理關卡審核
if nlevel == 750 and plevel in (1, 2):
    return True

# 若為總經理室人員(master=4) 且 為13職等以上人員(rankAbove13=1)，需進入總經理關卡審核
if master == 4 and rankAbove13 == 1:
    return True

# --- 不予審核條件 ---

# 若上述特殊審核條件皆不滿足，預設不予審核，跳過此關卡
return False
