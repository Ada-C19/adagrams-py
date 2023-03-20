import random
import string

value_of_letters = {
        
        "A" : 1 , "B" : 3 , "C": 3 , 
        "D" : 2 , "E": 1 , "F": 4 ,
        "G" : 2 , "H" : 4, "I" : 1, 
        "J" : 8 , "K" : 5 ,"L" : 1 , 
        "M" : 3 , "N" : 1 , "O" : 1 , 
        "P": 3, "Q" : 10 , "R" : 1 ,
        "S" : 1 , "T" : 1 , "Q" : 10 ,
        "U" : 1 , "V" : 4 , "W" : 4 , 
        "X" : 8 , "Y" : 4 , "Z" : 10
        
        }
    

def draw_letters():
    
    pool_of_letters = {
    
    
    "A" : 9, "N" : 6, "B" : 2, "O" : 8, "C" : 2, "P" : 2, "D" : 4, "Q" : 1, 
    "E" : 12,"R" : 6, "F" : 2, "S" : 4, "G" : 3, "T" : 6, "H" : 2, "U" : 4,
    "I" : 9, "V" : 2, "J" : 1, "W" : 2, "K" : 1, "X" : 1, "L" : 4, "Y" : 2, 
    "M" : 2, "Z" : 1 
    
    }
    
    
    
    player_letters = []
    random_letter = ""
    
    while len(player_letters) < 10:
        random_letter = random.choice(string.ascii_uppercase)
        if pool_of_letters[random_letter] > 0:
            pool_of_letters[random_letter] -= 1
            player_letters .append(random_letter)
        
    return player_letters 
        

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter = letter_bank[0]
    for letter in word:
        if letter not in letter_bank:
            return False
        if word.count(letter) != letter_bank.count(letter):
            return False
    return True    
        
            
def score_word(word):
    word = word.upper()
    score = 0
    for letter in word:
        score += value_of_letters[letter]
    if len(word) >= 7:
        score += 8     
    return score

def get_highest_word_score(word_list):
    
    winner_word = None
    winner_score = 0
    for word in word_list:
        score = score_word(word)
        if score > winner_score:
            winner_word = word
            winner_score = score
        elif score == winner_score and len(word) == len(winner_word):   
            continue
        elif score == winner_score:
            if len(word) < len(winner_word) and len(winner_word) !=10:
                winner_word = word
            elif len(word)==10:
                winner_word = word
    return (winner_word, winner_score)        
        