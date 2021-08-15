import random

number = random.randrange(1,9)

title1 = "Guess my number (It is between 1 and 9) You get 5 guesses"
print(title1)

inputNumber = int(input("Enter your guess: "))

for i in range(1,5):    
    if (inputNumber < number):
        print("Oops! Your guess was wrong. Pick a number higher than ",inputNumber)
        inputNumber = int(input("Enter your guess: "))

    elif (inputNumber > number):
        print("Oops! Your guess was wrong. Pick a number lower than ", inputNumber)
        inputNumber = int(input("Enter your guess: "))
    elif (inputNumber == number):
        print("Congratulations! You guessed my number")
else:
    print("You Lost")
    
