if vaid==7 or vaid==5 or vaid==21:
    return False
if nlevel>=800: #單位主管以上
   return False

if vaid==67 and (second==3 or onlySecond==2 or secondDept==1):#工會假單->二廠人事
    return True

if plevel == 6 and (not (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111 or vaid==20 or vaid==12 or vaid==14) or (hours>8 or continueDays>1) ):#業務企劃中心
    return True

if (plevel==2 or second==3) and nlevel<=700 and vaid==6:
  return True
if nlevel<=750 and plevel!=1 and plevel!=2 and (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111):
    return False
if second==3 and nlevel<=750 and plevel!=1 and plevel!=2 and (not (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111 or vaid==20 or vaid==12 or vaid==14) or (hours>8 or continueDays>1) ):
    return True

if nlevel==750 and (((vaid==12 or vaid==20 or vaid==21 or vaid==15) and hours<=8)  or  (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111)):
   return False

return False