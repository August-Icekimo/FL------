# 條件一：如果請假類別為「工會公出假 (67)」，則進入審核。
if vaid==67:
    return True

# 條件二：判斷是否屬於人事室人員 (onlyHRDept = 1)
if onlyHRDept==1: 
    # 屬於人事室人員，進一步判斷是否需要審核。
    
    # 審核邏輯 (與人事室副主任的複雜條件相同)：
    # 僅審核以下兩類人員的請假單：
    # 1. 職級為副單位主管以下 (nlevel <= 750) 且 非一廠/二廠 (plevel != 1, 2) 的人員。
    # 2. 且 該假別不在「公出、公假、補休、休假、遞延休假、事假、病假」的排除清單內
    #    或 請假時數超過一天 (hours > 8 或 continueDays > 1)。
    # 排除清單：vaid=4(公出), 7(公假), 35-38/109-111(補休), 20(休假), 21(遞延休假), 12(事假), 14(病假)
    if nlevel<=750 and plevel!=1 and plevel!=2 and (not (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111 or vaid==20 or vaid==21 or vaid==12 or vaid==14) or (hours>8 or continueDays>1) ): 
        return True
        
    # 如果是人事室人員，但其請假單不符合上述複雜審核條件 (即被人事副主任排除/不需審核)，則返回 False。
    return False 

# 如果不符合條件一 (非工會公出假) 且 不符合條件二 (非人事室人員)，則最終不審核 (Return False)。
return False