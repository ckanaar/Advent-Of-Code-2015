# =======================================================================================================
### ======= ###
### IMPORTS ###
### ======= ###


# =======================================================================================================
### ==== ###
### CODE ###
### ==== ###

def load_data(fname: str): 

    with open(f"ref/{fname}", "r") as file:
        lines = file.readlines()

    for idx, item in enumerate(lines): 
        clean_line = item.replace("\n", "")
        lines[idx] = clean_line

    return lines