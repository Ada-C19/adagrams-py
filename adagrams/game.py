# Now you need a function returns the score of a given word as defined by the Adagrams game.

# Implement the function score_word in game.py. This method should have the following properties:

# Has one parameter: word, which is a string of characters
# Returns an integer representing the number of points
# Each letter within word has a point value. The number of points of each letter is summed up to represent the total score of word
# Each letter's point value is described in the table below
# If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points

import random



def draw_letters():
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
    hand = []
    full_letter_list = []
    for alpha, number in LETTER_POOL.items():
        for i in range(number):
            full_letter_list.append(alpha)
    while len(hand) != 10:
        letter = random.choice(full_letter_list)
        if hand.count(letter) < LETTER_POOL[letter]:
            hand.append(letter)    
    return hand


def uses_available_letters(word, letter_bank):
    word = word.upper()
    for letter in word:
        if letter in letter_bank:
            if word.count(letter) <=  letter_bank.count(letter):
                continue
            else:
                return False
        else:
            return False
    return True

def score_word(word):
    points_total = 0
    SCORE_CHART_DICT ={
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"],
    }
    word = word.upper()

    if len(word) >= 7:
        points_total += 8
    for letter in word:
        for point_key, alpha_list in SCORE_CHART_DICT.items():
            for alpha in alpha_list:
                if alpha == letter:
                    points_total += point_key

    return points_total

def get_highest_word_score(word_list):
    pass

# print statements
# print(draw_letters())
# print(random.choice(LETTER_POOL.keys()))