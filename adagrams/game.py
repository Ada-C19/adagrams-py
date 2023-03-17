from random import choices

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
ONLY_LETTERS = [letter for letter in LETTER_POOL.keys()]
ONLY_WEIGHTS = [num for num in LETTER_POOL.values()]


def draw_letters():
    ten_letters = ""
    while len(ten_letters) < 10:
        letter = choices(ONLY_LETTERS, ONLY_WEIGHTS, k=1)[0]
        if ten_letters.count(letter) < LETTER_POOL[letter]:
            ten_letters += letter
    return ten_letters

def uses_available_letters(word, letter_bank):
    letter_bank_count = {}
    for letter in letter_bank:
        letter_bank_count[letter] = letter_bank.count(letter)
    for letter in word.upper():
        if letter in letter_bank and letter_bank_count[letter] > 0:
            letter_bank_count[letter] -= 1
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass