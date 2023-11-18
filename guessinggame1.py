#the guessing game
import random
random = (random.randint(1, 100))
yourguess =  int(input("enter guess"))
if random == yourguess:
    print("got it")
else:
    print("try again","missed by",random-yourguess)
