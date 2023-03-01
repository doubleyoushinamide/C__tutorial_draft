#Project name: Gee001
# definite importations to avoid memory leaks or lagging issues
from random import randint
from math import log2

# User defined upper and lower bounds whence the guessing can range from

upper, lower = int(input("Input upper bound: \n")), int(input("Input lower bound: \n"))

#Gee001 chooses a random number between upper and lower limits
sysChoose = randint(lower, upper)

#Gee001 also assigns the maximum number of times to guess for
maxGuess = round(log2(upper - lower + 1))
print(f"You can only guess for {maxGuess} times")

#counting is set to zero
count = 0

while count < maxGuess:
    #counting increases by one for every iteration
    count += 1

    #User guesses within the loop
    userGuess = int(input(f"Kindly guess a number between {upper} and {lower}: \n"))

    #If the user predicted a jackpot
    if userGuess == sysChoose:
        print(".........................................")
        print("Congratulations! You have guessed right.")
        print("........................................")
        break

    #if the user guessed too low
    elif userGuess < sysChoose:
        print("..........................................")
        print("You are way too low! \n Try again!")
        print("..........................................")

    #condition if user guessed too high
    elif userGuess > sysChoose:
        print("..........................................")
        print("You are way too high! \n Try again!")
        print("..........................................")

    #if the user guessed too close
    if (userGuess >= sysChoose - 5) and (userGuess <= sysChoose + 5):
        print("..........................................")
        print("Weldone, you're very close! \n Try again!")
        print("........................................")


#This is an extra condition if the number of guesses are exceeded    
if (count >= maxGuess) and not (userGuess == sysChoose):
    print(f"You have guessed {maxGuess} times \nYou've then exceeded the maximum number of guesses, \nGAME OVER!")

"""
(1) The time complexity of this code is O(n)
because the number of iterations are not fixed; they depend on the minimum number of guesses,
i.e., log2(upper - lower + 1)

(2) Space complexity of this code is O(1)
because all variables used in the code are of same size (int = 4 bytes).
No extra space is required to store the variables.
"""