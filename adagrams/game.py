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


def draw_letters():
    hand_of_letters = []                             # 1
    
    # syntax: new_list = copy.deepcopy(old_list)
    letter_pool_copy = copy.deepcopy(LETTER_POOL)
    
    while len(hand_of_letters) < 10:                            # 3, # 4- 5, # P2 - 5
        letter_dict_keys = list(LETTER_POOL.keys())
        weight_values_list = list(LETTER_POOL.values())
        random_letter = random.choices(letter_dict_keys, weights = weight_values_list, k=1)[0]
                
        if letter_pool_copy[random_letter] > 0:
            hand_of_letters.append(random_letter)
            
            letter_pool_copy[random_letter] -= 1
            
    return hand_of_letters

        
    # 1. capitalize all letters, to bypass text case from user input
    # 2. assigns number value to each letter in the letterbank
    # 3. assigns number value to each letter in the word
    # 4. loop through each letter in the word that the user provides 
    # 5. if the letter is in the word, subtract value of letter in the word from the letter in the letter_bank
    # 6  if letter from the word is NOT in letter_bank, return False
    # 7. if the value of the letter is less than 0 return False
    # 8. if the letter from that word is in the letter bank, return True
    
    # look into count method, while using a string.

    
def uses_available_letters(word, letter_bank):
    
    word = word.upper()                                                
    
    for letter in word:                                                  

        letter_bank_counter = Counter(letter_bank)
        
        word_counter = Counter(word)

        if letter in letter_bank_counter:                           
            letter_bank_counter.subtract(word_counter)                      
            
            if letter_bank_counter[letter] < 0:
                return False
        
        if  letter not in letter_bank:                                   
            return False                     
        
    return True                                                         
        



def score_word(word):                                           # 1
    
    score_chart = {                                             # 2
    1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"], 
    5: ["K"], 
    8: ["J", "X"], 
    10: ["Q" "Z"]   
}
    
    total_points_scored = 0                                     # 3
    

    for letter in word.upper():                                 # 4
        for dict_key, dict_value in score_chart.items():        # 5
            if letter in dict_value:                            # 6
                total_points_scored += dict_key                 # 7
        
    if len(word) > 6:                                           # 8 
        total_points_scored += 8
        
    return total_points_scored
    


def get_highest_word_score(word_list):
    pass
