# =======================================================================================================
### ======= ###
### IMPORTS ###
### ======= ###

from helpers.data import load_data
from helpers.string import check_naughty, check_naughty_2, is_really_nice

# =======================================================================================================
### ==== ###
### CODE ###
### ==== ###

# # Loading the data. 
data = load_data("input.txt")

# # PART 1: Checking the number of naughty strings. 
# total = 0 
# for item in data:
#     if check_naughty(item) == True: 
#         total += 1 
    
# print(total)

# # PART 2: Checking the number of naughty strings. 
total = 0
for item in data:
    print(item) 
    if is_really_nice(item) == True: 
        total += 1 
print(total)


