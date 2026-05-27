if (plevel==1 or plevel==2 )and nlevel >=750:
    return False
# 跳過總經理室13等以上人員
if master==4 and rankAbove13==1:
    return False
if nlevel<=750  :
    return True
return False