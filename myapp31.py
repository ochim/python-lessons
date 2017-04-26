# 内包表記

# 0 - 9
# print([i for i in range(10)])
# print([i*3 for i in range(10)])
# print([i*3 for i in range(10) if i%2 == 1])

# ジェネレータ
print(i*3 for i in range(10) if i%2 == 1)
# 集合体
print({i*3 for i in range(10) if i%2 == 1})
