import random 

def draw_letters():

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
    # create a list that will eventually be filled with 10 different letters
    hand = []
    length_of_hand = 10
    

    # based on the desired length of the hand (in this case, 10), 
    # the loop will simulate a player 'picking' 10 random letters 
    # for their hand
    
    while len(hand) < length_of_hand: 
        # random letter generator (upper case)
        random_letter = chr(random.randint(ord('A'), ord('Z')))

        if LETTER_POOL[random_letter] == 0: 
            continue
        
        else: 
            LETTER_POOL[random_letter] -= 1
            hand.append(random_letter)

    return hand 

def uses_available_letters(word, letter_bank):
    # check each character in the word string is in the letter_bank array
    # (in the right quantities) i.e. if the user's guess contains 3 Y's and t
    # the hand only has 1, then it is not a valid guess
    # use sets to see if one if a subset of the other? 

    word_set = set()
    letter_bank_set = set(letter_bank)
    
    # place each character in the set
    for character in word: 
        word_set.add(character)
    
    return word_set.issubset(letter_bank_set)

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass