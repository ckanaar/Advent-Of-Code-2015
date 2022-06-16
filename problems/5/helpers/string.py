# =======================================================================================================
### ======= ###
### IMPORTS ###
### ======= ###


# =======================================================================================================
### ==== ###
### CODE ###
### ==== ###


def check_naughty(string: str): 

    # Step 1: Check for at least three vowels. 
    vowels = False
    vowel_count = 0 
    for idx in range(len(string)): 
        if string[idx] in "aeiou": 
            vowel_count += 1 
    if vowel_count >= 3: 
        vowels = True

    # Step 2: Check for double characters. 
    double_char = False
    for idx in range(len(string) - 1):
        if string[idx] == string[idx + 1]:
            double_char = True
    
    # Step 3: Check whether the string does not contain ab, cd, pq, or xy. 
    forbidden = True
    if "ab" in string or "cd" in string or "pq" in string or "xy" in string: 
        forbidden = False

    if vowels == True and double_char == True and forbidden == True: 
        return True
    else: 
        return False 

def check_naughty_2(string: str): 

    # Step 1: Check wether a pair of two letters appears at least twice in the string without overlapping. 
    match = False 
    for i in range(len(string) - 1): 
        pair = string[i : i + 2]
        for j in range(len(string) - 1):
            if j + 1 >= i and j - 1 <= i + 1: 
                continue 
            else: 
                match_pair = string[j : j + 2]
                if pair == match_pair: 
                    match = True 
    
    # Step 2: Check whether the string contains at least one letter which repeats with exactly one letter between them. 
    repeat = False 
    for i in range(len(string) - 2):
        triplet = string[i : i + 3]
        if triplet[0] == triplet[2] and triplet[1] != triplet[0] and triplet[2] != triplet[1]: 
            repeat = True

    if match == True and repeat == True:
        return True 
    else: 
        return False 


def is_really_nice(s):
    first = False
    for i in range(len(s) - 3):
        sub = s[i: i + 2]
        if sub in s[i + 2:]:
            first = True
            print("{} is really nice and repeats with {}".format(s, sub))
            break
    if not first:
        return False
    second = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            second = True
            break
    return second
    

