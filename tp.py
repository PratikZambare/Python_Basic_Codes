print("print the stars in reverse or normal manner")
user = int(input("1 for normal for 0 for reverse : "))
stars = int(input("How many stars do you wanna print : "))
new = bool(user)

if user ==True :
    for i in range(stars+1) :
        for j in range(i) :
            print("*", end=" ")
        print()
elif user ==False :
    for i in range(stars ,0,-1) :
        for j in range(i) :
            print("*", end=" ")
        print()
