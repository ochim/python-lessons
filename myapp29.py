# map(関数, イテレータ)

def triple(n):
    return n * 3

print(tuple(map(triple,[4,5,6])))

# lambda 引数: 処理
print(list(map(lambda n: n*3,[4,5,6])))
