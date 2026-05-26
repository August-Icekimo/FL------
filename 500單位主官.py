if vaid==7:
    return False
if nlevel>=800: 
    return False

if secondDept==3 and nlevel<800:   #彬鴻修改
    return True
if secondDept==4 and (hours>8 or continueDays>1 or vaid==13 or vaid==16 or vaid==18 or vaid==26 or vaid==27 or vaid==28 or vaid==31 or vaid==93):   #彬鴻修改
    return True
if secondDept==5  and (hours>8 or continueDays>1 or vaid==13 or vaid==16 or vaid==18 or vaid==26 or vaid==27 or vaid==28 or vaid==31 or vaid==93) :   #彬鴻修改
    return True
#if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
#    return False
if master==2 and plevel!=1 and plevel!=2 and nlevel<800:
    return True
if linkuncheng ==1:
    return True
if (plevel==1 or plevel==2) and master==1 and nlevel<=650 and (((vaid==12 or vaid==20 or vaid==14) and hours>8)  or  (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111) or continueDays>1) :
    return True
if (plevel==1 or plevel==2 ) and nlevel<=650 and (((vaid==12 or vaid==20 or vaid==14) and hours<=8)  or  (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111)) and continueDays<=1:
    return False
if  (master==2 or master==4)and nlevel<=700 and (((vaid==12 or vaid==20 or vaid==14) and hours<=8)  or  (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111)) and continueDays<=1:
    return False

return True