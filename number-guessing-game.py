import random

def main():
    welcome()
    game()


def game():
    attempts = 0
    levels = {1: "Easy", 2:"Medium", 3:"Hard"}
    chances = 0
    guess = 0
    number = random.randrange(1, 101)

    while True:
        try:
            level = int(input("Enter your choice: "))
            print(f"\nGreat! You have selected the {levels[level]} difficulty level")
            match level:
                case 1: chances = 10
                case 2: chances = 5
                case 3: chances = 3
            break
        except(ValueError, KeyError):
            pass

    while attempts != chances or guess != number:
        attempts += 1
        while True:
            try:
                guess = int(input("Enter your guess: "))
                break
            except(ValueError):
                pass

        if guess > number:
            print(f"Incorrect! The number is less than {guess}")
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}")
        else:
            print(f"Congratulations! you guessed the number in {attempts} attempts")
            retry = input("Type yes if you want to play again!: ").lower()
            if  retry == "yes":
                attempts = 0
                number = random.randrange(1, 101)
                continue
            else:
                break

    

def welcome():
    print("\n-- Welcome to the Number Guessing Game! -- ")
    print("I'm thinking of a number between 1 and 100.")
    print("\nSelect your difficulty level: ")
    print("1.) Easy (10 chances)")
    print("2.) Medium (5 chances)")
    print("3.) Hards (3 chances)")
    print()

if __name__ == "__main__":
    main()
