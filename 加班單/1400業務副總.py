# --- 預設不予審核 ---
# # --- 進入審核條件 (Quick Pass) ---

# 若職級為副單位主管(750)或以下，且簽核部門「非」第一工廠(1)、「非」第二工廠(2)、「非」工務副總督導(3)，需進入業務副總關卡審核
if nlevel <= 750 and plevel not in (1, 2, 3):
    return True


# --- 不予審核條件 (Quick Fall / 排除條件) ---

# 若簽核部門為業務企劃中心(6)，跳過此關卡不予審核
if plevel == 6:
    return False


# 若上述條件皆不滿足，預設跳過此關卡
return False
