# 總經理室人員<800職級的公假需經主管簽核
if master == 4 and nlevel < 800 and vaid == 7:
    return True

# 副主管、組長、副組長(onlySecond==1)、股長(非一二廠)的公假需經主管簽核
if (nlevel == 750 or nlevel == 700 or (nlevel == 650 and onlySecond == 1) or
    (nlevel == 500 and plevel != 1 and plevel != 2)) and vaid == 7:
    return True

# 秘書室副組長的公假需經主管簽核
if nlevel == 650 and master == 2 and vaid == 7:
    return True

return False