# 公假直接跳過本關卡
if vaid == 7:
    return False

# 副組長以上職級直接跳過本關卡
if nlevel >= 650:
    return False

# 第一、二工廠人員直接跳過本關卡
if plevel == 1 or plevel == 2:
    return False

# 其他情況進入簽核
return True