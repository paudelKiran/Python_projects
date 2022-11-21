# Rock, scissor and paper game
import random


def com_choice():
    return random.randint(1, 3)


usr_score = 0
comp_score = 0
tied = 0
loop = 1

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~ WELCOME TO THE ROCK SCISSOR AND PAPER GAME ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("------------>>>> By Kiran Paudel")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ ENJOY YOUR GAME ~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("\nGAME RULES :\n\t1.Person to score more points till end will be the winner.\n\t2.You will be only given 3 chances.\n\t3.If both you and computer have same choice or same score at the end then it would be tie.")


def main():
    global usr_score, comp_score, tied, loop
    usr_score = 0
    comp_score = 0
    tied = 0
    loop = 1

    while(loop < 6):
        com_choice()
        print(
            "\nPlease enter your choice in numbers.[1.Rock\t2.Scissor\t3.Paper")
        usr_choice = int(input("---> "))

        if(usr_choice in [1, 2, 3]):
            result(usr_choice, com_choice())
            loop = loop+1

        else:
            print("Invalid Input!! Try again.")

    if(usr_score > comp_score):
        print("\n\t\tFinally, You are the winner!!!!! Congratulations! ")
    elif(comp_score > usr_score):
        print("\n\t\tFinally, Computer is the winner!!!!! Try again next time.. ")
    else:
        print("\n\t\tGame tied!!!")


def result(usr_choice, comp_choice):
    """
    1.Rock
    2.Scissor
    3.Paper
    """
    global usr_score, comp_score, tied, loop
    if(usr_choice == comp_choice):
        tied += 1
        print(
            f"Tied!!\t Your Score: {usr_score}\t Computer Score: {comp_score}\t Tied: {tied}")
    elif(usr_choice == 1 and comp_choice == 2):
        usr_score += 1
        print(
            f"You won!!\t Your Score: {usr_score}\t Computer Score: {comp_score}\t Tied: {tied}")
    elif(usr_choice == 1 and comp_choice == 3):
        comp_score += 1
        print(
            f"Computer won!!\t Your Score: {usr_score}\t Computer Score: {comp_score}\t Tied: {tied}")
    elif(usr_choice == 2 and comp_choice == 1):
        comp_score += 1
        print(
            f"Computer won!!\t Your Score: {usr_score}\t Computer Score: {comp_score}\t Tied: {tied}")
    elif(usr_choice == 2 and comp_choice == 3):
        usr_score += 1
        print(
            f"You won!!\t Your Score: {usr_score}\t Computer Score: {comp_score}\t Tied: {tied}")
    elif(usr_choice == 3 and comp_choice == 1):
        usr_score += 1
        print(
            f"You won!!\t Your Score: {usr_score}\t Computer Score: {comp_score}\t Tied: {tied}")
    elif(usr_choice == 3 and comp_choice == 2):
        comp_score += 1
        print(
            f"Computer won!!\t Your Score: {usr_score}\t Computer Score: {comp_score}\t Tied: {tied}")


def again():
    main()
    print("\nDo you want to play again [y/n]??")
    repeat = input("--> ")
    if (repeat.upper() == "Y"):
        print("\t\tNEW GAME")
        main()
    else:
        print("Thanks for playing. Hope to see you soon..")


again()
