import random


def draw_letters():
    hand_dict = {}
    LETTER_POOL = { 'A': 9, 'N': 6,
                    'B': 2, 'O': 8,
                    'C': 2, 'P': 2, 
                    'D': 4, 'Q': 1,
                    'E': 12,'R': 6, 
                    'F': 2, 'S': 4,
                    'G': 3, 'T': 6,
                    'H': 2, 'U': 4,
                    'I': 9, 'V': 2,
                    'J': 1, 'W': 2,
                    'K': 1, 'X': 1,
                    'L': 4, 'Y': 2,
                    'M': 2, 'Z': 1
                 }
    hand = []
    hand_dict = {}
    num_letters = 10 
    letters, weights = zip(*LETTER_POOL.items())
    hand = random.choices(letters, weights, k = num_letters)
    valid_hand = False

    while not valid_hand:
        for letter in hand:
            if letter in hand_dict:
                hand_dict[letter] += 1
            else:
                hand_dict[letter] = 1 
  
        for letter in hand_dict.keys():
            if hand_dict[letter] <= LETTER_POOL[letter]:
                valid_hand = True
            else:
                hand = random.choices(letters, weights, k = num_letters)

    return hand

                     
                   
                    
                     
                    
                     
                     
                     
                     
                    
                     
                    
                


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass