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

    letter_pool = [
        'J', 'K', 'Q', 'X', 'Z', 
        'B', 'C', 'F', 'H', 'M', 'P', 'V', 'W', 'Y',
        'G',
        'D', 'L', 'S', 'U', 
        'N', 'R', 'T', 
        'O', 
        'A', 'I', 
        'E'
    ]

    weight = [
        1, 1, 1, 1, 1, 
        2, 2, 2, 2, 2, 2, 2, 2, 2, 
        3,
        4, 4, 4, 4,
        6, 6, 6,
        8, 
        9, 9, 
        12
    ]

    user_hand = []

    for i in range(10): 
        random_choice = random.choices(letter_pool, weights=weight, k = 1)

        tile = letter_pool.index(random_choice[0])
        weight[tile] -= 1
        if weight[tile] == 0: 
            weight.pop(tile)
            letter_pool.pop(tile)

        user_hand.append(random_choice[0])
        
    return user_hand






def uses_available_letters(word, letter_bank):
    uppercase_word = word.upper()
    for char in uppercase_word: 
        if char not in letter_bank or uppercase_word.count(char) > letter_bank.count(char):
            return False  
    return True 






def score_word(word):
    score_chart = {
        'A': 1, 
        'E': 1, 
        'I': 1, 
        'O': 1, 
        'U': 1, 
        'L': 1, 
        'N': 1, 
        'R': 1, 
        'S': 1, 
        'T': 1,
        'D': 2,
        'G': 2,
        'B': 3,  
        'C': 3, 
        'M': 3, 
        'P': 3,  
        'F': 4,  
        'H': 4, 
        'V': 4, 
        'W': 4, 
        'Y': 4, 
        'K': 5,    
        'J': 8,  
        'X': 8,
        'Q': 10, 
        'Z': 10             
    }

    cap_word = word.upper()
    word_score = 0
    for char in cap_word: 
        if score_chart[char]: 
            word_score += score_chart[char]
        else: 
            continue
    # if length of word is between 6 - 10
    if len(cap_word) >= 7 and len(cap_word) <= 10: 
        word_score += 8

    scores_list = list()
    scores_list.append(word_score)
    return word_score






def get_highest_word_score(word_list):
    high_score = 0
    winning_word = ""
    ties = []
    multiple_tie_words = []

    for word in word_list:
        score = score_word(word)
        multiple_tie_words.append(word)

        if score in ties:
            if len(ties) >= 1: 
                winning_word = max(word_list, key=len)
            if len(ties) >= 2 or len(word) != 10:
                if len(word_list) == 2 and len(winning_word) == 10:
                    winning_word = max(word_list, key=len)
                else: 
                    winning_word = min(word_list, key=len)

        if score > high_score: 
            high_score = score
            winning_word = word

            ties.append(score)

    return winning_word, high_score