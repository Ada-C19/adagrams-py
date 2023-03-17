# import numpy
import numpy as np
# letter pool copied from test_wave_01
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
    
# Each string should contain exactly one letter
    # Imagine that the user returns their hand to the pool before drawing new letters; array should be within the loop
    arr_of_str = []
    letters = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    probability = []
    for key in LETTER_POOL:
        p = LETTER_POOL[key]
        probability.append(p)
    probs = np.array(probability)
    probs_scaled = probs / probs.sum()
    arr_of_str.append(np.random.choice(letters, 10, p=probs_scaled))

    result = []
    str_arr = arr_of_str[0]
    for char in str_arr:
        result.append(str(char))
    return result

    # for i in range(10):
# The letters should be randomly drawn from a pool of letters: random.
# This letter pool should reflect the distribution of letters as described in the table below
# There are only 2 available C letters, so draw_letters cannot ever return more than 2 Cs
# Since there are 12 Es but only 1 Z, it should be 12 times as likely for the user to draw an E as a Z
# Invoking this function should not change the pool of letters
        # random_letter = LETTER_POOL
        # arr_of_str.append(random_letter)



    # Returns an array of ten strings








    

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass