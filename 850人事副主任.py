# 審核 防疫相關假別 (117-120) 或 工會公出假 (67)
if vaid==117 or vaid==118 or vaid==119 or vaid==120 or vaid==67: 
    return True

# 排除 已簽准公假 (7), 工會公出假 (67), 公務 (6), 公差 (5), 遞延休假 (21)
if vaid==7 or vaid==67 or vaid==6 or vaid==5 or vaid==21: 
    return False

# 排除 一廠 (1), 二廠 (2)
if plevel==1 or plevel==2: 
    return False

# 排除 單位主管以上 (nlevel >= 800)
if nlevel>=800: 
   return False

# 排除 副單位主管 (750) 的以下假別：
# 1. 一天的事假 (12)、休假 (20)、遞延休假 (21)、特准病假 (15)
# 2. 或 公出 (4)、已簽准公假 (7)、各種補休 (35-38, 109-111)
if nlevel==750 and (((vaid==12 or vaid==20 or vaid==21 or vaid==15) and hours<=8) or (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111)):
   return False

# 排除 副單位主管以下 (< 750) 且 非一廠/二廠 的以下假別：
# 公出 (4)、已簽准公假 (7)、各種補休 (35-38, 109-111)
if nlevel<=750 and plevel!=1 and plevel!=2 and (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111):
    return False

# 審核 非一廠/二廠 (plevel != 1, 2) 的副單位主管以下 (< 750) 的以下狀況：
# 1. 該假別不在排除清單內 (排除清單: 公出(4), 公假(7), 補休(35-38/109-111), 休假(20), 遞延休假(21), 事假(12), 病假(14))
# 2. 或 該假別超過一天 (hours > 8 或 continueDays > 1)
if nlevel<=750 and plevel!=1 and plevel!=2 and (not (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111 or vaid==20 or vaid==21 or vaid==12 or vaid==14) or (hours>8 or continueDays>1) ): 
    return True

return False