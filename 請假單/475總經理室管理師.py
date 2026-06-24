if onlyHRDept==1 and nlevel<=750: #屬於人事室人員
    return True

# 若申請人屬於人事室人員 (onlyHRDept == 1)
if onlyHRDept==1: 
    # 針對人事室人員中，職級在「副單位主管」(750)(含)以下：
    # 若假別「非」常見免簽假別（公出4 / 補休35-38,109-111 / 休假20 / 遞延休假21 / 事假12 / 病假14），
    # 「或者」請假時數 > 8 小時，
    # 「或者」連續請假天數 > 1 天，則須經過總經理室管理師簽核
    #   未列出的公假(本廠公務)7 (非本廠公務)31 會經過總經理室管理師簽核
    if nlevel<=750 and (vaid not in (4, 12, 14, 20, 21, 35, 36, 37, 38, 109, 110, 111) or hours>8 or continueDays>1): 
        return True
        
    # 人事室人員未符合上述條件的假單，則跳過此關
    return False 

return False # 其餘不審核