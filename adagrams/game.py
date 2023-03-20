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

    aux_letter_pool = LETTER_POOL.copy()
    
    available_letters_list = []

    while len(available_letters_list) < 10:
        numbers = (random.randint(65,90))
        letters_for_user = chr(numbers)

        if aux_letter_pool[letters_for_user] > 1:
            available_letters_list.append(letters_for_user) 
            aux_letter_pool[letters_for_user] -= 1

    return available_letters_list



def uses_available_letters(word, letter_bank):
    
    if len(letter_bank) < len(word):
        return False
    aux_letter_bank = letter_bank.copy()
    for letter in word:
        if letter in aux_letter_bank:
            aux_letter_bank.remove(letter)
        else:
            return False
            
    return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass


word = "pasa"
letter_bank = ["c","a","s", "a", "s"]
#print(draw_letters())
print(uses_available_letters(word, letter_bank))