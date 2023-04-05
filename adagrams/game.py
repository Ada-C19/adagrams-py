from random import sample

LETTER_POOL = {
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
ONLY_LETTERS = list(LETTER_POOL.keys())
ONLY_WEIGHTS = list(LETTER_POOL.values())
LETTER_VALUE = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"],
}

# helper function:
def build_letter_to_score(input_dict):
    '''return a dictionary with each letter matched with it's score.'''
    letter_to_score = {}
    for score, letters in input_dict.items():
        for letter in letters:
            letter_to_score[letter] = score
    return letter_to_score
  

def draw_letters():
    '''return a list of ten letters from an alphabet pool.'''
    # uses random.sample which takes the list ONLY_LETTERS,
    # and returns a list of 10 (k=10) elements in that list, weighted by ONLY_WEIGHTS.
    ten_letters = sample(ONLY_LETTERS, counts = ONLY_WEIGHTS, k=10)
    return ten_letters


def uses_available_letters(word, letter_bank):
    '''verify the input word uses only letters in the player's hand.'''
    letter_bank_count = {}
    for letter in letter_bank:
        if letter not in  letter_bank_count:
            letter_bank_count[letter] = 1
        else:
            letter_bank_count[letter] += 1
    for letter in word.upper():
        if letter in letter_bank and letter_bank_count[letter] > 0:
            letter_bank_count[letter] -= 1
        else:
            return False
    return True


def score_word(word):
    '''return the total score of a word by adding the value of each letter'''
    letter_to_score = build_letter_to_score(LETTER_VALUE)
    total_score = 0
    for letter in word.upper():
        total_score += letter_to_score[letter]
    if len(word) > 6:
        total_score += 8
    return total_score
# n for time complexity: n is chars in word - letter_values is constant, not a variable, that loop doesn't count

def get_highest_word_score(word_list):
    '''Given a list of words, return the highest scoring word'''
    words_and_scores = { word: score_word(word) for word in word_list }
    highest_score = max(words_and_scores.values())
    words_with_high_score = [
        word for word, score in words_and_scores.items() if score == highest_score
    ]
    for word in words_with_high_score:
        if len(word) == 10:
            return word, highest_score
    return min((words_with_high_score), key=len), highest_score

# 3n * m => n * m for time complexity.