
# import random
import random

import copy 
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
letter_list = []
for letter in LETTER_POOL.keys():
    letter_list += LETTER_POOL[letter] * letter
# print(letter_list)

def draw_letters():
    selected_letters = []
    while len(selected_letters) < 10:
        random_index = random.randint(0,  len(letter_list)-1)
        chosen_letter = letter_list[random_index]
        if selected_letters.count(chosen_letter) < LETTER_POOL[chosen_letter]:
            selected_letters += chosen_letter
            # print(selected_letters)
            
        else:
            continue
    print(selected_letters)
    return selected_letters
      
      


def uses_available_letters(word, letter_bank):
    # letter_bank = str(input("please input an anagram "))
    # while type(word) == str:    
    list_copy = copy.deepcopy(letter_bank)

    for character in word.upper(): 
        if character in list_copy:
            list_copy.remove(character) 
        else: 
            return False
    

    return True
        
        
def score_word(word):
    word_score = 0 
    scores = {"A" : 1, "E": 1, "I": 1, "O": 1, "U": 1 ,"L": 1, "N": 1, "R": 1, "S": 1, "T": 1, "D": 2, "G": 2,"B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,"K": 5, "J": 8, "X":8 ,"Q": 10, "Z": 10}

    for letter in word.upper():
        word_score += scores[letter]
    if len(word) >= 7:
        word_score += 8

    return word_score
   




def get_highest_word_score(word_list):
    winning_word = ''
   
    highest_score = 0 
    for word in word_list: 
        word_score = score_word(word)  
        if word_score > highest_score:  # if word_score is greater than the highest score
            
           highest_score = word_score 
           winning_word = word # winning words now contains the winning word
        elif word_score == highest_score: # and if word_score is equal to the highest word
            if len(winning_word) == 10:
                pass
            elif len(word) < len(winning_word) and len(winning_word) != 10: # nested conditional, if the length of the word is greater than the chosen word 
                winning_word = word 
            elif len(word) == 10 and len(winning_word) != 10:
                winning_word = word 
        
            
      
    return winning_word, highest_score
    