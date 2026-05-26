# 【人事室主任 (職級 900) 的審核邏輯】
# 進入審核條件一：假別為「防疫相關假別」或「工會公出假」。
# vaid=117-120 (防疫相關假別), vaid=67 (工會公出假)
if vaid==117 or vaid==118 or vaid==119 or vaid==120 or vaid==67: 
    return True

# 排除條件一：排除「已簽准公假」、「工會公出假」、「公務」、「公差」、「遞延休假」。
# 這些假別通常已有簽核流程或性質特殊，主任在此階段直接排除。
# vaid=7(公假), vaid=67(工會公出假), vaid=6(公務), vaid=5(公差), vaid=21(遞延休假)
if vaid==7 or vaid==67 or vaid==6 or vaid==5 or vaid==21: 
    return False

# 排除條件二：排除來自「一廠」或「二廠」的所有請假單。
# plevel=1 (一廠), plevel=2 (二廠)
if plevel==1 or plevel==2: 
    return False

# 排除條件三：排除「單位主管以上」職級 (nlevel >= 800) 的請假單。
# 審核目標僅鎖定在副單位主管或以下。
if nlevel>=800: 
   return False

# 排除條件四：【針對副單位主管 (750) 的特定排除】
# 排除以下兩種情況的「副單位主管」請假單：
# 1. 僅請「一天」的事假(12)、休假(20)、遞延休假(21)、特准病假(15)。
# 2. 或 請「公出(4)」、「已簽准公假(7)」、「各種補休(35-38, 109-111)」。
if nlevel==750 and (((vaid==12 or vaid==20 or vaid==21 or vaid==15) and hours<=8) or (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111)):
   return False

# 排除條件五：【針對非一廠/二廠的一般人員的特定排除】
# 排除 職級為副單位主管以下 (nlevel <= 750) 且 非一廠/二廠 (plevel != 1, 2) 的以下假別：
# 「公出(4)」、「已簽准公假(7)」、「各種補休(35-38, 109-111)」。
if nlevel<=750 and plevel!=1 and plevel!=2 and (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111):
    return False

# 最終進入審核條件 (Return True)：
# 針對 非一廠/二廠 (plevel != 1, 2) 的副單位主管以下 (< 750) 人員，若符合以下**任一**條件則需審核：
# 1. 該假別不在「公出、公假、補休、休假、遞延休假、事假、病假」的排除清單內。
# 2. 或 該請假單屬於「所有超過一天的假別」 (hours > 8 或 continueDays > 1)。
if nlevel<=750 and plevel!=1 and plevel!=2 and (not (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111 or vaid==20 or vaid==21 or vaid==12 or vaid==14) or (hours>8 or continueDays>1) ): 
    return True

# 預設：如果所有條件都不符合，則最終不審核 (Return False)。
return False