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
    
    letter_bank_copy = list(letter_bank)
    
    for letter in word:
        if letter not in letter_bank_copy:
            return False
        letter_bank_copy.remove(letter)

    return True


def score_word(word):

    score_dict = {

    ("A","E","I","O","U","L","N","R","S","T"): 1,
    ("D","G"): 2,
    ("B","C","M","P"):3,
    ("F","H","V","W","Y"): 4,
    ("K"):5,
    ("J","X"): 8,
    ("Q","Z"): 10,
}
    total_score = 0
    for letter in word.upper():
      
        for key in score_dict:
            if letter in key:
                total_score += score_dict[key]
                break
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
            if len(word) < best_word:
                best_word = word
            #if the current word has 10 letters, set it as new winning word
            elif len(word) == 10:
                best_word = word

    #return a tuple of winning word and its score
    return (best_word, highest_score)

