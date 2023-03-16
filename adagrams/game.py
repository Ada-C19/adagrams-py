import random as r

def make_letter_list():
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
    pass

def get_highest_word_score(word_list):
    pass