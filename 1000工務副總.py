if vaid==117 or vaid==118 or vaid==119 or vaid==120:
    return True
if plevel == 6 and (hours>8 or continueDays>1) : #業務企劃中心
    return True
if plevel == 3 and vaid ==5:
    return True
if vaid==7 or vaid==5 or vaid==6:
    return False
if vaid==67: 
   return False

#彬鴻修改
if secondDept==3 and nlevel<=750 and (hours>8 or continueDays>1 or vaid==13 or vaid==16 or vaid==18 or vaid==26 or vaid==27 or vaid==28 or vaid==31 or vaid==93):   
    return True
if secondDept==4 and (hours>8 and vaid==31):   #彬鴻修改
    return True
if secondDept==5 and (hours>8 and vaid==31):   #彬鴻修改
    return True
if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
    return False
if nlevel<=750 and plevel==3 and (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111):
    return False
if plevel==3 and vaid==6:
    return False
if nlevel<=750 and plevel==3 and (not (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111 or vaid==20 or vaid==21 or vaid==12 or vaid==14) or (hours>8 or continueDays>1) ):
    return True
 
 
return False