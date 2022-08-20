# a = 9
# b = 8
# c = sum((a, b)) # built in function

def function1(a, b):
    print("Hello you are in function 1", a+b) # This is a way to creaate a new simple function

def function2(a, b):
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""
    average = (a+b)/2
    # print(average)
    return average

# v = function2(5, 7)
# print(v)
print(function2.__doc__) # Giving a strings as an messege for a any programmer that use your code after you
                        # to give a messege to him for simplicity to know that waht is the work for this function defined
print(function2(2,4))
