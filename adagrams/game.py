import random

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
    letter_bank = []
    letter_list = []
    for letter, limit in DISTRIBUTION_OF_LETTERS.items():
        letter_list.append(letter)

    while len(letter_bank) <= 9:
        letter_choice = random.choice(letter_list)
        letter_count = letter_bank.count(letter_choice)
        if letter_count < DISTRIBUTION_OF_LETTERS[letter_choice]:
            letter_bank.append(letter_choice)
    print(letter_bank)
    return letter_bank


def uses_available_letters(word, letter_bank):
    word = word.upper()
    for letter in word:
        # print(letter)
        # print(word)
        letter = letter.upper()
        frequency_in_word = word.count(letter)
        frequency_in_bank = letter_bank.count(letter)
        if frequency_in_bank < frequency_in_word:
            return False
    return True
            



def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass


# draw_letters()
# uses_available_letters()