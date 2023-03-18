import random


def draw_letters():
    
    letters = {
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
# this variable holds all the letters to draw
    letter_box = []

 # loop through the dict
    for letter, number in letters.items():
        #loop and check if the letter actually matches the frequency being added 
        for i in range(number):
            letter_box.append(letter)

        #this holds the 10 letters -- 
    letter_list = []

## looping through letters using random.choice and appends to the letter_list
    for letters in range(10):
        letter = random.choice(letter_box)
        letter_list.append(letter)
    # remove will prevent from creating duplicates to be added
        letter_box.remove(letter)
    return letter_list

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass