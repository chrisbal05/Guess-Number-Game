import random
game = False

def guess(x):
    guessCount = 0
    random_number = random.randint(1, x)
    guess = 0
    while game == False:
        while guessCount <= 7:
            while guess != random_number:
                guess = int(input(f"Guess a number between 1 and {x}: "))
                if guess < random_number:
                    guessCount += 1     
                    print("Too Low!")
                elif guess > random_number:
                    print("Too High")
                    guessCount += 1
                elif guess == random_number:    
                    print(f"You have guessed the number {random_number}")
                    tryAgain()
        print("Sorry. No tries left!")
        tryAgain()

def tryAgain():
    ask1 = str(input("Would you like to play again?(y/n): "))
    if ask1 == "y":
        guessCount = 0
        game = False
    elif ask1 == "n":
        game = True
        print("Goodbye")
        quit()


        
guess(100)