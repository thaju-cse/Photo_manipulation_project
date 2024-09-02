import random

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass

def main():
    # Prompt the user for a level
    level = get_positive_integer("Level: ")

    # Generate a random number between 1 and the specified level
    number = random.randint(1, level)

    while True:
        # Prompt the user to guess the number
        guess = get_positive_integer("Guess: ")

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
