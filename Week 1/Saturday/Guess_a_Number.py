import random
secretNumber = random.randint(1, 10)
def guessesLeft():
while True:
    numberGuess = int(raw_input("I am thinking of a number between 1 and 10. What's the number? "))
    if numberGuess == secretNumber:
        print "You Win!"
        break
    elif numberGuess > secretNumber:
        print "%s is too high" % (numberGuess)
    elif numberGuess < secretNumber:
        print "%s is too low" % (numberGuess)