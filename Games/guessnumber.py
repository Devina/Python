import random

random_number = random.randint(1, 10)
player_guess = int(input("Guess a number between 1 and 10: "))

while True:
    if player_guess == random_number:
        print("You guessed the number")
        restart_game = input("Type 'y' to play again: ")
        if restart_game == "y":
            player_guess = int(input("Guess a number between 1 and 10: "))
            random_number = random.randint(1, 10)
        else:
            print ("Thanks for playing")
            break;
    elif player_guess < random_number:
        print("Your guess is low, try again")
        player_guess = int(input("Guess new number: "))
    else:
        print("Your guess is high, try again")
        player_guess = int(input("Guess new number: "))
