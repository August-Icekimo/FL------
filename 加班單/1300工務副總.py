if nlevel<=750 and (plevel==3):#plevel非工廠的督導單位  750為課長級
    return True
if nlevel<750 and (plevel==1 or plevel==2):#plevel 1第一工廠 2第二工廠
    return True
if plevel==6:#業務企劃中心
   return True
return False