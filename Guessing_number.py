import random

rand_num = random.randint(0, 100)

print("\n\t\t\t\t~~~~~~~~~~~~~~ Welcome to the game of guessing numbers ~~~~~~~~~~~~~~~~")
print("You will get total 7 chance to guess the correct number.\n")
a = 0
while(a < 7):
    print("Chance left--> ", 7-a)
    inp_num = int(input('Enter number between 0 to 100 :\t'))

    if 0 < inp_num < 100:
        if rand_num == inp_num:
            print("\tCongratulations!! Your guess is absolutely correct in try ", a)
            break
        elif inp_num < rand_num:
            print("You guessed too low.")
            a = a+1
            continue
        elif inp_num > rand_num:
            print("You guessed too high.")
            a = a+1
            continue

    else:
        print("Invalid input!! Try again.")

if a == 7:
    print(f"\tThe correct number was {rand_num}")
    print("\tThanks for playing. Hope to see you again.")
