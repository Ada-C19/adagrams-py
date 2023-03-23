from random import choice

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
    hand = []
    while len(hand) < 10: 
        alphabet, occurence = choice(list(LETTER_POOL.items()))
        if hand.count(alphabet) < occurence: 
            hand.append(alphabet)
    return hand

def uses_available_letters(word, letter_bank):

    bank_copy = letter_bank.copy()
    word = word.upper()
    for letter in word:
        if letter not in bank_copy:
            return False
        bank_copy.remove(letter)
    return True


def score_word(word):
    score = 0 
    letter_scores = {
        "a":1, "e":1, "i":1 , "o":1, "u":1, "l":1, "n":1, "r":1, "s":1, "t":1,
        "d":2, "g": 2,
        "b":3, "c":3, "m":3, "p":3,
        "f": 4, "h":4, "v":4, "w":4, "y":4,
        "k":5,
        "j":8, "x":8,
        "q":10, "z":10
        }
    for letter in word.lower():
        score += letter_scores.get(letter, 0)
    if len(word) in [7, 8, 9, 10]:  
        score += 8

    return score 

def get_highest_word_score(word_list):
    if not word_list:
        return None
    

    high_score = 0
    winning_word = ""
    
    
    for word in word_list:
        score = score_word(word)
        if score > high_score:
            high_score = score
            winning_word = word

        # Tie 
        elif score == high_score:
            # word with fewest letters wins
            if len(winning_word) == 10: 
                continue 
            elif len(word) == 10: 
                winning_word = word 
                high_score = score
            elif len(word) < len(winning_word):
                winning_word = word 
            
                    
    return (winning_word, high_score)

    
        #  elif score == high_score:
        #     # word with fewest letters wins
        #     if len(word) < len(winning_word) or len(word) == 10:
        #             winning_word = word
        #             max_len = len(word)
        #             break 
        #     # Word with 10 letters wins
        #     elif len(word) == 10:
        #             winning_word = word
        #             max_len = len(word)
        #     #both words same score and length, pick the first
        #     elif len(word) < len(winning_word) or (len(word) == max_len and len(winning_word) != 10):
        #             winning_word = word
        #             max_len = len(word)


        # Word with 10 letters wins
            # elif len(word) < len(winning_word) or (len(word) == 10 and len(winning_word) < 10):
            #         winning_word = word
            #         max_len = len(word)


        # elif len(word) == max_len and len(winning_word) < 10:
            #         winning_word = word
            #         max_len = len(word)
