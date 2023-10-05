# Rock paper game: Nixal_T
import random

while True:
    pick_one = ["rock", "paper", "scissors"]
    comp = random.choice(pick_one)
    player = None
    while player not in pick_one:
        player = input("'rock','paper' or 'scissors': ").lower()
    if comp == player:
        print("Player: ", player)
        print("Computer: ", comp)
        print("You tie!")
    elif player == "rock":
        if comp == "paper":
            print("Player: ", player)
            print("Computer: ", comp)
            print("You lose!!")
        if comp == "scissors":
            print("Player: ", player)
            print("Computer: ", comp)
            print("You win!!")
    elif player == "paper":
        if comp == "rock":
            print("Player: ", player)
            print("Computer: ", comp)
            print("You win!!")
        if comp == "scissors":
            print("Player: ", player)
            print("Computer: ", comp)
            print("You lose!!")
    elif player == "scissors":
        if comp == "rock":
            print("Player: ", player)
            print("Computer: ", comp)
            print("You lose!!")
        if comp == "paper":
            print("Player: ", player)
            print("Computer: ", comp)
            print("You win!!")
    play_again = input("Do you want to play again (yes/no): ").lower()
    if play_again != "yes":
        break

print("BYE! Thank you for playing!!")

# WIN CONDITIONS:
# (comp)    (Player)
# paper - scissors --> comp lose
# paper - rock --> comp win
# paper - paper --> tie

# rock - rock
# rock - scissors
# rock - paper

# scissors - scissors
# scissors - rock
# scissors - paper
