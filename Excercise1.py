# Guess the number : -
n = 18
guess = 10
while(guess > 0) :
    print("Chance Left : " , guess)
    guess = guess - 1
    m = int(input("Enter the number of your guess : "))
    if m < n :
        print("Increase your guess number : \n")
        continue
    elif m > n :
        print("Decrease your guess number : \n")
        continue
    else :
        print("Congrats | You Guess the correct number \n")
        print(10-guess, ". no of He/she guesses to finish ...")
        break
if guess == 0 :
    print("\n\t\tGame Over ... \n")