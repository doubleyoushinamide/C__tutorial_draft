# Imports the necessary library for selecting random objects
import random

# Create the regional lists of states
northeast = ["MA", "RI", "CT", "NH", "VT", "ME"]
south = ["VA", "DE", "MD", "NC", "SC", "GA", "FL"]
midwest = ["OH", "IL", "IN", "KY", "MI", "WI"]
west = ["CA", "OR", "WA", "NV", "AZ", "UT", "MT"]

# Ask user for input state
state = input("Type in a US State: ")

# Select a random state from that list, excluding the input state
if state in northeast:
    random_state = random.choice([state for state in northeast if state != state])
elif state in south:
    random_state = random.choice([state for state in south if state != state])
elif state in midwest:
    random_state = random.choice([state for state in midwest if state != state])
elif state in west:
    random_state = random.choice([state for state in west if state != state])

# Prints the selected random state
print("The randomly selected state is: "+random_state)
