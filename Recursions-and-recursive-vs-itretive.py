# def fact(n) : # itretive function
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac
# def factr(n) : # recursive function
#     if n == 0 or n == 1:
#         return 1
#     else :
#         return n * factr(n-1)
# def fibonacci(n): # recursive fibo
#     if n==1 :
#         return 0
#     elif n ==2 :
#         return 1
#     else :
#         return fibonacci(n-1) + fibonacci(n-2)
# num = int(input("give the number to calculate a factorial : "))
# # numb = int(input("give the number to calculate a fibonacci : "))
# print("factorial using itretive :" , fact(num))
# # print("factorial using recursive :" , factr(num))
# # print("fibonacci number is : " , fibonacci(numb))
def factorial(n):
    fact = 1
    for i in range(2 , n+1):
        fact = fact * i
    return fact

print(factorial(7))
