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
    available_letters = []
    ten_random_letters = []

    # I am iterating through each letter and number in the dictionary so that I can
    # get a list (available_letters) showing all available letters. 
    for letter, number in LETTER_POOL.items():
        available_letters.append(letter)
    print(available_letters)

    while len(ten_random_letters) < 10:
        one_random_letter = random.choice(available_letters)
        ten_random_letters.append(one_random_letter)
        available_letters.remove(one_random_letter)
    return ten_random_letters


    #  create a list with letters available
    # from that list get random letters til you have 10

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass