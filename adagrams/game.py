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
    used_letters = {}
    letters = []
    possible_letters = list(LETTER_POOL.keys())

    while len(letters) <= 9:
        random_int = random.randint(0, 25)
        random_l =  possible_letters[random_int]
        if not used_letters.get(random_l) == LETTER_POOL[random_l]:
            if (not used_letters.get(random_l)):
                used_letters[random_l] = 0 
            used_letters[random_l] += 1
            letters.append(random_l)
        
    return letters



def uses_available_letters(word, letter_bank):
    letter_bank_dict = {}

    for character in word:
        if character in letter_bank and word.count(character) <= letter_bank_dict[character]:
            return True 
        else:
            return False


            # for character in letter_bank:
            #     if character in letter_bank_dict.keys():
            #         letter_bank_dict[character] += 1
            #     else:
            #         letter_bank_dict[character] = 1



def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass