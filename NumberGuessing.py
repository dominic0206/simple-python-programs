import random
import math

#User input for lower bound and upper bound of guessing
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

#Generating random number
rand = random.randint(lower,upper)

#Limiting number of trials
trials = round((upper - lower)/3)
print("\nYou only have ",trials," chances to guess!\n")

#Initializing number of trials
count = 0

#To commit the number of trials
while count < trials:
    
    #User input guess
    guess = int(input("Guess: "))

    #Comparing guess to generated number
    if rand == guess:
        print("Congratulations you guessed it right")
        break
    elif rand > guess:
        print("Your guess is too small! Guess higher")
        count += 1
    elif rand < guess:
        print("Your guess is too high! Guess smaller")
        count += 1

#To break if number of trials exceeded or obtained
if count >= trials:
    print("\nThe number is %d" %rand, "\nBetter luck next time")

   
    