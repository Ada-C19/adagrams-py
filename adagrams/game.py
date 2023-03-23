import random 
import string
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

def draw_letters():
    
    letters_list = []

    for char, frequency in LETTER_POOL.items():
        letters_list.extend([char] * frequency)


    hand = []
    for i in range(10):
        randomLetter = random.choice(letters_list)
        hand.append(randomLetter)
        letters_list.remove(randomLetter)
    

    #*********
    #YET TO SEE IF FREQUENCY IS LESS THAN THE LETTER POOL
    return hand
    

def uses_available_letters(word, letter_bank):
    # the purpose of this function is to check if the letters in the user input
    # are in present in our current hand.

    # access our hand
    list_copy = copy.deepcopy(letter_bank)

    # letters_in_list_flag == True

    for letter in word.upper():
        if letter in list_copy:
            list_copy.remove(letter)
        else:
            return False

    return True



def score_word(word):
    score_chart = {1 : ["A","E", "I", "O", "U", "L", "N", "R", "S", "T" ],
                   2 :["D","G"],
                   3 : ["B", "C", "M", "P" ],
                   4 : ["F", "H", "V", "W", "Y"],
                   5 : ["K"],
                   8 : ["J", "X"],
                   10 : ["Q", "Z"]
                   }
    pass

def get_highest_word_score(word_list):
    pass