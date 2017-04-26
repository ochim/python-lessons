# class

class User:
    # clss variable
    count = 0
    def __init__(self,name):
        User.count += 1
        self.name = name

print(User.count)
tom = User("t")
bob = User("b")
print(User.count)
print(bob.count)
