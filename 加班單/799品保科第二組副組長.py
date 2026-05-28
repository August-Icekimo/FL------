# 檢查人員的簽核部門是否屬於「第一工廠」或「第二工廠」 (plevel == 1 或 plevel == 2)
# 並且申請人的職級必須小於或等於「組長/課長」 (nlevel <= 700)
if plevel in (1, 2) and nlevel <= 700:
    # 滿足條件者，加班單需經過「品保科第二組副組長」關卡簽核
    return True

# 不滿足上述條件者，跳過此關卡
return False
