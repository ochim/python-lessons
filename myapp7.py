# if
score = int(input("score ? "))

if score > 80:
    print("great!")
elif score > 60:
    print ("good!")
else:
    print("so so .....")

print("Great!!" if score > 80 else "so so ...")
