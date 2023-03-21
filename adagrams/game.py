import random

def draw_letters():

   # create letter pool to draw letters from
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

    # create empty list to hold hand
    hand = []

    # counter for cards; loop to pull random letters from dictionary keys
    #  conditional will draw letters/increment i until 10 cards drawn 
    i = 0
    while i < 10:
        draw_random_letters = random.choice(list(LETTER_POOL.keys()))
        letter_count = hand.count(draw_random_letters)
        if letter_count < LETTER_POOL[draw_random_letters]:
            hand.append(draw_random_letters)
            i += 1

    return hand
   


def uses_available_letters(word, letter_bank):

    # use upper to account for lowercase
    word = word.upper()

    # loop; if letter is not in bank or quantity is wrong, return false
    for letter in word:
        if letter not in letter_bank:
            return False
        elif word.count(letter) > letter_bank.count(letter):
            return False
        
    return True


def score_word(word):

    # lists grouped by the score of each letter
    one_point = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    two_point = ["D", "G"]
    three_point = ["B", "C", "M", "P"]
    four_point = ["F", "H", "V", "W", "Y"]
    five_point = ["K"]
    eight_point = ["J", "X"]
    ten_point = ["Q", "Z"]

    # total starts at 0; check every letter in word, add score to total
    total_score = 0
    word = word.upper()
    for letter in word:
        if letter in one_point:
            total_score += 1
        elif letter in two_point:
            total_score += 2
        elif letter in three_point:
            total_score += 3
        elif letter in four_point:
            total_score += 4
        elif letter in five_point:
            total_score += 5
        elif letter in eight_point:
            total_score += 8
        elif letter in ten_point:
            total_score += 10
   
   # bonus points for the length of the word
    if len(word) >= 7:
        total_score += 8
        
    return total_score       
    

def get_highest_word_score(word_list):

    # start at 0 and empty list bc everything will be more than nothing
    winning_score = 0
    winning_word = ""

    # loop
    # call score from previous function
    # check if every word's score is greater than current winning score
    # if no, loop again; if yes, that becomes the new winning score/word
    # if tie, check the length of the words; scores are tied, don't check again
    # tie if previous word len not 10 and current word is shorter
    # tie if previous word shorter than 10 and current is 10   
    for word in word_list:
        score = score_word(word)
        if score > winning_score:
            winning_score = score
            winning_word = word
        elif winning_score == score:
            previous_word_len = len(winning_word)
            current_word_len = len(word)
            if current_word_len == 10 and previous_word_len < 10:
                winning_word = word
            elif previous_word_len != 10 and current_word_len < previous_word_len:
                winning_word = word

    return (winning_word, winning_score)