import random
m = ["Rock", "Paper", "Scissors"]
computer = m[random.randint(0,2)]

player = False

while player == False:
    player = input("Enter your name:")
    if computer == player:
        print("It's a tie")
    elif player == 'Rock':
        if computer == 'Paper':
            print("You loose. The computer wins")
        else:
            print("You win!")
    elif player == 'Paper':
        if computer == 'Scissor':
            print("You loose. The computer wins")
        else:
            print("You win!")
    elif player == 'Scissor':
        if computer == 'Rock':
            print("You loose. The computer wins")
        else:
            print("You win!")
    new_game = input("Do you want to play another round? (y/n)")
    if yes
        player = False
else:
    print("Thanks a lot for playing!")
    break
