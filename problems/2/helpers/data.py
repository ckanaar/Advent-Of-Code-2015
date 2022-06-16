# =======================================================================================================
### ======= ###
### IMPORTS ###
### ======= ###

# =======================================================================================================
### ==== ###
### CODE ###
### ==== ###

def load_data(fname: str): 
    """_summary_

    Args:
        fname (str): Name of the file.

    Returns:
        lines: 2D list with dimensions.
    """

    # Opening and reading the file. 
    file  = open(f"ref/{fname}", "r")
    lines = file.readlines()
    file.close()

    # Getting the dimensions in a 2D list. 
    for idx, dimension in enumerate(lines):
        dimension_clean = dimension.replace("\n", "")
        lines[idx] = dimension_clean.split("x")
        
        for i in range(len(lines[idx])): 
            lines[idx][i] = int(lines[idx][i])
        
    return lines



