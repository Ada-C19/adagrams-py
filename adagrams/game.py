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

    for letter, count in letter_pool_dict.items():
        pool_list += [letter] * count

    while len(player_hand) < 10:  
        letter = random.choice(pool_list) 
        player_hand += letter
        pool_list.remove(letter)
    return player_hand    
# i dont think my function is accounting for probability
#refactor if time , research .choices
                                                                            
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
    pass                                                                            
#score word                                                                         
# caps or lower case is fine                                                                             
# ignore 0                                                                                               
# bonus points for words >= 7                                                                                  


def get_highest_word_score(word_list):                                              
    pass                                                                            
#identify which word got the highest score and what the score was                                        
# still get highest score even if the list is unsorted ( so not by index?)                               
# if two words have the same score, game prioritizes shorter word                                        
# EXCEPT if the word is ten letters long                                                                 
# multi way ties pick shortest words    
# 

                                                           