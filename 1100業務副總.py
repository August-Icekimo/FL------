if plevel == 6: #業務企劃中心
    return False

if vaid==7 or vaid==6:
    return False
if (vaid==5 or vaid==67) and plevel!=3  and nlevel<900:
    return True

#彬鴻修改
if secondDept==3 and nlevel<=750 and vaid==5:   
    return True

if plevel==1 or plevel==2 or plevel==3:
    return False
if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
    return False
if nlevel<=750 and plevel!=1 and plevel!=2 and plevel!=3 and (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111):
    return False
if plevel==3 and vaid==6:
    return False
if nlevel<=750 and plevel!=1 and plevel!=2 and plevel!=3 and (not (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111 or vaid==20 or vaid==21 or vaid==12 or vaid==14) or (hours>8 or continueDays>1) ):
    return True
return False