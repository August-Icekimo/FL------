# --- 進入審核條件 (Quick Pass) ---
# --- 不予審核條件 (Quick Fall / 排除條件) ---

# 若為13職等以上人員(rankAbove13=1)，跳過此關卡不予審核
# (註：此類別的加班單簽核流程特殊，不經過此審核節點)
if rankAbove13 == 1:
    return False

# 若上述排除條件皆不滿足，預設均進入審核
return True
