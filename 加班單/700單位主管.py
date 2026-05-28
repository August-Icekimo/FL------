# (已註解掉的邏輯) 
#  若為總經理室人員(master==4)且職級小於單位主管(800)，不須審核
# if master == 4 and nlevel < 800:
#    return False

# 檢查是否為「總經理室人員」 (人員群組-主 master == 4) 
# 且為「13職等以上人員」 (旗標 rankAbove13 == 1)
# 若是，則強制跳過此單位主管關卡
if master == 4 and rankAbove13 == 1:
    return False

# 檢查申請人職級是否為「副單位主管」含以下 (nlevel <= 750)
# 若是，則需要經過此「單位主管」關卡審核
if nlevel <= 750:
    return True 

# 職級為單位主管(800)含以上者，不需經過此關卡審核
return False
