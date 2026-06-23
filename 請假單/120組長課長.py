# 組長以下職級申請本廠公務公假，非政風流程，非駐衛警部門時進入簽核
if nlevel < 700 and vaid == 7 and linkuncheng != 1 and plevel != 5:
    return True
return False