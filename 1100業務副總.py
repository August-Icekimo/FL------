# 業務企劃中心不經過此關卡
if plevel == 6: #業務企劃中心
    return False

# 假別為公假(本廠公務) (7) 或 公務 (6) 不經過此關卡
if vaid==7 or vaid==6:
    return False

# 若為公差 (5) 或 理監事會務假 (67)，且非屬工務副總督導 (plevel!=3)，且職級低於副總 (nlevel<900)，需由業務副總審核
if (vaid==5 or vaid==67) and plevel!=3  and nlevel<900:
    return True

# 彬鴻修改: 製證中心組流程設定-資通機電 (secondDept==3) 且職級為副單位主管(含)以下 (nlevel<=750)，申請公差 (5) 需審核
if secondDept==3 and nlevel<=750 and vaid==5:   
    return True

# 第一工廠 (1)、第二工廠 (2)、工務副總督導 (3) 的單，不經過業務副總
if plevel==1 or plevel==2 or plevel==3:
    return False

# 一般人員 (100) 申請遞延休假 (21) 且請假時數小於8小時不進入此關卡
if nlevel==100 and vaid==21 and hours<8:#一般人員申請遞延休假小於8HR不進入
    return False

# 職級在副單位主管(含)以下 (nlevel<=750)，且非屬一廠、二廠、工務副總督導，
# 申請公出 (4)、公假(本廠公務) (7)、或各類補休 (35, 36, 37, 38, 109, 110, 111) 不進入此關卡
if nlevel<=750 and plevel!=1 and plevel!=2 and plevel!=3 and (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111):
    return False

# 簽核部門為工務副總督導 (3) 且為公務 (6) 不經過此關卡 (前面已排除 plevel==3，此段可能為保險機制)
if plevel==3 and vaid==6:
    return False

# 職級在副單位主管(含)以下 (nlevel<=750)，且非屬一廠、二廠、工務副總督導，
# 只要「不屬於」一般較短天數之假別 (公出、公假(本廠公務)、各類補休、休假、遞延休假、事假、病假)，
# 或者 (請假時數大於8小時 或 連續天數大於1天)，就需要業務副總審核
if nlevel<=750 and plevel!=1 and plevel!=2 and plevel!=3 and (not (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111 or vaid==20 or vaid==21 or vaid==12 or vaid==14) or (hours>8 or continueDays>1) ):
    return True

# 預設不經過此關卡
return False
