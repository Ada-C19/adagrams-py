import random as r

def make_letter_list():
    #Define the frequencies of each letter
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

    #Turn dict into list where each letter appears a number of times
    #equal to its frequency
    letter_list = []
    for letter, count in LETTER_POOL.items():
        for _ in range(count):
            letter_list.append(letter)

    return letter_list


def draw_letters():
    letter_list = make_letter_list()

    hand = []

    for _ in range(10):
        letter_index = r.randint(0, len(letter_list) - 1)
        hand.append(letter_list[letter_index])
        letter_list.pop(letter_index)

    return hand


def uses_available_letters(word, letter_bank):
    #Create dict of hand with letter as key and count as value
    letter_dict = {}
    for letter in letter_bank:
        letter = letter.lower()
        letter_dict[letter] = letter_dict.get(letter, 0) + 1

    #Create dict of word with letter as key and count as value
    word_dict = {}
    for i in range(len(word)):
        letter = word[i].lower()
        word_dict[letter] = word_dict.get(letter, 0) + 1

    #print(letter_dict.keys())

    #Compare to verify word letters are in bank AND there aren't too many
    for letter, count in word_dict.items():
        if letter not in list(letter_dict.keys()):
            return False
        elif count > letter_dict[letter]:
            return False
    return True

def score_word(word):
    #Define score for each letter
    SCORE_DICT = {
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
        "Z": 10
    }

    #Iterate through word and total score for each letter
    score = 0
    for i in range(len(word)):
        letter = word[i].upper()
        score += SCORE_DICT[letter]

    #Add 8 extra points if word is 7-10 letters long
    if len(word) in range(7,11):
        score += 8

    return score

def get_highest_word_score(word_list):
    pass