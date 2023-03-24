import random

letter_bank = {
"A" : 9,	
"B" : 2,
"C" : 2,	
"D" : 4,	
"E" : 12,	
"F" : 2,	
"G" : 3,	
"H" : 2,	
"I" : 9,
"J" : 1,	
"K" : 1,	
"L" : 4,
"M" : 2,
"O": 8,
"P": 2,
"Q": 1,
"R": 6,
"S": 4,
"T": 6,
"U": 4,
"V": 2,
"W": 2,
"X": 1,
"Y": 2,
"Z": 1,
}

def draw_letters():
    
    letters = []
    
    for letter, count in letter_bank.items():
       
        letters.extend([letter] * count)
    random.shuffle(letters)
    hand = letters[:10]
    return hand

print(draw_letters())

def uses_available_letters(word, letter_bank):
   
    word = word.upper()
    
    letter_bank_copy = list(letter_bank)#not necessary
    
    for letter in word:
        if letter not in letter_bank_copy:
            return False
        letter_bank_copy.remove(letter)# not nessecary

    return True


def score_word(word): 
    
    score_dict = {
"A" : 1,	
"B" : 3,
"C" : 3,	
"D" : 2,	
"E" : 1,	
"F" : 4,	
"G" : 2,	
"H" : 4,	
"I" : 1,
"J" : 8,	
"K" : 5,	
"L" : 1,
"M" : 3,
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

    total_score = 0
    for letter in word.upper():
        total_score += score_dict.get(letter,0)
        
    if 7 <= len(word) <= 10:
        total_score += 8

    return total_score


def get_highest_word_score(word_list):

    #word_list is a list of strings ['','','']
    highest_score = 0
    best_word = ""
    
    for word in word_list:
        score = score_word(word)
        
        if score > highest_score:
            highest_score = score
            best_word = word
        
        #if tie in scores, follow tie-breaking rules
        elif score == highest_score:
            #if the current word is shorter than winning word, set it as new winning word
            if len(word) < len(best_word):# check here comparing int to word
                best_word = word
            #if the current word has 10 letters, set it as new winning word 7-10 forgot 7
            elif len(word) == 10:
                best_word = word

    #return a tuple of winning word and its score
    return (best_word, highest_score)

