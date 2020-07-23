import random


MAX_NUMBER = 1000


def guess():
    guess_number = random.randint(1, MAX_NUMBER)
    tries = 0
    while True:
        number = input(f"Guess the number between 0 and {MAX_NUMBER}:")
        if number.isdigit():
            number = int(number)
            if number == guess_number:
                print(
                    "Correct, the number was %s. You did %s guesses."
                    % (guess_number, tries)
                )
                break
            tries += 1
            if number < guess_number:
                print("Higher")
            else:
                print("Lower")
        else:
            print("Write a number")


if __name__ == "__main__":
    guess()
