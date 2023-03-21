
def draw_letters():
    import random

    RANGE_LOW = 0
    RANGE_HIGH = 25

#     LETTER_POOL = {
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

    list_of_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "k", \
                       "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    hand = []
    while len(hand) < 10:
        random_number = random.randint(RANGE_LOW, RANGE_HIGH)
        letter = list_of_letters[random_number]
        hand.append(letter)
    print(hand)
    return hand




def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass