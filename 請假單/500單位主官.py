# 【500 單位主官 審核邏輯】
# 預設進入審核，除非符合排除條件

# === 假別常數定義 ===
# 短期假別（8小時以內）
vaid_short_term = (12, 14, 20)
# 公出、公假、補休（短假排除用）
vaid_short_exclude = (4, 7, 35, 36, 37, 38, 109, 110, 111)

# === 排除條件判斷 ===
# 公假直接排除
if vaid == 7:
    return False

# 職級過高排除
if nlevel >= 800:
    return False

# 單日內的短假判斷
is_short_leave = continueDays <= 1 and (
    (vaid in vaid_short_term and hours <= 8) or
    vaid in vaid_short_exclude
)

# 一二廠副組長以下的單日短假排除
if plevel in (1, 2) and nlevel <= 650 and is_short_leave:
    return False

# 秘書室/總經理室組長以下的單日短假排除
if master in (2, 4) and nlevel <= 700 and is_short_leave:
    return False

# 預設進入審核 (包含製證中心、政風流程等特定人員)
return True
