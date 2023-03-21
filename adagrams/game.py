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


    letter_pool_copy = letter_pool.copy()
    hand_of_letter = []

    while len(hand_of_letter) < 10:
        letter = random.choice(list(letter_pool_copy.keys()))
        if letter.isalpha() and letter_pool_copy[letter] > 0:
                hand_of_letter.append(letter)
                letter_pool_copy[letter] -=1
        else:
            continue
    return hand_of_letter





def uses_available_letters(word, letter_bank):

    word = word.upper()
    letter_dict = {}
    for letter in letter_bank:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    
    for letter in word:
        if letter not in letter_dict:
            return False
        elif letter_dict[letter] == 0:
            return False
        else:
            letter_dict[letter] -= 1
    
    return True


    # for letters in list_word:
    #     for letters in letter_bank:
    #         if letters in letter_bank:
    #             letter_bank.remove(letters)
    #         return True
    # else:
    #     return False
 


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass