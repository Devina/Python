from random import randint

print("...Rock...")
print("...Paper...")
print("...Scissors...")
player_choice = input("(Enter your choice): ").lower()
computer_choice = randint(0, 2)

if computer_choice == 1:
    computer_choice = "rock"
    print("Computer choice: Rock")
elif computer_choice == 2:
    computer_choice = "paper"
    print("Computer choice: Paper")
else:
    computer_choice = "scissors"
    print("Computer choice: Scissors")

if ((player_choice == "rock" or player_choice == "paper" or player_choice == "scissors") and (computer_choice == "rock" or computer_choice == "paper" or computer_choice == "scissors")):
    if player_choice == computer_choice:
        print ("it's a draw!")
    elif player_choice == "rock":
        if computer_choice == "paper":
            print ("Computer wins!")
        else:
            print ("you win!")
    elif player_choice == "paper":
        if computer_choice == "scissors":
            print ("Computer wins!")
        else:
            print ("you win!")
    elif player_choice == "scissors":
        if computer_choice == "rock":
            print ("Computer wins!")
        else:
            print ("You win!")
else:
    print("Invalid input detected")
