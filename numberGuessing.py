import random
randomNum = (random.randint(1,100))

guessNum = int(input("Guess the number:"))
counter = 1


while guessNum != randomNum:
    if guessNum < randomNum:
        print("Guess Higher")
    else:
        print("Guess Lower")
    guessNum = int(input("Guess the number:"))
    counter+=1
print("You Guessed the right number!")
print("You took",counter,"attempts")

