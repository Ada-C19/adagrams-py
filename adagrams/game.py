import random

# LETTER_POOL = {
#     'A': 9, 
#     'B': 2, 
#     'C': 2, 
#     'D': 4, 
#     'E': 12, 
#     'F': 2, 
#     'G': 3, 
#     'H': 2, 
#     'I': 9, 
#     'J': 1, 
#     'K': 1, 
#     'L': 4, 
#     'M': 2, 
#     'N': 6, 
#     'O': 8, 
#     'P': 2, 
#     'Q': 1, 
#     'R': 6, 
#     'S': 4, 
#     'T': 6, 
#     'U': 4, 
#     'V': 2, 
#     'W': 2, 
#     'X': 1, 
#     'Y': 2, 
#     'Z': 1
# }

# player_one = []
# pool_conversion = list(LETTER_POOL)

# def draw_letters():

#     re_ordered_list = random.sample(pool_conversion, len(pool_conversion))
#     game_letters = re_ordered_list[:10]
#     return game_letters

# ----------------------------------------------------------------------------


def uses_available_letters(word, letters):
    matches = []
    word = word.upper()
    for letter in word:
        if letter in letters:
            if matches.count(letter) < letters.count(letter):
                matches.append(letter)
            elif matches.count(letter) == letters.count(letter):
                continue
    
    if len(matches) == len(word):
        return True
    else:
        return False

    
# matches = []

# def uses_available_letters(word, letters):
#     word = word.upper()
#     for letter in word:
#         if letter in letters:
#             if matches.count(letter) < letters.count(letter):
#                 matches.append(letter)
#             elif matches.count(letter) == letters.count(letter):
#                 continue
#         else: continue

#     if len(matches) == len(word):
#         return True
#     else:
#         return False


# def score_word(word):
    # pass

# def get_highest_word_score(word_list):
    # pass