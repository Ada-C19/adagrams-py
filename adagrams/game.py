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
    letter_list = []

    while len(letter_list) != 10:
        # letter, quantity = random.choice(list(LETTER_POOL.items()))
        letter = random.choice(list(LETTER_POOL.keys()))
        if LETTER_POOL[letter] > 0:
            letter_list.append(letter)
            LETTER_POOL[letter] -= 1

    return letter_list


def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    for letter in word.upper():
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True


def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass
