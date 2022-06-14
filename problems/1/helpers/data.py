# =======================================================================================================
### ======= ###
### IMPORTS ###
### ======= ###
import os 

# =======================================================================================================
### ==== ###
### CODE ###
### ==== ###

def load_data(fname: str):
    """

    Args:
        fname (str): Name of the file.

    Returns:
        chars: List of characters.
    """
    
    # Opening and reading the file. 
    file  = open(f"ref/{fname}", "r")
    lines = file.readlines()
    file.close()

    # Getting the characters.
    chars = [char for char in lines[0]]

    return chars 

    
