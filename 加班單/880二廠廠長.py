# 若申請人職級為單位主管(800)含以上，跳過此關卡
if nlevel >= 800:
    return False

# 若申請人所屬群組為總經理室人員(4)，跳過此關卡
if master == 4:
    return False

# 若申請人為13職等以上人員(rankAbove13=1)，跳過此關卡
if rankAbove13 == 1:
    return False

# 若簽核部門為數位身分識別證製作中心(7) 且 申請人職級為單位主管(800)之下，需經二廠廠長審核
if plevel == 7 and nlevel < 800:
    return True

# 預設行為：其他情況跳過此關卡
return False
