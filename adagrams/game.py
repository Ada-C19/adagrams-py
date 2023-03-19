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

    letter_value = {
    ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
    ('D', 'G'): 2,
    ('B', 'C', 'M', 'P'): 3,
    ('F', 'H', 'V', 'W', 'Y'): 4,
    ('K',): 5,
    ('J', 'X'): 8,
    ('Q', 'Z'): 10
    }
    score = []
    
    for letter, point in letter_value.items():
        for char in word:
            if char.upper() in letter:
                score.append(point)
    
    if len(word) in range(7, 10):
        score.append(8)
            
    return sum(score)


def get_highest_word_score(word_list):
# return a tuple with("word", int(score))
    winning_score = 0
    winning_word = ""
    # calculate score of each word in list
    for word in word_list:
        words_score = score_word(word)
        #wining word with less words or = 10
        # if score is tied of words  or are same length,
        #  winning word is first from list
        if words_score > winning_score:
            winning_score = words_score
            winning_word = word
        
        if words_score == winning_score:
            if len(word) < len(winning_word) or len(word) > len(winning_word) and len(word) == 10:
                winning_word = word
                winning_score = words_score
    final_word = (winning_word, winning_score)
    return final_word
