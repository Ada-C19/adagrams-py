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
    big_list = []
    for letter, letter_quantity in LETTER_POOL.items():
        big_dict = letter * letter_quantity
        for single_char in big_dict:
            big_list.append(single_char)

    draw_of_10_letters = []
    while len(draw_of_10_letters) < 10:
        random_letter = random.choice(big_list)
        draw_of_10_letters.append(random_letter)
        big_list.remove(random_letter)
    return draw_of_10_letters

draw_letters()   

def uses_available_letters(word, letter_bank):

        word = word.upper()
        for letter in word:
            word_count = word.count(letter)
            letter_bank_count = letter_bank.count(letter)
            if letter not in letter_bank:
                return False
            if word_count > letter_bank_count:
                return False
        return True

# ******* TEST 3 **********
def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass