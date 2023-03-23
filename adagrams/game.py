import random

#in letter out qty
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
    #each letter in the list appears as many times as its value 
    letters = []
    #count/value - how many the letter should appear
    #letter/key
    for letter, count in letter_bank.items():
        #adds to end by amount of value
        letters.extend([letter] * count)
    random.shuffle(letters)
    hand = letters[:10]
    return hand

print(draw_letters())

def uses_available_letters(word, letter_bank):
   
    word = word.upper()
    #create a copy of the letter bank so that we can modify it
    letter_bank_copy = list(letter_bank)
    #loop over each letter in the word
    for letter in word:
        #if the letter is not in letter bank, return False
        if letter not in letter_bank_copy:
            return False
        #if the letter is in letter bank, remove it from copy
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

    #initialize info
    high_score = 0
    winning_word = ""

    for word in word_list:
        # score = the word, score
        if score > high_score:
            #high score and winning word something here
            elif:
                #coniditons for 10 letters

    #return [winning word, score]
    """

    return a tuple with data or winning word and score
    * The tuple must contain the following elements:
    * index 0 ([0]): a string of a word
    * index 1 ([1]): the score of that word

    incase of tie
    prefer word with fewest letters
    unless word is 10 letters long
    if multiple score on same list are same, pick first
    
    """
    pass
