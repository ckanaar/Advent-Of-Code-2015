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
        lines: Processed lines.
    """

    # Opening and reading the file. 
    with open(f"ref/{fname}", "r") as file: 
        lines = file.readlines()
    
    # Remove the , and through from the files. 
    for i in range(len(lines)): 
        cleaner_line       = lines[i].replace("through", "")
        cleanest_line      = cleaner_line.replace("turn", "")
        most_cleanest_line = cleanest_line.replace("\n", "")
        lines[i]           = [x for x in most_cleanest_line.split(" ") if x]
    
    return lines
    