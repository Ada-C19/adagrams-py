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
    hand = []
    copy_letter_pool = LETTER_POOL.copy()
    while len(hand) < 10:
        random_letter = random.choices(
            list(copy_letter_pool), weights=copy_letter_pool.values(), k=1)
        str_random_letter = random_letter[0]

        if copy_letter_pool[str_random_letter] > 0:
            hand.append(str_random_letter)
            copy_letter_pool[str_random_letter] -= 1
    return hand


def uses_available_letters(word, letter_bank):
    word_upper = word.upper()
    for letter in word_upper:
        if word_upper.count(letter) != letter_bank.count(letter):
            return False
    return True


def score_word(word):
    score = 0
    score_chart = {
        "A": 1,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 4,
        "G": 2,
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5,
        "L": 1,
        "M": 3,
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10,
    }

    for letter in word.upper():
        if letter in score_chart:
            score += score_chart[letter]
    if len(word) >= 7:
        score += 8
    return score


def get_highest_word_score(word_list):
    highest_score = 0
    winner = None

    for word in word_list:
        word_score = score_word(word)
        if word_score > highest_score:
            highest_score = word_score
            winner = (word, word_score)
        elif word_score == highest_score:
            if len(word) == 10:
                return (word, word_score)
            elif len(word) < len(winner[0]):
                winner = (word, word_score)
    return winner
