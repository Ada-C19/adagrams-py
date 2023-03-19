import random
import string
import copy
import collections


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
    pass

def get_highest_word_score(word_list):
    pass