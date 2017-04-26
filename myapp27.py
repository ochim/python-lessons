# リスト型とタプル
# 集合型
# 辞書型

sales = {"taguchi": 200, "fkoji": 400}
print(sales["fkoji"])
sales["fkoji"] = 500
sales["dotinstall"] = 800
del(sales["taguchi"])
print(sales)

for key, value in sales.items():
    print("{0} = {1}".format(key, value))
