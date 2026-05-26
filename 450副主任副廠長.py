if (plevel==1 or plevel==2) and master==1 and nlevel<=650 and second==2 and vaid!=67:
    return True
if vaid==7:
    return False
if (plevel==1 or plevel==2) and vaid==67:
    return False

if second!=2: #非指定督導
   return False
if nlevel>=750:
    return False
if vaid==67 and (nlevel==700 or (nlevel==650 and onlySecond==1)):
    return True
if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
    return False
if (plevel==1 or plevel==2) and nlevel<=650 and (((vaid==12 or vaid==20 or vaid==14) and hours<=8)  or  (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111)) and continueDays<=1:
    return False

return True