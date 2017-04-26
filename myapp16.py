# class
# method

class User:
    # clss variable
    count = 0
    # constructor
    def __init__(self,name):
        User.count += 1
        self.name = name
    # instance method
    def say_hello(self):
        print ("hello {0}".format(self.name))
    # class method
    @classmethod
    def show_info(cls):
        print("{0} instances".format(cls.count))

tom = User("tom")
bob = User("bob")

tom.say_hello()
bob.say_hello()

User.show_info()
