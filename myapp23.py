# リスト

scores = [40,50]

print(scores[1])
scores[0]= 45
print(len(scores))

scores.append(100)
print(scores)

# for score in scores:
#     print(score)

# i:index, score:要素
for i,score in enumerate(scores):
    print("{0}: {1}".format(i,score))
