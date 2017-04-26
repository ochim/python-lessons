# クラスの継承
# User -> AdminUser

class User:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("hi {0}".format(self.name))

class AdminUser(User):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def say_hello(self):
        print("hello {0} ({1})".format(self.name,self.age))

    #override
    def say_hi(self):
        print("[admin] hi {0}".format(self.name))

bob = AdminUser("bob",23)
print(bob.name)
print(bob.age)
bob.say_hi()
bob.say_hello()
