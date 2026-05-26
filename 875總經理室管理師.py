# 判斷是否需要經過「總經理室管理師」簽核關卡

# 若假別為理監事會務假(67)，必須經過總經理室管理師簽核
if vaid==67:
    return True

# 若申請人屬於人事室人員 (onlyHRDept == 1)
if onlyHRDept==1: 
    # 針對人事室人員中，職級在「副單位主管」(750)(含)以下，且非一廠(1)、二廠(2)之人員：
    # 若假別「非」常見免簽假別（公出4 / 公假(本廠公務)7 / 補休35-38,109-111 / 休假20 / 遞延休假21 / 事假12 / 病假14），
    # 「或者」請假時數 > 8 小時，
    # 「或者」連續請假天數 > 1 天，則須經過總經理室管理師簽核
    if nlevel<=750 and plevel!=1 and plevel!=2 and (not (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111 or vaid==20 or vaid==21 or vaid==12 or vaid==14) or (hours>8 or continueDays>1) ): 
        return True
        
    # 人事室人員未符合上述條件的假單，則跳過此關
    return False 

# 預設跳過此關卡
return False
