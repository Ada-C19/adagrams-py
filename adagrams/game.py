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
    SCORE_CHART = {
        "AEIOULNRST": 1,
        "DG": 2,
        "BCMP": 3,
        "FHVWY": 4,
        "K": 5,
        "JX": 8,
        "QZ": 10
    }
    score = 0

    for key, value in SCORE_CHART.items():
        for letter in word.upper():
            if letter in key:
                score += value
    if 7 <= len(word) <= 10:
        score += 8
    return score


def get_highest_word_score(word_list):
    best_word = ""
    highest_score = 0

    for i in range(0, len(word_list)):
        current_word_score = score_word(word_list[i])
        if current_word_score > highest_score:
            best_word = word_list[i]
            highest_score = current_word_score

        elif current_word_score == highest_score:
            if (len(word_list[i]) == 10) and (len(best_word) == 10):
                best_word = best_word
                highest_score = highest_score
            elif (len(word_list[i]) == 10) and (len(best_word) != 10):
                best_word = word_list[i]
                highest_score = current_word_score
            elif (len(word_list[i]) != 10) and (len(best_word) == 10):
                best_word = best_word
                highest_score = highest_score
            elif len(word_list[i]) > len(best_word):
                best_word = best_word
                highest_score = highest_score
            elif len(word_list[i]) < len(best_word):
                best_word = word_list[i]
                highest_score = current_word_score

    return best_word, highest_score
