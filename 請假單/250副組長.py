if vaid==7:
    return False
if nlevel >= 650  : #副組長以上不進入
    return False
if plevel==1 or plevel==2:
   return False
#if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
#    return False
return True