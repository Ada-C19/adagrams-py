import random

def draw_letters():
    # LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    # "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # letter_bank = random.choices(LETTERS, weights=(9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1), k=10)

    # print(letter_bank)
    # return letter_bank

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

    letter_bank = []
    for i in range(10):
        letter = random.choice(list(LETTER_POOL.keys()))
        letter_bank.append(letter)
        LETTER_POOL[letter] -= 1
        
        if LETTER_POOL[letter] == 0:
            LETTER_POOL.pop(letter)


    print(letter_bank)
    return letter_bank


def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    for letter in word.upper():
        if letter in letter_bank_copy:
            # do A
            letter_bank_copy.remove(letter)
        else:
            # do B
            return False
    # if we got here, for went thru entire word
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass