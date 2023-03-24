import random

def draw_letters():
    letter_pool = {
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

    letter_poolCopy = letter_pool.copy()
    hand = []
    while len(hand) < 10:
        letter = random.choice(list(letter_poolCopy.keys()))
        if letter.isalpha() and letter_poolCopy[letter] > 0:
            hand.append(letter)
            letter_poolCopy[letter] -=1
    return hand


def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    for letter in word.upper():
        if letter not in letter_bank_copy:
            return False
        letter_bank_copy.remove(letter)
    if len(letter_bank_copy) >= len(word):
        return True
    else:
        return False

def score_word(word):
    letter_score = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1,
    'P': 3,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'W': 4,
    'X': 8,
    'Y': 4,
    'Z': 10
    }

    score = 0
    word = word.upper()
    for letter in word:
        score += letter_score[letter]
    if len(word) >= 7 and len(word) <= 10:
        return score + 8
    return score


def get_highest_word_score(word_list):
    words_and_scores = {}
    highest_score_words = []
    for word in word_list:
        words_and_scores[word] = score_word(word)
    highest_score = max(words_and_scores.values())
    for word, score in words_and_scores.items():
        if score == highest_score:
            highest_score_words.append(word)
    highest_score_words.sort(key=lambda x: (len(x) != 10, len(x), x))
    return (highest_score_words[0], highest_score)