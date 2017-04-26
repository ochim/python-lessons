# モジュール

# import user
from user import AdminUser, User

bob = AdminUser("bob", 23)
tom = User("tom")

print(bob.name)
bob.say_hi()
bob.say_hello()
tom.say_hi()
