import random 

LETTER_POOL = [
    ("A", 9),
    ("B", 2),
    ("C", 2),
    ("D", 4),
    ("E", 12),
    ("F", 2),
    ("G", 3),
    ("H", 2),
    ("I", 9),
    ("J", 1),
    ("K", 1),
    ("L", 4),
    ("M", 2),
    ("N", 6),
    ("O", 8),
    ("P", 2),
    ("Q", 1),
    ("R", 6),
    ("S", 4),
    ("T", 6),
    ("U", 4),
    ("V", 2),
    ("W", 2),
    ("X", 1),
    ("Y", 2),
    ("Z", 1)
]

def draw_letters():
    letter_bank = []
    number_of_letter_available = []
    
    for letter in LETTER_POOL:
        number_of_letter_available.append(letter[1])
    
    while len(letter_bank) < 10:    
        random_index = random.randint(0, len(LETTER_POOL) - 1)
        if number_of_letter_available[random_index] > 0:
            letter_bank.append(LETTER_POOL[random_index][0])
            number_of_letter_available[random_index] -= 1
 
    return letter_bank


def uses_available_letters(word, letter_bank):
    cap_word = word.upper()
    letter_bank_quantity = {}
    char_quantity = {}
    result = False

    for letter in letter_bank:
        if letter not in letter_bank_quantity:
            letter_bank_quantity[letter] = 1
        else:
            letter_bank_quantity[letter] += 1
    
    for char in cap_word:
        if char not in char_quantity:
            char_quantity[char] = 1
        else:
            char_quantity[char] += 1
    
    for letter in cap_word:
        if letter not in letter_bank or char_quantity[letter] > letter_bank_quantity[letter]:
            result = False
            break 
        else:
            result = True

    return result  


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass