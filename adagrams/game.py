import random
import string

def draw_letters():
    
    letter_pool = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    #Returns an array of 10 random uppercase letters in the appropriate quantities

    letters = random.choices(letter_pool, weights = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1], k = 10)

    return letters
    #---failing 1 test -- how to return subsiquent hands that keeps track of freq of used letters
    
def uses_available_letters(word, letter_bank):
    letter_dict = {}
    word_dict = {}
    #returns either True or False
    #check if letter in submitted word are in letter_bank (some or all letters in hand)
    # returns true if every letter in submitted word is available(in the right numbers) in letter_bank
    #print(letter_bank) 
    
    for item in letter_bank:
        if (item in letter_dict):
            letter_dict[item] += 1
        else:
            letter_dict[item] = 1

    #print(letter_dict)

    for elem in word.upper():
        if (elem in word_dict):
            word_dict[elem] += 1
        else:
            word_dict[elem] = 1
    #print(word_dict)
    
    #returns false if any submitted letters in letter_bank are incorrect

    for key, value in word_dict.items():
        if key not in letter_dict or not value <= letter_dict[key]:
            return False
    return True

def score_word(word):  
    
    # dict that holds the key value pairs of letters and their scores.
    letter_score_dict = {
        "A": 1,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 4,
        "G": 2, 
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5,
        "L": 1,
        "M": 3, 
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10,
    }
    #variable that scores will be added to
    score_total = 0
    # variable to keep track of the length of each word
    word_length = 0
    #for each letter in the word: 
    for char in word.upper():
        score_total += letter_score_dict[char]
        word_length = len(word.upper())

    if word_length >= 7 or word_length <= 10:
        score_total += 8  
    elif word_length == "":
        word_length = 0 
        return score_total
    
def get_highest_word_score(word_list):
    
    word_list = score_word(word)
    best_word = {}
    max_val_word = 0
    #find the highest scoring word in word_list
    for word in word_list:
    #looks at word_list and calc tie breakers
        if len(word) == wo
        
        word_list.sort()
        max_val_word = word_list[-1]
        return max_val_word
    #returns winning word and score after calc in form of tuple
    return best_word[0][1]
    #if there is a tie: the word with fewer letters wins unless one word had exactly 10 letters
    if len(word) in word_list == 10:

