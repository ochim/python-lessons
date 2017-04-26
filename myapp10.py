# method
# def say_hi():
def say_hi(name, age = 20):
    # print("Hi")
    print ("hi {0} ({1})".format(name, age))

say_hi('tom',23)
say_hi("bob",25)
say_hi("jobs")
say_hi(age=18, name="rick")
