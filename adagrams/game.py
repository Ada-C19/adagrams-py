import random

def draw_letters():
    letters_list = []
    pool_of_letters_dict = {
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
        "Z": 1

    }
    letter_freq = {}
    #letters_list.append(random.choice(list(pool_of_letters_dict.keys())))
    #return letters_list
  
    while len(letters_list) < 10:
        random_letter = (random.choice(list(pool_of_letters_dict.keys())))
        if random_letter in letter_freq:
            letter_freq[random_letter] += 1
            if letter_freq[random_letter] < pool_of_letters_dict[random_letter]:
                letters_list.append(random_letter)
        else:
            letter_freq[random_letter] = 1
            letters_list.append(random_letter)
    return letters_list

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass