import random


def draw_letters():                                                                       
    letter_pool_dict = {
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
    pool_list = []
    player_hand = []
#this is where my code accounts for probability, right? (line 36,37)
    for letter, count in letter_pool_dict.items():
        pool_list += [letter] * count

    while len(player_hand) < 10:  
        letter = random.choice(pool_list) 
        player_hand += letter
        pool_list.remove(letter)
    return player_hand    


def uses_available_letters(word, letter_bank):
    copy = letter_bank[:]
    word = word.upper()
    player_word = []
    for letter in word:
        if letter in copy:
            copy.remove(letter)
            player_word.append(letter)
        else:
            return False
    return True
                    

def score_word(word):
    letter_values = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}   
    
    word = word.upper()
    score = 0
    for letter in word:
        points = letter_values[letter]
        score += points

    if len(word) >= 7:
        score += 8
    return score
# look at this crazy dictionary i tried to make with lists of strings to numbered keys!                                                          
#  int_letters = {
#     1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
#     2: ['D', 'G'],
#     3: ['B', 'C', 'M', 'P'],
#     4: ['F', 'H', 'V', 'W', 'Y'],
#     5: ['K'],
#     8: ['J', 'X'],
#     10: ['Q', 'Z']
# }    


def get_highest_word_score(word_list):  
    winning_word = None
    winning_score = 0
    score_list = [] 
    final_word_list = []
    for word in word_list:
        scores = score_word(word)
        score_list.append(scores) 
        final_word_list.append(word)


    # for i in score_list:    
    winning_score = max(score_list)
        # final_word_list[i] = max(score_list[i]) 
        # winning_word = final_word_list[i]

    
    return (winning_word, winning_score)
                                        
# still get highest score even if the list is unsorted ( so not by index?)                               
# if two words have the same score, game prioritizes shorter word                                        
# EXCEPT if the word is ten letters long                                                                 
# multi way ties pick shortest words    
