# イテレータ

scores = [40, 50, 70, 90, 60]
# it = iter(scores)
# print(next(it))
# print(next(it))
# print("hoge")
# print(next(it))
#
# for score in scores:
#     print(score)

def get_infinite(): # generator
    i = 0
    while True:
        yield i * 2
        i += 1

g = get_infinite()
print(next(g))
print(next(g))
