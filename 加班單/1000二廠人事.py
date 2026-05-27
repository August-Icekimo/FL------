# 【二廠人事 (1000) 的審核邏輯】
# --- 預設不予審核 ---
# --- 進入審核條件 (Quick Pass) ---

# 如果職級為「副單位主管及以下 (nlevel <= 750)」的人員，則進入審核。
# *注意：此條件會捕捉所有職級 <= 750 的人員，除了已被上一個條件排除的一廠/二廠高階人員。
if nlevel <= 750:
    return True

# --- 不予審核條件 (Quick Fall / 排除條件) ---
# 排除來自「第一工廠 (1)」或「第二工廠 (2)」且職級在「副單位主管及以上 (nlevel >= 750)」的人員。
if plevel in (1, 2) and nlevel >= 750:
    return False

# 跳過總經理室(master=4) 13職等以上人員(rankAbove13=1)
if master == 4 and rankAbove13 == 1:
    return False

# 其餘不符合進入審核條件的請假單，則排除/不審核。
return False
