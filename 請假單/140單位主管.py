if master==4 and nlevel<800 and vaid==7:
    return True

if (nlevel==750 or nlevel==700  or (nlevel==650 and onlySecond==1) or (nlevel==500 and plevel!=1 and plevel!=2)) and vaid==7:
    return True
if nlevel==650 and master==2 and vaid==7:
    return True
#if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
#    return False
return False