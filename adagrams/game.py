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
    tiles = [] #list that's ten letters
    count = 0 #going to stop at 10
    letters_dict = LETTER_POOL.copy()
    while count != 10:
        letter = random.choices(list(letters_dict), weights = letters_dict.values(), k = 10)
        if letters_dict[letter] > 0:
            letters_dict[letter] -= 1
            tiles.append(letter)
            count += 1
        else:
            continue
    return tiles
        

    

        

            





def uses_available_letters(word, letter_bank):
    pass

        


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

draw_letters()