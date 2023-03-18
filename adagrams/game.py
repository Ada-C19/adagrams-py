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

player_one = []

def draw_letters():

    x = list(LETTER_POOL)

    re_ordered_list = random.sample(x, len(x))
    this_fool = re_ordered_list[:10]
    return this_fool
    # while len(player_one) < 10:
    #     letter = random.choice(list(LETTER_POOL))
    #     if letter in player_one and player_one.count(letter) >= LETTER_POOL.get(letter):
    #         continue
    #     else:
    #         player_one.append(letter)
    # return player_one


#     return game_letters
#     pass

# def uses_available_letters(word, letter_bank):
#     pass

# def score_word(word):
#     pass

# def get_highest_word_score(word_list):
#     pass