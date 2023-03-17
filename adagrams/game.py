import random

LETTER_BANK = ("A", "A", "A", "A", "A", "A", "A", "A", "A",
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
               "Z")

LENGTH_OF_HAND = 10

def draw_letters():
    hand = []

    while len(hand) < LENGTH_OF_HAND:
        i = random.randint(0, len(LETTER_BANK)-1)
        hand.append(LETTER_BANK[i])

    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass