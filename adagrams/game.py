import random

def draw_letters():
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
    available_letters =[]
    for letter, number in LETTER_POOL.items():
        letter_quantity = letter * number
        available_letters.append(letter_quantity)


    letter_string = ''.join(available_letters)
    list_letter_pool = list(letter_string)
    
    hand = []

    while len(hand) != 10:
        random_letter = random.choice(list_letter_pool)
        hand.append(random_letter)
        for letter in list_letter_pool:
            if letter in hand:
                list_letter_pool.remove(letter)
    return hand

    
cl
def uses_available_letters(word, hand):


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass