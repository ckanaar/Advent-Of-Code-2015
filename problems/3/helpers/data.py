# =======================================================================================================
### ======= ###
### IMPORTS ###
### ======= ###


# =======================================================================================================
### ==== ###
### CODE ###
### ==== ###

def load_data(fname: str): 

    # Opening and reading the data. 
    file = open(f"ref/{fname}", "r")
    lines = file.readlines()
    file.close()

    # Getting the characters into a list. 
    chars = [char for char in lines[0]]

    return chars 

