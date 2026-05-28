# 檢查是否為「人事室」專屬流程 (旗標 onlyHRDept == 1)
if onlyHRDept == 1:
    # 檢查職級是否低於「單位主管」(nlevel < 800，例如副單位主管750以下)
    if nlevel < 800:
        # 人事室且為副單位主管以下者，需經過此關卡審核
        return True
    
    # 職級為單位主管(800)含以上者 (如人事主任)，不需經過此關卡
    return False

# 非人事室的其他單位人員，皆跳過此關卡
return False
