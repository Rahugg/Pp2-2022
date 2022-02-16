import random

def Guess_the_number(name,tries,check):
    guess = int(input("Take a guess.\n"))
    if(guess<check):
        print("\nYour guess is too low.")
    elif(guess>check):
        print("\nYour guess is too high.")
    else:
        print(f'Good job, {name} You guessed my number in {tries} guesses!')
        exit()
    Guess_the_number(name,tries+1,check)


name = input("Hello! What is your name?\n")
print(f'\nWell, {name}, I am thinking of a number between 1 and 20.')

Guess_the_number(name,0,random.randint(1,20))