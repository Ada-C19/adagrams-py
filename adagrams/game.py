
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
    # word_score = 0
    scores = {"A" : 1, "E": 1, "I": 1, "O": 1, "U": 1 ,"L": 1, "N": 1, "R": 1, "S": 1, "T": 1, "D": 2, "G": 2,"B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,"K": 5, "J": 8, "X":8 ,"Q": 10, "Z": 10}

    for letter in word.upper():
        word_score += scores[letter]
    if len(word) >= 7:
        word_score += 8

    return word_score
   
#     word_score = 0
#     extra_points = 8
#    # if able to refactor try a nested list. 
#     value_1_list = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
#     value_2_list = ["D", "G"]
#     value_3_list = ["B", "C", "M", "P"]
#     value_4_list = ["F", "H", "V", "W", "Y"]
#     value_5_list = ["K"]
#     value_8_list = ["J", "X"]
#     value_10_list = ["Q", "Z"]


# # score = 0
# score = 0
# for letter in word:
    
# dict
# for letter in word 
# score += scores["letter"]
    
#     while len(word) < 7:
#         for character in word.upper():
#             if character in value_1_list:
#                 word_score += 1
#             elif character in value_2_list:
#                 word_score += 2
#             elif character in value_3_list:
#                 word_score += 3
#             elif character in value_4_list:
#                 word_score += 4
#             elif character in value_5_list:
#                 word_score += 5
#             elif character in value_8_list: 
#                 word_score += 8
#             elif character in value_10_list:
#                 word_score += 10
#         return word_score
#     else:
#         for character in word.upper():
#             if character in value_1_list:
#                 extra_points += 1
#             elif character in value_2_list:
#                 extra_points += 2
#             elif character in value_3_list:
#                 extra_points += 3
#             elif character in value_4_list:
#                 extra_points += 4
#             elif character in value_5_list:
#                 extra_points += 5
#             elif character in value_8_list: 
#                 extra_points += 8
#             elif character in value_10_list:
#                 extra_points += 10
#         return extra_points
            





def get_highest_word_score(word_list):
    winning_word = ''
    # winning_words = [] # setting empty list to put winning words 
    # setting a chosen word variable to an empty string 
    highest_score = 0 # setting a counter called highest_score to 0
    # word_string = '' # setting a word_string variable converter to an empty string
    for word in word_list: # iterating over the word list 
        # word_string = ''
        word_score = score_word(word)  #calling the score word function and setting it to word_score
        
        if word_score > highest_score:  # if word_score is greater than the highest score
            
           highest_score = word_score # the highest score now takes that score
           winning_word = word # winning words now contains the winning word
        elif word_score == highest_score: # and if word_score is equal to the highest word
            if len(winning_word) == 10:
                pass
            elif len(word) < len(winning_word) and len(winning_word) != 10: # nested conditional, if the length of the word is greater than the chosen word 
                winning_word = word # chosen word is now the word
                    # winning_words.remove(chosen_word) 
            elif len(word) == 10 and len(winning_word) != 10:
                winning_word = word 
        
            
            # winning_words.append(word) # it adds that word to the list,(how we get ties)
        
    
        
            # iterating over every word in winning_word list                # word_string = winning_words[0]
                 # the word is now removed from the list, aka the smallest word wins. 
                
                # elif len(word) > len(chosen_word): # nested conditional, if the length of the word is greater than the chosen word 
                #     chosen_word = word # chosen word is now the word
                #     winning_words.remove(chosen_word)
                #         # print(winning_words) 
    return winning_word, highest_score
    
#     return word_string, highest_score

# def get_highest_word_score(word_list):
  
#     winning_words = [] 
#     chosen_word = ''
#     highest_score = 0 
#     word_string = ''
#     for word in word_list: 
#         # word_string = ''
#         word_score = score_word(word) 
        
#         if word_score > highest_score: 
            
#            highest_score = word_score 
#            winning_words = [word] # winning words now contains the winning word
#         elif word_score == highest_score:
#             winning_words.append(word)
#         for word in winning_words:
#             word_string = winning_words[0]
#             if len(winning_words) > 1:
#                 # word_string = winning_words[0]
#                 if len(word) > len(chosen_word):
#                     chosen_word = word
#                     winning_words.remove(chosen_word)
#                     # word_string = winning_words
#                     # print(winning_words)
#                 elif len(word) < 10:
#                     winning_words.remove(word)
#             # elif len(word )

                


    
    return word_string, highest_score
# print(get_highest_word_score(["MMMM", "WWW", "BBBBBB", "AAAAAAAAAA"]))
        

    
    
# for word in winning_words:
#             word_string = word
#             if len(winning_words) > 1:
#                 if len(word) > len(chosen_word):
#                     chosen_word = word
#                     winning_words.remove(chosen_word)
#                 #     print(winning_words)
#                 # if len(word) == 10:
#                 #     winning_words.append(word)
#                 # if len(word) < 10:
#                 #     winning_words.append(word)