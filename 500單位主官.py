# 【單位主官 審核邏輯】

# --- 全局排除條件 ---
# 已簽准之公假(7)不需主官審核
if vaid==7:
    return False

# 單位主管(800)含以上者，不需單位主官審核 (僅審核副單位主管750以下)
if nlevel>=800: 
    return False

# --- 特定部門/流程強制審核條件 ---
# 製證中心組流程設定-資通機電 (secondDept=3) 且 職級為單位主管以下 (<800) 者，需審核
if secondDept==3 and nlevel<800:   #彬鴻修改
    return True

# 製證及品檢封裝股流程-空白 (secondDept=4) 且 符合特定假別或時數條件者，需審核
# 條件為：請假時數>8、連續天數>1、或 特定假別(婚假13,喪假16,家庭照顧18,流產26,娩假27,產檢28,非本廠公假31,生理假93)
if secondDept==4 and (hours>8 or continueDays>1 or vaid==13 or vaid==16 or vaid==18 or vaid==26 or vaid==27 or vaid==28 or vaid==31 or vaid==93):   #彬鴻修改
    return True

# 製證及品檢封裝股流程-品檢封裝製證 (secondDept=5) 且 符合特定假別或時數條件者，需審核
# 條件同上 (時數>8、連續天數>1、或 婚假/喪假/家庭照顧/流產/娩假/產檢/非本廠公假/生理假)
if secondDept==5  and (hours>8 or continueDays>1 or vaid==13 or vaid==16 or vaid==18 or vaid==26 or vaid==27 or vaid==28 or vaid==31 or vaid==93) :   #彬鴻修改
    return True

# (已註解掉的邏輯) 一般人員(100)申請遞延休假(21)小於8HR不進入
#if nlevel==100 and vaid==21 and hours<8:
#    return False

# 秘書室人員(master=2) 且 非一/二廠 (plevel!=1,2) 且 職級為單位主管以下 (<800) 者，需審核
if master==2 and plevel!=1 and plevel!=2 and nlevel<800:
    return True

# 特殊政風流程 (linkuncheng=1) 者，需審核
if linkuncheng ==1:
    return True

# --- 一廠與二廠廠長室人員 (master=1) 審核條件 ---
# 針對一廠或二廠(plevel=1,2)，廠長室人員(master=1)，副組長/副課長以下(nlevel<=650)
# 若請假超過一天 (hours>8 或 continueDays>1 的事假12/休假20/病假14)，或屬於特定假別(公出4/公假7/各種補休35-38/109-111)，需審核
if (plevel==1 or plevel==2) and master==1 and nlevel<=650 and (((vaid==12 or vaid==20 or vaid==14) and hours>8)  or  (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111) or continueDays>1) :
    return True

# --- 特殊排除條件 (單日或短時數特定假別) ---
# 針對一廠或二廠(plevel=1,2)，副組長/副課長以下(nlevel<=650)
# 若是請「單日以內」的事假12/休假20/病假14，或公出4/公假7/各種補休，則跳過主官審核
if (plevel==1 or plevel==2 ) and nlevel<=650 and (((vaid==12 or vaid==20 or vaid==14) and hours<=8)  or  (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111)) and continueDays<=1:
    return False

# 針對秘書室(master=2)或人事組長群組(master=4)，組長/課長以下(nlevel<=700)
# 若是請「單日以內」的事假12/休假20/病假14，或公出4/公假7/各種補休，則跳過主官審核
if  (master==2 or master==4)and nlevel<=700 and (((vaid==12 or vaid==20 or vaid==14) and hours<=8)  or  (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111)) and continueDays<=1:
    return False

# 通過所有排除與特定審核條件後，預設進入單位主官審核
return True