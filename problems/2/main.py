# =======================================================================================================
### ======= ###
### IMPORTS ###
### ======= ###
import numpy as np 

from helpers.data import load_data

# =======================================================================================================
### ==== ###
### CODE ###
### ==== ###

# Loading the data. 
data = load_data("input.txt")

# PART 1: Computing the total amount of wrapping paper required.
total = 0 
for present in data: 
    total += 2*present[0]*present[1] + 2*present[1]*present[2] + 2*present[2]*present[0] + min(present[0]*present[1], present[1]*present[2], present[2]*present[0])

# PART 2: Including Ribbons
total = 0 
for present in data: 
    present.sort()
    total += present[0]*2 + present[1]*2 + np.prod(present)

print(total)
    