import random

LETTER_BANK = (
    "A", "A", "A", "A", "A", "A", "A", "A", "A",
    "B", "B",
    "C", "C",
    "D", "D",
    "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
    "F", "F",
    "G", "G", "G",
    "H", "H",
    "I", "I", "I", "I", "I", "I", "I", "I", "I",
    "J",
    "K",
    "L", "L", "L", "L",
    "M", "M",
    "N", "N", "N", "N", "N", "N",
    "O", "O", "O", "O", "O", "O", "O", "O",
    "P", "P",
    "Q",
    "R", "R", "R", "R", "R", "R",
    "S", "S", "S", "S",
    "T", "T", "T", "T", "T", "T",
    "U", "U", "U", "U",
    "V", "V",
    "W", "W",
    "X",
    "Y", "Y",
    "Z"
)

LETTER_INFO = {
    'A': {'frequency': 9, 'value': 1},
    'B': {'frequency': 2, 'value': 3},
    'C': {'frequency': 2, 'value': 3}, 
    'D': {'frequency': 4, 'value': 2}, 
    'E': {'frequency': 12, 'value': 1}, 
    'F': {'frequency': 2, 'value': 4}, 
    'G': {'frequency': 3, 'value': 2}, 
    'H': {'frequency': 2, 'value': 4}, 
    'I': {'frequency': 9, 'value': 1}, 
    'J': {'frequency': 1, 'value': 8}, 
    'K': {'frequency': 1, 'value': 5}, 
    'L': {'frequency': 4, 'value': 1}, 
    'M': {'frequency': 2, 'value': 3}, 
    'N': {'frequency': 6, 'value': 1}, 
    'O': {'frequency': 8, 'value': 1}, 
    'P': {'frequency': 2, 'value': 3}, 
    'Q': {'frequency': 1, 'value': 10}, 
    'R': {'frequency': 6, 'value': 1}, 
    'S': {'frequency': 4, 'value': 1}, 
    'T': {'frequency': 6, 'value': 1}, 
    'U': {'frequency': 4, 'value': 1}, 
    'V': {'frequency': 2, 'value': 4}, 
    'W': {'frequency': 2, 'value': 4}, 
    'X': {'frequency': 1, 'value': 8}, 
    'Y': {'frequency': 2, 'value': 4}, 
    'Z': {'frequency': 1, 'value': 10}
}

LENGTH_OF_HAND = 10

def draw_letters():
    hand = []

    while len(hand) < LENGTH_OF_HAND:
        i = random.randint(0, len(LETTER_BANK)-1)
        current_letter = LETTER_BANK[i]

        if current_letter in hand:
            occurences = 0
            for current_letter in hand:
                occurences += 1
            if LETTER_INFO[current_letter]['frequency'] <= occurences:
                continue

        hand.append(current_letter)

    return hand

def uses_available_letters(word, letter_bank):
    letter_bank_copy = []
    word = word.upper()
    for letter in letter_bank:
        letter_bank_copy.append(letter)

    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass