import random

import copy

import collections
from collections import Counter


LETTER_POOL = {
    'A': 9,
    'B': 2,
    'C': 2,
    'D': 4,
    'E': 12,
    'F': 2,
    'G': 3,
    'H': 2,
    'I': 9,
    'J': 1,
    'K': 1,
    'L': 4,
    'M': 2,
    'N': 6,
    'O': 8,
    'P': 2,
    'Q': 1,
    'R': 6,
    'S': 4,
    'T': 6,
    'U': 4,
    'V': 2,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1
}

# =============================== draw_letters ===============================

def draw_letters():
    hand_of_letters = []                             
    
    letter_pool_copy = copy.deepcopy(LETTER_POOL)
    
    while len(hand_of_letters) < 10:                            
        letter_dict_keys = list(LETTER_POOL.keys())
        weight_values_list = list(LETTER_POOL.values())
        random_letter = random.choices(
            letter_dict_keys, 
            weights = weight_values_list, 
            k=1
        )[0]
                
        if letter_pool_copy[random_letter] > 0:
            hand_of_letters.append(random_letter)
            
            letter_pool_copy[random_letter] -= 1
            
    return hand_of_letters



# =============================== uses_available_letters ===============================
    
def uses_available_letters(word, letter_bank):
    
    word = word.upper()                                     # 1                                                
    
    for letter in word:                                     # 2                                                  

        letter_bank_counter = Counter(letter_bank)          # 3
        
        word_counter = Counter(word)                        # 4

        if letter in letter_bank_counter:                   # 5                           
            letter_bank_counter.subtract(word_counter)      # 6                      
            
            if letter_bank_counter[letter] < 0:             # 7
                return False                                # 8
        
        if letter not in letter_bank:                       # 9                                   
            return False                                    # 10                     
        
    return True                                             # 11                                                         


    # 1. capitalize all letters, to bypass text case from user input
    # 2. loop through each letter in the word
    # 3. assigns number value to each letter in the letterbank, 
    #    based on the number of times that letter appears
    # 4. assigns number value to each letter in the word
    #    based on the number of times that letter appears
    # 5. check if the letter that's in the word is also in the letter bank
    # 6. if it is, subtract the value of that letter in the word
    #    from the value of that corresponding letter in the letter bank
    # 7. if the value of the letter in the letter bank is less than 0, 
    #    that means there aren't any of that letter left in the bank
    # 8. return False - this accounts for overusing a valid letter choice
    # 9. if that letter is not in the letter bank, 
    # 10. return False 
    # 11. if the loop makes it to this point- 
    #     every letter in the word is in the letter bank in the correct amount
    #     so this is a valid anagram, and we return True
        


# =============================== score_word ===============================

def score_word(word):                                           # 1 - 2
    score_chart = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]  
}
    
    total_points_scored = 0                                     # 3
    

    for letter in word.upper():                                 # 4
        for dict_key, dict_value in score_chart.items():        # 5
            if letter in dict_value:                            # 6
                total_points_scored += dict_key                 # 7
        
    if len(word) > 6:                                           # 8 
        total_points_scored += 8                                # 9
        
    return total_points_scored                                  # 10
    
    

# 1. function takes in a word as a parameter
#    word, which is a string of characters

# 2. score_chart
#    using a dictionary - the key is immutable
#    you can loop through both the keys and the values
#    and return the key, which is an integer in this case.


# 3   Each letter within word has a point value, that we'll need to sum later,
#     so the variable total_points_scored helps us hold a value
    
# 4   Loop through each of the letters in the word that's provided as an argument
#     for each word, if the user enters a word that's lowercase,
#     using .upper() will capitalize it so it matches the case of the
#     elements that are contained in the score_chart list

# 5   loop through the dictionary's values-- which are a list
#     Loop through both keys and values, by using the items() method:
#     for x, y in thisdict.items():
#        print(x, y)
    
# 6    check if that letter is in the dictionary's value     
    
# 7    and if it is, then add the dictionary's key- which is an integer
#      to the total points scored

# 8    if the length of the word is 7, 8, 9, or 10

# 9    then add 8 additional points
    
# 10   the function returns an integer, representing the number of the total points scored


# =============================== get_highest_word_score ===============================

def get_highest_word_score(word_list):                  # 1
    highest_score =  0                                  # 2
    winning_word_list= []                               # 3
	
    for word in word_list:                              # 4

        word_score = score_word(word)                   # 5

        if word_score > highest_score:                  # 6
            highest_score = word_score                  # 7
            winning_word_list= [word]                   # 8
        
        
        elif word_score == highest_score:               # 9
            winning_word_list.append(word)              # 10

    letter_count = 10                                   # 11
    best_word = ''                                      # 12
    
    if len(winning_word_list) == 1:                     # 13
        return winning_word_list[0], highest_score
    else:                                               # 14
        for word in winning_word_list:

            if len(word) == 10:                         # 15
                return word, highest_score
            else:
                
                if len(word) < letter_count:            # 16
                    letter_count = len(word)
                    best_word = word
    
    return best_word, highest_score                     # 17