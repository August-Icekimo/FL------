if vaid==7:
    return False
if nlevel>=700:
    return False
if secondDept==3 and nlevel<500:   #彬鴻修改
    return True
if secondDept==2 and plevel==2 and nlevel<500:
    return True
if (plevel==1 or plevel==2) and nlevel<500 and (((vaid==12 or vaid==20 or vaid==15) and hours<=8)  or  ( vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111)) and continueDays<=1:
    return False
if linkuncheng ==1:
    return False
#if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
#    return False
return True