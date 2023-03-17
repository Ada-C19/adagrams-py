import random
#comment to test Git push
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
    letter_pool = []
    hand = []
    # append LETTER_POOL keys into a list
    for key in LETTER_POOL.keys():
        letter_pool.append(key)

    # print(f"letter_pool is {letter_pool}")
    # random.randint() as to append a random index from letter_pool list
    for i in range(10):
        hand.append(letter_pool[random.randint(0, 25)])
    
    return hand
    
draw_letters()

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass