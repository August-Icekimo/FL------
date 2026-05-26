if vaid==67:
    return False
if nlevel==800 or nlevel==900:
    return True
if nlevel==750 and (plevel==1 or plevel==2) and vaid!=7:
    return True
if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
    return False
return False