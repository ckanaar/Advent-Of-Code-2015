# =======================================================================================================
### ======= ###
### IMPORTS ###
### ======= ###
from helpers.data import load_data

# =======================================================================================================
### ==== ###
### CODE ###
### ==== ###

# Loading the data.
data = load_data("input.txt")

# PART 1: Going through the data to count the floor. 
floor = 0 
for char in data: 
    if char == '(': 
        floor += 1 
    elif char == ')': 
        floor -= 1

# PART 2: Finding the first character that lands Stana in the basement. 
running  = True 
position = 1
floor    = 0 
while running:

    if data[position - 1] == '(': 
        floor += 1
    elif data[position - 1] == ')': 
        floor -= 1
    
    if floor == -1: 
        running = False 
        print(position)
    
    else: 
        position += 1
    