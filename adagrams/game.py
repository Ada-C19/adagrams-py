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
    final_letter_choice = []
    print(letter_pool)
    for number in range(0,10):
        while True:
            chosen_letter = random.choice(list(letter_pool.keys()))
            if(letter_pool[chosen_letter] == 0):
                continue 
            else:
                break
        final_letter_choice.append(chosen_letter)
        letter_pool[chosen_letter] -= 1
    return final_letter_choice


def uses_available_letters(word, letter_bank):
    letter_bank_new = letter_bank.copy()
    for characters in word:
        chosen_character = characters.upper()
        try:
            letter_bank_new.remove(chosen_character)
        except:
            return False
    return True

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
    final_score = 0
    for characters in word:
        final_score += letter_score[characters.upper()]
    if len(word) >= 7:
        final_score += 8
    return final_score

def get_highest_word_score(word_list):
    pass