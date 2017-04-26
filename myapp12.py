# function

msg = "global hello" # global variable

# def say_hi():
#     msg = "local hello" # local variable
#     print(msg)

def say_hi():
    global msg
    msg = "write global hello"
    print(msg)

say_hi()
print(msg)
