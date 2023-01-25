import random

total_score = 0
attempts = 0

while True:
    number = random.randint(1, 10) # Generate a random number
    print("Guess a number: ")
    while True:
        guess = int(input())
        attempts += 1
        if guess == number:
            if attempts == 1:
                total_score += 1
            else:
                total_score += 1 - (attempts * 0.2)
            print("Correct guess! Your score is: {:.2f}".format(total_score))
            attempts = 0
            break
        elif guess > number:
            print("Guess a smaller number")
        else:
            print("Guess a bigger number")
        if attempts == 5:
            print("You ran out of attempts. No score.")
            attempts = 0
            break

    play_again = input("Do you want to play again? (y/n)")
    if play_again.lower() != "y":
        print("Your total score is: {:.2f}".format(total_score))
        break
