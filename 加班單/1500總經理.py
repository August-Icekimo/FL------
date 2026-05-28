# 審核單位主管 OR 副總經理
if nlevel==800 or nlevel==900:
    return True
# 審核副單位主管 AND (第一工廠 OR 第二工廠)
if nlevel==750 and plevell in (1, 2):
    return True
# 特別取回總經理室13等以上人員
if master==4 and rankAbove13==1:
    return True
# 預設不主動審核
return False