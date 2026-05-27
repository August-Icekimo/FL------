# --- 預設不予審核 ---
# --- 進入審核條件 (Quick Pass) ---

# 若職級在組長/課長(700)以下(即<700)，且人員群組-主「非」總經理室人員(4)，需進入審核
if nlevel < 700 and master != 4:
    return True

# 若上述條件皆不滿足，預設跳過此關卡
return False
