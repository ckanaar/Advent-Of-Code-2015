# =======================================================================================================
### ======= ###
### IMPORTS ###
### ======= ###

# =======================================================================================================
### ==== ###
### CODE ###
### ==== ###

def process_lights(command: str, lights_1: int, lights_2: int, lights: list):

    # Splitting the lights. 
    lights_1_list = [int(i) for i in lights_1.split(",")]
    lights_2_list = [int(i) for i in lights_2.split(",")]

    # Case 1: Turning lights on.
    if command == "on":
        for i in range(lights_1_list[0], lights_2_list[0]+ 1): 
            for j in range(lights_1_list[1], lights_2_list[1] + 1):
                 lights[i][j] = "on"
        
    # Case 2: Turning lights off. 
    elif command == "off":
        for i in range(lights_1_list[0], lights_2_list[0]+ 1): 
            for j in range(lights_1_list[1], lights_2_list[1] + 1):
                 lights[i][j] = "off"

    # Case 3: Toggling lights. 
    else: 
       for i in range(lights_1_list[0], lights_2_list[0]+ 1): 
            for j in range(lights_1_list[1], lights_2_list[1] + 1):
                if lights[i][j] == "on": 
                    lights[i][j] = "off"
                else: 
                    lights[i][j] = "on"

    return lights 

def process_brightness(command: str, lights_1: int, lights_2: int, lights: list):

    # Splitting the lights. 
    lights_1_list = [int(i) for i in lights_1.split(",")]
    lights_2_list = [int(i) for i in lights_2.split(",")] 

    # Case 1: Turning the lights on. 
    if command == "on":
        for i in range(lights_1_list[0], lights_2_list[0]+ 1): 
            for j in range(lights_1_list[1], lights_2_list[1] + 1):
                lights[i][j] += 1

    # Case 2: Turning lights off. 
    elif command == "off":
        for i in range(lights_1_list[0], lights_2_list[0]+ 1): 
            for j in range(lights_1_list[1], lights_2_list[1] + 1):
                if lights[i][j] == 0: 
                    continue
                else:
                    lights[i][j] -= 1

    # Case 1: Turning the lights on. 
    if command == "toggle":
        for i in range(lights_1_list[0], lights_2_list[0]+ 1): 
            for j in range(lights_1_list[1], lights_2_list[1] + 1):
                lights[i][j] += 2

    return lights


    
         
        
