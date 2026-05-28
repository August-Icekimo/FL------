# (已註解掉的歷史邏輯) 若為總經理室人員(master==4)且職級小於單位主管(800)，不須審核
# if master == 4 and nlevel < 800:
#    return False

# 必須同時符合以下條件，才需進入「單位主管」關卡審核：
# 1. 申請人職級為「副單位主管」含以下 (nlevel <= 750)
# 2. 排除特殊高階人員：不能同時是「總經理室人員」(master == 4) 或「13職等以上」(rankAbove13 == 1)
return nlevel <= 750 and not (master == 4 or rankAbove13 == 1)
