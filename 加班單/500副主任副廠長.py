# 跳過二廠人員
if second==2:
    return False
# 審核 副單位主管以下人員
if nlevel<750:
    return True
return False