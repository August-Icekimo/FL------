# 排除條件一：排除來自「一廠 (1)」或「二廠 (2)」且職級在「副單位主管及以上 (nlevel >= 750)」的人員。
if (plevel==1 or plevel==2 )and nlevel >=750:
    return False
# 排除條件二：跳過總經理室13等以上人員
if master==4 and rankAbove13==1:
    return False

# 進入審核條件一：如果職級為「副單位主管及以下 (nlevel <= 750)」的人員，則進入審核。
# *注意：此條件會捕捉所有職級 <= 750 的人員，除了已被上一個條件排除的一廠/二廠高階人員。
if nlevel<=750:
    return True

# 排除條件二：其餘不符合進入審核條件的請假單（即非一廠/二廠，且職級 > 750 的單位主管以上人員），則排除/不審核。
return False