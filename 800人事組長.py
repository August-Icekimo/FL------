if vaid==117 or vaid==118 or vaid==119 or vaid==120 or vaid==67:
    return True
if vaid==7 or vaid==67 or vaid==5 or vaid==21:
    return False
if (plevel==1 or plevel==2) and nlevel<=700 and vaid==6:
  return True

if plevel==1 or plevel==2:
    return False
if nlevel>=800: #單位主管以上
   return False

if nlevel==750 and (((vaid==12 or vaid==20 or vaid==21 or vaid==15) and hours<=8)  or  (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111)):
   return False
if nlevel<=750 and plevel!=1 and plevel!=2 and (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111):
    return False 
if nlevel<=750 and plevel!=1 and plevel!=2 and (not (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111 or vaid==20 or vaid==21 or vaid==12 or vaid==14) or (hours>8 or continueDays>1) ):
    return True
return False