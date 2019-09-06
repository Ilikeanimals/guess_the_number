import random
def is_valid_number():
    if s.isdigit() and s > 1 and s < 100
        return True
def main():
    num = random.random(1,100)
    guess_num = False
    guess = input('Guess a number from 1 to 100:')
    num_guess = 0
    while not guess_num:
        if not is_valid_nu(guess):
            guess < num:
            guess = str(input("I won't count that one. A number between 1 and 100:"))
        else:
            num_guess += 1
            guess = int(guess)
        if guess < num:
            guess = str(input("Too low. Guess again"))
        elif guess > num:
            guess = str(input("Too high. Guess again"))
        else:
            print("You got it in " + num_guess + "guesses!")
            guess_num = True
        print("Thanks for playing")


