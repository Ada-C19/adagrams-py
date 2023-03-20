import random
import getpass

HAND_SIZE = 10

DISTRIBUTION_OF_LETTERS = {
    "A": 9, "B": 2,
    "C": 2, "D": 4,
    "E": 12, "F": 2,
    "G": 3, "H": 2,
    "I": 9, "J": 1,
    "K": 1, "L": 4,
    "M": 2, "N": 6,
    "O": 8, "P": 2,
    "Q": 1, "R": 6,
    "S": 4, "T": 6,
    "U": 4, "V": 2,
    "W": 2, "X": 1,
    "Y": 2, "Z": 1
}


def draw_letters():
    hand = []
    letter_list = []
    for x, y in DISTRIBUTION_OF_LETTERS.items():
        letter_list.append(x)

    while len(hand) <= 9:
        letter_choice = random.choice(letter_list)
        letter_count = hand.count(letter_choice)
        if letter_count < DISTRIBUTION_OF_LETTERS[letter_choice]:
            hand.append(letter_choice)
    print(hand)
    return hand


def uses_available_letters(word, letter_bank):
    pass


def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass


draw_letters()