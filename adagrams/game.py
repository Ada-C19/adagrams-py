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

def draw_letters():
    alphabet = list(LETTER_POOL.keys())
    drawn_letters = []

    while True:
        # Ensure return list does not have more than 10 elems
        if len(drawn_letters) == 10:
            break

        random_letter = alphabet[random.randint(0, len(alphabet)-1)]
        quantity = LETTER_POOL[random_letter]
        counter = 0
        
        # Letter should not be in return list more than its quantity in the pool
        for i in range(len(drawn_letters)):
            if drawn_letters[i] == random_letter:
                counter += 1
        if counter < quantity:
            drawn_letters.append(random_letter)

    return drawn_letters


def uses_available_letters(word, letter_bank):
    available_letters = copy.deepcopy(letter_bank)
    word = word.upper()

    for letter in word:
        if letter in available_letters:
            available_letters.remove(letter)
        else:
            return False  
    return True


def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass