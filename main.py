from sys import argv
import random


def input_validate(int):
    if int < 9 and int > -1:
        # Input validation "Success"
        if xState[int] == 0 and zState[int] == 0 :
            return 1
        elif bot == 1:
            return 0
        else:
            print(f"You've entered {int}!\nDon't try to Change privious inputs!")
            return 0
    else:
        return 0


def structure(xState, zState):
    
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)

    # Printing proper structure
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

    pass


def change_state(who, int):
    global xState
    global zState
    if who == "X":
        xState[int] = "X"
    elif who == "Z":
        zState[int] = "Z"



def check_win(xState, zState):
    def win_test():
        # Win cases
        if zState[3] == "Z" and zState[4] == "Z" and zState[5] == "Z":
            return 2 # 2 for Z 
        elif zState[0] == "Z" and zState[1] == "Z" and zState[2] == "Z":
            return 2
        elif zState[6] == "Z" and zState[7] == "Z" and zState[8] == "Z":
            return 2
        elif zState[0] == "Z" and zState[4] == "Z" and zState[8] == "Z":
            return 2
        elif zState[2] == "Z" and zState[4] == "Z" and zState[6] == "Z":
            return 2        
        elif zState[0] == "Z" and zState[3] == "Z" and zState[6] == "Z":
            return 2
        elif zState[1] == "Z" and zState[4] == "Z" and zState[7] == "Z":
            return 2
        elif zState[2] == "Z" and zState[5] == "Z" and zState[8] == "Z":
            return 2
        elif xState[3] == "X" and xState[4] == "X" and xState[5] == "X":
            return 1 # 1 for X
        elif xState[0] == "X" and xState[1] == "X" and xState[2] == "X":
            return 1
        elif xState[6] == "X" and xState[7] == "X" and xState[8] == "X":
            return 1
        elif xState[0] == "X" and xState[4] == "X" and xState[8] == "X":
            return 1
        elif xState[2] == "X" and xState[4] == "X" and xState[6] == "X":
            return 1
        elif xState[0] == "X" and xState[3] == "X" and xState[6] == "X":
            return 1
        elif xState[1] == "X" and xState[4] == "X" and xState[7] == "X":
            return 1        
        elif xState[2] == "X" and xState[5] == "X" and xState[8] == "X":
            return 1
        else:
            # No player won yet
            return 0

        
    if win_test() == 1:
        return 1
    elif win_test() == 2:
        return 2
    else:
        return 0



if __name__ == "__main__":

    print("Welcome to TicTacToe Game!")

    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    try :
        print(f"Welcome {argv[1].capitalize()}")
        user_name = argv[1]
    except :
        user_name = input("\nEnter your name: ")
    
    user_name = user_name.capitalize()

    turn = 0    # Turn 0 is X's turn & 1 is O's turn

    chance_left = 9 #This is how many chance left for X & Y to continue play

    bot_ask = input("Do you want to play with bot ? \nPress Y/y/1/Yes for yes \nPress N/n/0/No for play with another player : ")

    if bot_ask[0] == "Y" or bot_ask[0] == "y" or bot_ask[0] == "1" or bot_ask[0] == "Yes" or bot_ask[0] == "True":
        bot = 1
    else:
        bot = 0
    

    print(f"\nHello {user_name}! Enjoy this game... \n ")
    
    print(f" 0 | 1 | 2 ")
    print(f"---|---|---")
    print(f" 3 | 4 | 5 ")
    print(f"---|---|---")
    print(f" 6 | 7 | 8 ")

    while (chance_left>0):
        if turn == 0:
            x_input = int(input("Enter X's Input: "))
            intt = input_validate(x_input)
            if intt:
                change_state("X", x_input)
                structure(xState, zState)
                turn = 1
                chance_left -= 1
            else:
                print("Enter valid input!!")
        else :
            if bot == 1:
                z_input = int(random.randrange(0,8))
                print(f"Z's input is {z_input} \n")
            else:
                z_input = int(input("Enter Z's Input: "))
            intt = input_validate(z_input)
            if intt:
                change_state("Z", z_input)
                structure(xState, zState)
                turn = 0
                chance_left -= 1
            elif intt is False and bot == 1:
                pass
            else:
                print("Enter valid input!!")
            
        check_win(xState, zState)
        if check_win(xState, zState) == 0:
            continue
        elif check_win(xState, zState) == 1:
            print("\nX win " *5)
            break
        elif check_win(xState, zState) == 2:
            print("\nZ win " *5)
            break
        else:
            print("Check 'check win func ()' \n Error!!!!")
            exit(1)
    

if chance_left == 0:
    print("Match draw!!")

print(f"Thanks for playing {user_name} Hope you've enjoyed the game!\n")
exit()

# https://youtu.be/0LHmevWVvpc

# https://www.youtube.com/watch?v=ci9kHFl0OEs
