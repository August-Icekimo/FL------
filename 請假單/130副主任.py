# 股長、組長、副組長申請本廠公務公假，且簽核部門非第一、二工廠時，需經副主任簽核
if (nlevel==500 or nlevel==700 or (nlevel==650 and onlySecond==1) ) and vaid==7 and plevel!=1 and plevel!=2:
    return True
if master==4 and nlevel==100 and vaid==7:#總經理室一般人員要給其他單位的副主任簽核
    return True
#if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
#    return False
if master==2 and vaid==7 and plevel!=1 and plevel!=2 and nlevel<=700:
    return True
return False