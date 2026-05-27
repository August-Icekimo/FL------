# --- 預設不予審核 ---

# --- 進入審核條件 (Quick Pass) ---

# 若職級在副單位主管(750)以下(即<750)，需進入審核
if nlevel < 750:
    return True

# --- 不予審核條件 (Quick Fall / 排除條件) ---

# 若人員群組-副為副主任2督導(2) (註：原系統標註為跳過二廠人員)，跳過此關卡不予審核
if second == 2:
    return False

# 若上述條件皆不滿足，預設跳過此關卡
return False
