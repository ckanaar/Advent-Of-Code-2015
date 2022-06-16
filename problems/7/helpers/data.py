# =======================================================================================================
### ======= ###
### IMPORTS ###
### ======= ###


# =======================================================================================================
### ==== ###
### CODE ###
### ==== ###


def load_data(fname: str): 

    # Opening and reading the file. 
    with open(f"ref/{fname}", "r") as file: 
        lines = file.readlines() 

    # Reading the lines and formatting. 
    for i, line in enumerate(lines):
        clean_line = line.replace("\n", "")
        cleaner_line = clean_line.replace("->", "")
        lines[i] = [x for x in cleaner_line.split(" ") if x]
        
    print(lines)