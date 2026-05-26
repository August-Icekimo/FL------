# 【人事承辦 審核邏輯】

# --- 特定防疫假強制審核 ---
# 117: (不支薪)防疫照顧假, 118: 防疫病假, 119: 防疫隔離假, 120: (不支薪)疫苗接種假
if vaid==117 or vaid==118 or vaid==119 or vaid==120:
    return True

# --- 全局部門排除 ---
# 業務企劃中心(plevel=6) 的請假單不進人事承辦
if plevel == 6: #業務企劃中心
    return False

# --- 工會會務假特殊邏輯 ---
# 理監事會務假(67)：若「非」二廠相關人員 (不屬於二廠人事業務範圍 second=3，且不屬於派駐二廠 onlySecond=2 或 secondDept=1)，則進入本關審核 (二廠工會假單會交由二廠人事審核)
if vaid==67 and not (second==3 or onlySecond==2 or secondDept==1):#非二廠工會假單
    return True

# --- 特定假別排除 ---
# 公假(7)、公差(5)、遞延休假(21) 不需人事承辦審核
if vaid==7 or vaid==5 or vaid==21:
    return False

# --- 二廠人員排除 ---
# 屬於二廠人事業務範圍(second=3) 或 簽核部門為第二工廠(plevel=2) 的請假單，交由二廠處理，本關不審
if second==3 or plevel==2: #非二廠 (註: 判斷式意義為屬於二廠者直接return False跳過)
    return False

# --- 職級排除 ---
# 單位主管(800)含以上者，本關不審 (人事承辦僅處理副單位主管以下)
if nlevel>=800: #單位主管以上
   return False

# (重複的安全防護邏輯，維持原樣)
if second==3:
  return False

# --- 針對特定職級與假別的審核條件 ---
# 非第二工廠(plevel!=2) 的組長/課長以下(nlevel<=700)，若申請公務(6)，則進入審核
if plevel!=2 and nlevel<=700 and vaid==6:
  return True

# --- 副單位主管(750) 特定短天數/假別排除 ---
# 職級為副單位主管(750) 申請以下情況不審：
# 1. 單日以內(<=8HR) 的事假(12)/休假(20)/遞延休假(21)/特准病假(15)
# 2. 或 公出(4)、公假(7)、各種補休(35-38, 109-111)
if nlevel==750 and (((vaid==12 or vaid==20 or vaid==21 or vaid==15) and hours<=8)  or  (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111)):
   return False

# --- 非一/二廠 (總公司等) 副主管以下特定假別排除 ---
# 副主管以下(nlevel<=750) 且 非第一/第二工廠 (plevel!=1,2)，申請 公出(4)/公假(7)/各種補休(35-38, 109-111) 者不審
if nlevel<=750 and plevel!=1 and plevel!=2 and (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111):
    return False

# --- 非一/二廠 副主管以下 長天數或特殊假別審核 ---
# 副主管以下(nlevel<=750) 且 非第一/第二工廠 (plevel!=1,2)：
# 若申請「非」排除清單(公出/公假/補休/休假/遞休/事假/病假) 的 特殊假別
# 或 請假超過一天 (hours>8 或 continueDays>1)，則進入審核
if nlevel<=750 and plevel!=1 and plevel!=2 and (not (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111 or vaid==20 or vaid==21 or vaid==12 or vaid==14) or (hours>8 or continueDays>1) ):
    return True

# 預設：如果不符合上述進入條件，則不進入人事承辦審核
return False