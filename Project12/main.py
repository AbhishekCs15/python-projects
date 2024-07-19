import random
from art import logo
print(logo)
num1 = random.randint(1, 100)

print("Welcome to the Number guessing Game!")

print("your task is to find a number between 1 to 100")


def main(lives):
    print(f"you only have {lives} chances")

    for liv in range(0, lives, 1):
        guess1 = int(input("enter the first guess number"))
        if guess1 < 0 or guess1 > 100:
            print("enter valid input")
            exit()
        if guess1 == num1:
            print(f"you won, the correct answer is {num1} ")
            exit()
        if guess1 >= num1:
            print("high")
        elif guess1 <= num1:
            print("low")
        lives -= 1
    print(f"nice try but correct answer is {num1}")


choice = input(f"You want to play 'easy' or 'hard' ").lower()
if choice == 'easy':
    main(10)
elif choice == 'hard':
    main(5)
else:
    print("enter valid input")
