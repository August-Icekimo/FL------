# 跳過單位主管
if nlevel >= 800:
    return False
if master==4:
    return False
if rankAbove13==1:
    return False
# 簽核層級 單位主管 AND 數位身分識別證製作中心
if plevel == 7 and nlevel < 800:
    return True
return False