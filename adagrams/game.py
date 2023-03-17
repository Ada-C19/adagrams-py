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
#make list to return for "hand"
#draw 10 random letters from pool
#reflect letter distribution in dict
    hand = []
    for letter, quantity in LETTER_POOL.items():
        for num in range(quantity):
            hand.append(letter)
            random.shuffle(hand)
    return hand[:10]

def uses_available_letters(word, letter_bank):
    check_letters = {}
    word1 = word.upper()

    for letter in letter_bank:
        if letter not in check_letters:
            check_letters[letter] = 1
        else:
            check_letters[letter] +=1 

    # if letter in bank then add by 1

    # check if an input from user found in hand
    for char in word1:
    # # return false if letter not in letter bank used
        if char not in letter_bank or check_letters[char] == 0:
            return False
        else:
            check_letters[char] -= 1
            

    return True
    # return true if every letter in input in letter bank
    # elif letter in word in letter_bank:
    #     check_letters[letter] -= 1
    
    

#check if input is some or alll of hand
# return false if input has too much of a letter compared to letter_bank



def score_word(word):
    # passes in a string
    # returns an int representing total score
    # if len of word 7-10 than +8 points
# |Letter                        | Value|
# |:----------------------------:|:----:|
# |A, E, I, O, U, L, N, R, S, T  |   1  |
# |D, G                          |   2  |
# |B, C, M, P                    |   3  |
# |F, H, V, W, Y                 |   4  |
# |K                             |   5  |
# |J, X                          |   8  |
# |Q, Z                          |   10 |
def get_highest_word_score(word_list):
    pass