# 【審核主體：勞安室二廠 (職級 610) 的審核邏輯】

if (vaid==26 or vaid==27 or vaid==28 or vaid==103) and (secondDept==1 or plevel==2 ):
    # 進入審核：如果請假類別是「公傷病假(26)」、「生理假(27)」、「職災假(28)」、「疫苗接種假(103)」，
    # 且該假單來自「特定部門代碼 1 (secondDept=1)」或「第二工廠 (plevel=2)」，則進入審核。
    return True

# 排除條件：所有不符合上述特定條件的請假單，均排除/不審核。
return False