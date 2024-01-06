import random

def guess(x) :

    randon_number=random.randint(1, x)
    guess=0
    while (guess!=randon_number) :
        guess = int(input(f"enter a number from range of 1 to {x}"))
        print(guess)
        if guess < randon_number:
            print("your number is too low")

        elif guess > randon_number :
            print("number is too high!")


        else :
           print("congo u found the number")

num = int(input("enter ur range :"))
guess(num)

