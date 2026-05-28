if nlevel<=750 and (second==3 or onlySecond==2 or secondDept==1):
    return True
# 跳過總經理室13等以上人員
if master==4 and rankAbove13==1:
    return False
if nlevel<750 and ( plevel==2):
    return True

return False