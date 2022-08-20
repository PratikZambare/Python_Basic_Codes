import random

lst = ['s','w','g']
chance = 10
no_of_chance = 0
no_of_chance_left = 10
computer_point = 0
human_point = 0

print("\t\t\t\t\t || Snake , Gun , Water Game || \t\t\t\t\t")
print('''Enter your choice : 
s for snake
g for Gun
w for water
choice? : ''')

while no_of_chance < chance :
    _input = input("Snake , Gun , Water : ")
    _random = random.choice(lst)

    if _input == _random :
        print("Tie Both have 0 point in this round")
    elif _input == 's' and _random == 'w':
        print(f"You guess {_input} and computer guess is {_random}")
        human_point = human_point + 1
        print("human won : 1 points to human ")
    elif _input == 's' and _random == 'g':
        print(f"You guess {_input} and computer guess is {_random}")
        computer_point = computer_point+1
        print("Computer won : 1 point to computer ")
    elif _input == 'g' and _random == 'w':
        print(f"You guess {_input} and computer guess is {_random}")
        computer_point = computer_point + 1
        print("Computer won : 1 point to computer ")
    elif _input == 'g' and _random == 's':
        print(f"You guess {_input} and computer guess is {_random}")
        human_point = human_point + 1
        print("human won : 1 points to human ")
    elif _input == 'w' and _random == 'g':
        print(f"You guess {_input} and computer guess is {_random}")
        human_point = human_point + 1
        print("human won : 1 points to human ")
    elif _input == 'w' and _random == 's':
        print(f"You guess {_input} and computer guess is {_random}")
        computer_point = computer_point + 1
        print("Computer won : 1 point to computer ")
    else :
        print("Wrong input !")
    no_of_chance = no_of_chance + 1
    no_of_chance_left = no_of_chance_left - 1
    print("Chances Left : ",no_of_chance_left)
    print()

print("\n\t\t\t\t\t || Game Over || \n\t\t\t\t\t")

if human_point < computer_point :
    print("\n\t || Human Got : ",human_point," points and Computer got",computer_point,"points || \t\t\t\t\t\n")
    print("\n\t\t\t\t\t || Computer wins || \t\t\t\t\t")

if computer_point<human_point :
    print("\n\t || Human Got : ",human_point," points and Computer got",computer_point,"points || \t\t\t\t\t\n")
    print("\n\t\t\t\t\t || Human wins || \t\t\t\t\t")

if computer_point==human_point :
    print("\n\t || Human Got : ",human_point," points and Computer got",computer_point,"points || \t\t\t\t\t\n")
    print("\t\t\t\t\t || There is draw between you and computer || \t\t\t\t\t")




