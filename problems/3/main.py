# =======================================================================================================
### ======= ###
### IMPORTS ###
### ======= ###

from collections import Counter 

from helpers.data import load_data

# =======================================================================================================
### ==== ###
### CODE ###
### ==== ###

data = load_data("input.txt")

def convert(lst):
    return tuple(lst)

# PART 1. 
# Empty list with positions
positions = []

# Starting position
position = [0 , 0]
positions.append(convert(position))

for idx, char in enumerate(data): 
    if char == "^": 
        position[0] += 1
    elif char == "v": 
        position[0] -= 1
    elif char == "<": 
        position[1] += 1
    elif char == ">": 
        position[1] -= 1

    # Appending the position to the list of positions. 
    positions.append(convert(position))

# Counting the number of times each position was visited.
count = Counter(positions)

# PART 2. 
# Splitting the data into Stanta's and Robot Stanta's parts. 
data_santa = data[1::2]
data_robot_santa = data[::2]

positions_santa = []
positions_robot_santa = []

position_santa = [0 , 0]
position_robot_santa = [0 , 0]
positions_santa.append(convert(position_santa))
positions_robot_santa.append(convert(position_robot_santa))

for idx, char in enumerate(data_santa): 
    if char == "^": 
        position_santa[0] += 1
    elif char == "v": 
        position_santa[0] -= 1
    elif char == "<": 
        position_santa[1] += 1
    elif char == ">": 
        position_santa[1] -= 1

    # Appending the position to the list of positions. 
    positions_santa.append(convert(position_santa))

for idx, char in enumerate(data_robot_santa): 
    if char == "^": 
        position_robot_santa[0] += 1
    elif char == "v": 
        position_robot_santa[0] -= 1
    elif char == "<": 
        position_robot_santa[1] += 1
    elif char == ">": 
        position_robot_santa[1] -= 1

    # Appending the position to the list of positions. 
    positions_robot_santa.append(convert(position_robot_santa))

positions_total = positions_santa + positions_robot_santa
count = Counter(positions_total)
print(len(count))




