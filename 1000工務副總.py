# 判斷是否需要經過「工務副總」簽核關卡

# 若假別為防疫相關假別，必須經過工務副總簽核
# 117: (不支薪)防疫照顧假, 118: 防疫病假, 119: 防疫隔離假, 120: (不支薪)疫苗接種假
if vaid in (117, 118, 119, 120):
    return True

# 業務企劃中心 (6)，若請假時數大於8小時或連續天數大於1天，需經過工務副總
if plevel == 6 and (hours>8 or continueDays>1) : #業務企劃中心
    return True

# 簽核部門為工務副總督導 (3)，且申請公差 (5)，需經過工務副總
if plevel == 3 and vaid == 5:
    return True

# 若假別為公假(本廠公務) (7) 或 公差 (5) 或 公務 (6)，跳過此關卡
# (註：上方已判斷 plevel==3 且 vaid==5 回傳 True，此處是針對非工務副總督導單位的公差)
if vaid in (5, 6, 7):
    return False

# 若假別為工會會務假 (67, 165, 166)，跳過此關卡
if vaid in (67, 165, 166): 
   return False

# 彬鴻修改: 製證中心組流程設定-資通機電 (secondDept==3) 且職級為副單位主管(含)以下 (nlevel<=750)，
# 且 (請假時數>8小時 或 連續天數>1天 或 為特定假別: 13婚假, 16喪假, 18家庭照顧假, 26流產假, 27娩(產)假, 28產檢假, 31公假(非本廠公務), 93生理假)，需經過工務副總
if secondDept==3 and nlevel<=750 and (hours>8 or continueDays>1 or vaid in (13, 16, 18, 26, 27, 28, 31, 93)):   
    return True

# 彬鴻修改: 製證及品檢封裝股流程-空白 (secondDept==4) 或 品檢封裝製證 (secondDept==5)，
# 請假時數大於8小時且為公假(非本廠公務) (31)，需經過工務副總
if secondDept in (4, 5) and hours>8 and vaid==31:   #彬鴻修改
    return True

# 一般人員 (100) 申請遞延休假 (21) 且請假時數小於8小時不進入此關卡
if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
    return False

# 職級在副單位主管(含)以下 (nlevel<=750)，且簽核部門為工務副總督導 (3)，
# 申請公出 (4)、公假(本廠公務) (7)、或各類補休 (35, 36, 37, 38, 109, 110, 111) 不進入此關卡
if nlevel<=750 and plevel==3 and vaid in (4, 7, 35, 36, 37, 38, 109, 110, 111):
    return False

# 職級在副單位主管(含)以下 (nlevel<=750)，且簽核部門為工務副總督導 (3)，
# 只要「不屬於」一般較短天數之假別 (公出、公假(本廠公務)、各類補休、休假、遞延休假、事假、病假)，
# 或者 (請假時數大於8小時 或 連續天數大於1天)，就需要工務副總審核
if nlevel<=750 and plevel==3 and (vaid not in (4, 7, 12, 14, 20, 21, 35, 36, 37, 38, 109, 110, 111) or hours>8 or continueDays>1):
    return True
 
# 預設不經過此關卡
return False
