import random

Start = 1
Finish = 10

while True:
    computer = random.randint(Start, Finish)
    player = None
    attempts = 0
    
    while player != computer:
        player = int(input(f"Guess the Number from {Start} to {Finish}: "))
        attempts += 1
        if player != computer:
            print("Incorrect, try again!")
    
    print("Correct!\n")
    print(f"# of Attempts: {attempts}")

    play_again = input("Do you wish to continue (y/n): ").lower()
    if play_again != "y":
        break

print("Thank You for Playing!")
