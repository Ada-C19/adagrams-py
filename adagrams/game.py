import random

SCORE_DICT = {
    "AEIOULNRST": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10,
}


def draw_letters():
    """Build a hand of 10 letters for the user

    Parameters:
    None

    Returns:
    list: letter_bank
    """

    letter_pool = {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 2,
        "Z": 1,
    }
    letter_bank = []
    freq = 10
    while freq > 0:
        letter = random.choice(list(letter_pool.keys()))
        if letter_pool[letter] != 0:
            letter_bank.append(letter)
            letter_pool[letter] -= 1
            freq -= 1

    return letter_bank


def uses_available_letters(word, letter_bank):
    """Check if an input word (a word a player submits) only uses
    characters that are contained within a collection of drawn letters

    Parameters:
    word, letter_bank

    Returns:
    bool: True or False
    """

    letter_bank_copy = letter_bank[:]
    for letter in word.strip():
        if letter.upper() not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter.upper())

    return True


def score_word(word):
    """Return the score of a given word as defined by Adagrams game

    Parameters:
    word

    Returns:
    int: score
    """

    score = 0
    for letter in word.strip():
        for key in SCORE_DICT:
            if letter.upper() in key:
                score += SCORE_DICT[key]

    if len(word.strip()) in range(7, 11):
        score += 8

    return score


def get_highest_word_score(word_list):
    """This function looks at the list of word_list and calculates
    which of these words has the highest score, applies any tie-breaking logic,
    and returns the winning word in a tuple

    Parameters:
    word_list

    Returns:
    tuple: highest_word, highest_score
    """
    highest_word, highest_score = "", 0

    for word in word_list:
        score = score_word(word.strip())
        if score > highest_score:
            highest_word, highest_score = word.strip(), score
        elif score == highest_score:
            if len(highest_word) == 10:
                continue
            elif len(word.strip()) == 10 or len(word.strip()) < len(highest_word):
                highest_word, highest_score = word.strip(), score

    return highest_word, highest_score
