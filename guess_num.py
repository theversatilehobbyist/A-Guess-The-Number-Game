import random
print("This is a 'guess the number' game! You can guess a number from 1 to 10 and the program will tell you if you are right or wrong!")
while True:
    chosen_random_number = random.randint(1,10)
    print()
    guess_number = int(input("Guess a number : "))


    if guess_number == chosen_random_number:
        print("Wow you got it!")

    else:
        print("Try Again :(")
        while guess_number != chosen_random_number:
            second_guess_number = int(input("Guess the number again : "))
            if second_guess_number == chosen_random_number:
                print("Wow you got it!")
                break
    print()
    enter_or_exit = input("Would you like to exit the game? Type (y) for yes or (n) for no ")
    if enter_or_exit == "y" or "(y)" or "Y":
        print("Okay then, bye! Hope you come to play again! ")
        break

    elif enter_or_exit == "n" or "(n)" or "N":
        print("Glad you want to keep playing! ")
        print()
