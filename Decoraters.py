# def fun1():
#     print("niraj hutiya")
#
# fun2 = fun1
# del fun1
# fun2()
#
# def executor(func) : # in function function call
#     func("this")
# executor(print)

# there are 2 ways to create decorater
# 1. is who_is_pratik = dec(who_is_pratik)
# 2. @ function name to pass 2nd function name on the 2nd function head.

def dec(fun):
    def exe():
        print("executing now : ")
        fun()
        print("Executed successfully. ")
    return exe

@dec  # 2nd way
def who_is_pratik():
    print("Pratik is a good boy. ")

# who_is_pratik = dec(who_is_pratik) # 1st way

who_is_pratik()

# def calculator(add):
#     def hello():
#         a=2
#         b=3
#         print("Boom Baam")
#         add()
#         print("Ding dong")
#     return hello
#
# @calculator
# def number():
#     print("Please enter your name : ")
#     a = input()
#     print(a)
#
# number()

# Decorators means calling function passing a function as an argument.