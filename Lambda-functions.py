# # def add(a, b):
# #     return a+b
# #
# # # minus = lambda x, y: x-y #lambda is known as a one line function
# #
# # def minus(x, y):
# #     return x-y
# #
# # print(minus(9, 4))
#
# def a_first(a):
#     return a[1]
#
# a = [[1,2],[7,6],[4,1]]
# b = [[1,2],[7,6],[4,1]]
# a.sort(key=lambda x : x[0]) # lambda x : x[0] - this type of create fun called anonymous function
# b.sort(key=a_first)
# print(a)
# print(b)

plus = lambda x , y : x+y
minus = lambda x , y : x-y
multi = lambda x , y : x*y
div = lambda x , y : x/y

ch = int(input('''enter your choice : 
1 - add
2 - subtract
3 - multiply
4 - division
choice? : '''))

x = int(input("1st number : "))
y = int(input("2nd number : "))
if ch == 1 :
    print("Addition is : ", plus(x, y))
elif ch == 2 :
    print("Subtraction is : ", minus(x, y))
elif ch == 3 :
    print("Multiplication is : ", multi(x, y))
elif ch == 4 :
    print("Division is : ", div(x, y))
else :
     print("fuck off !")





