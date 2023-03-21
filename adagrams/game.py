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
    '''
    This function returns a list of 10 random letters. It represents the 
    hand of letters that a player has drawn. It takes into account 
    the number of letters available for each letter. 
    Input: no parameters
    Output: Returns a list of 10 letters. 
    '''
    
    #creating a copy of LETTER_POOL
    letter_amount_dict = LETTER_POOL.copy()
    letters_list = []


    while len(letters_list) < 10:

        #getting random letter and resepctive number_of_letters,
        #first converted letter_amount_dict to a list ea. element has (key-value pair)
        letter, number_of_letters = random.choice(list(letter_amount_dict.items()))

        if number_of_letters > 0:
            #decrement number_of_letters from our letter_amount_dict
            letter_amount_dict[letter] = number_of_letters -1 
            #append the current letter to our letters_list
            letters_list.append(letter)

    return letters_list

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

draw_letters()
