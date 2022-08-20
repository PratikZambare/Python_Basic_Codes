"""print("Program to print stars :")
one = int(input("enter the number of rows do you want to print : "))
new = bool(input("0 fo reverse and 1 for normal : "))
if new == True :
    for i in range(1,one+1):
        for j in range(1 , i+1):
            print("*", end=(" "))
            print()"""


print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()