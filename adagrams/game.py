import random 

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
    # create a list that will eventually be filled with 10 different letters
    hand = []
    length_of_hand = 10
    counter = 0  

    # based on the desired length of the hand (in this case, 10), 
    # the loop will simulate a player 'picking' 10 random letters 
    # for their hand
    
    for draw_letter in range(length_of_hand): 
        # random letter generator
        random_upper_case_letter = chr(random.randint(ord('A'), ord('Z')))

        hand.append(random_upper_case_letter)

    return hand 

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass