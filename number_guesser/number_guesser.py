import random

top_of_range = input("Type a number: ")
# r = random.randrange(-10, 11)  # this function is not inclusive of the stoping number if you want 10 set it o 11
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()
r = random.randint(0, top_of_range)  # includes the number in the rang
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == r:
        if user_guess <= 2:
            print("You guessed it in", guesses, "guesses. \nYou are guessing genius")
        else:
            print("You got it in", guesses, "guesses")

        break
    elif user_guess > r:
        print("To high")
    else:
        print("Too low")
