# 判斷是否需要經過「人事副主任」簽核關卡

# 若假別為防疫相關假別或理監事會務假，必須經過人事副主任簽核
# 117: (不支薪)防疫照顧假, 118: 防疫病假, 119: 防疫隔離假, 120: (不支薪)疫苗接種假, 67: 理監事會務假
if vaid==117 or vaid==118 or vaid==119 or vaid==120 or vaid==67: 
    return True

# 若假別為公假(本廠公務)(7)、理監事會務假(67)、公務(6)、公差(5)、遞延休假(21)，則跳過此關
# （註：上方已判斷 vaid==67 回傳 True，此處 67 的判斷實際上不會被執行）
if vaid==7 or vaid==67 or vaid==6 or vaid==5 or vaid==21: 
    return False

# 若部門為第一工廠(1)或第二工廠(2)，則跳過此關 (註: 人事副主任主要審核總廠或非一二廠單位)
if plevel==1 or plevel==2: 
    return False

# 職級在「單位主管」(800)(含)以上者，不經過人事副主任
if nlevel>=800: 
   return False

# 針對職級為「副單位主管」(750) 的請假條件：
# 1. 事假(12)、休假(20)、遞延休假(21)、特准病假(15) 且 請假時數 <= 8 小時
# 2. 公出(4)、公假(本廠公務)(7)、及各類補休 (35加班, 36出差, 37值班, 38公務, 109行政值班, 110電機值班, 111警衛幹部值班)
# 若符合上述任一條件，跳過人事副主任簽核
if nlevel==750 and (((vaid==12 or vaid==20 or vaid==21 or vaid==15) and hours<=8) or (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111)):
   return False

# 針對職級在「副單位主管」(750)(含)以下，且非第一工廠(1)、第二工廠(2)之人員：
# 若為公出(4)、公假(本廠公務)(7) 或 各類補休 (35, 36, 37, 38, 109, 110, 111)，跳過人事副主任簽核
if nlevel<=750 and plevel!=1 and plevel!=2 and (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111):
    return False

# 針對職級在「副單位主管」(750)(含)以下，且非第一工廠(1)、第二工廠(2)之人員：
# 若假別「非」上述常見免簽假別（公出4/公假(本廠)7/各類補休/休假20/遞延休假21/事假12/病假14），
# 「或者」請假時數 > 8 小時，
# 「或者」連續請假天數 > 1 天，則須經過人事副主任簽核
if nlevel<=750 and plevel!=1 and plevel!=2 and (not (vaid==4 or vaid==7 or vaid==35 or vaid==36 or vaid==37 or vaid==38 or vaid==109 or vaid==110 or vaid==111 or vaid==20 or vaid==21 or vaid==12 or vaid==14) or (hours>8 or continueDays>1) ): 
    return True

# 預設跳過此關卡
return False