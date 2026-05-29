# 【二廠人事 審核邏輯】 (與 700人事承辦 互補的 "另一端")

# === 強制進入 (Pass Quick) ===

# --- 特定假別/身分 強制審核 ---
# 理監事會務假(67)：若身分屬於「二廠人事業務範圍(second=3)」、或「派駐二廠(onlySecond=2)」、或「派駐二廠要給二廠人事名單(secondDept=1)」，則交由二廠人事審核
if vaid==67 and (second==3 or onlySecond==2 or secondDept==1):#工會假單->二廠人事
    return True

# 業務企劃中心(plevel=6)：
# 若申請「非」排除清單(公出/公假/各種補休/休假/事假/病假) 的 特殊假別
# 或 請假超過一天 (hours>8 或 continueDays>1)，則交由二廠人事審核
if plevel == 6 and (vaid not in (4, 7, 35, 36, 37, 38, 109, 110, 111, 20, 12, 14) or (hours>8 or continueDays>1)):#業務企劃中心
    return True

# 第二工廠(plevel=2) 或 二廠人事業務範圍(second=3) 的 組長/課長以下(nlevel<=700)，若申請公務(6)，則進入審核
if (plevel==2 or second==3) and nlevel<=700 and vaid==6:
  return True

# --- 非一/二廠，但屬於「二廠人事管轄」(外派/特殊單位) 長天數或特殊假別審核 ---
# 二廠人事業務範圍(second=3) 且 副主管以下(nlevel<=750) 且 非第一/第二工廠 (plevel!=1,2)：
# 若申請「非」排除清單(公出/公假/補休/休假/事假/病假) 的 特殊假別
# 或 請假超過一天 (hours>8 或 continueDays>1)，則進入審核
if second==3 and nlevel<=750 and plevel!=1 and plevel!=2 and (vaid not in (4, 7, 35, 36, 37, 38, 109, 110, 111, 20, 12, 14) or (hours>8 or continueDays>1)):
    return True

# === 排除條件 ===

# --- 全局假別與職級排除 ---
# 公假(本廠公務7)、公差(5)、遞延休假(21) 不需二廠人事審核
if vaid in (7, 5, 21):
    return False

# 單位主管(800)含以上者，本關不審 (人事僅處理副單位主管以下)
if nlevel>=800: #單位主管以上
   return False

# --- 非一/二廠 (如總公司/企劃中心等) 短假排除 ---
# 副主管以下(nlevel<=750) 且 非第一/第二工廠 (plevel!=1,2)，申請 公出(4)/公假(7)/各種補休(35-38, 109-111) 者不審
if nlevel<=750 and plevel!=1 and plevel!=2 and vaid in (4, 7, 35, 36, 37, 38, 109, 110, 111):
    return False

# --- 副單位主管(750) 特定短天數/假別排除 ---
# 職級為副單位主管(750) 申請以下情況不審：
# 1. 單日以內(<=8HR) 的事假(12)/休假(20)/遞延休假(21)/特准病假(15)
# 2. 或 公出(4)、公假(7)、各種補休(35-38, 109-111)
if nlevel==750 and ((vaid in (12, 20, 21, 15) and hours<=8) or vaid in (4, 7, 35, 36, 37, 38, 109, 110, 111)):
   return False

# 預設：如果不符合上述特定條件，則不進入二廠人事審核
return False
