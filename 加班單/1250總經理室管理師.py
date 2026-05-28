# 若申請人為 13職等以上人員(rankAbove13=1)，跳過此關卡
if rankAbove13 == 1:
    return False

# 預設行為：其他情況皆需經過總經理室管理師審核
return True
