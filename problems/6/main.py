# =======================================================================================================
### ======= ###
### IMPORTS ###
### ======= ###

from concurrent.futures import process
from helpers.data import load_data
from helpers.lights import process_lights, process_brightness

# =======================================================================================================
### ==== ###
### CODE ###
### ==== ###

# Loading the data. 
data = load_data("input.txt")

# Creating an array of lights. 
lights = [[0 for _ in range(1000)] for _ in range(1000)]

# Processing the commands.
for idx, command in enumerate(data):
    lights = process_brightness(command[0], command[1], command[2], lights)

# Counting the number of lights lit. 
total = sum([sum(row) for row in lights])
print(total)




