import random

    
def draw_letters():
    letter_pool = {
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
    # create list of strings 'letters'
    letters = []
    # create empty list 'hand'
    hand = []
    # build a random hand of 10 letters for the user
    while len(hand) < 10:
        letter_pool_keys = letter_pool.keys()
        letter_list = list(letter_pool_keys)
        if len(letter_list) > 0:
            letter = random.choice(letter_list)
        # Return hand that has one letter each per list item
            if letter_pool[letter] > 0:
                hand.append(letter)
                # subtract from letter pool
                letter_pool[letter] -= 1
            elif letter_pool[letter] == 0:
                del letter_pool[letter]
    return hand

def uses_available_letters(word, letter_bank):
    # create var to count  occurrences of each letter in  word
    word = word.upper()
    word_letter_count = {}
    for letter in word:
        word_letter_count[letter] = word_letter_count.get(letter, 0) + 1
    # create var to count occurrences of each letter in the letter bank
    bank_letter_count = {}
    for letter in letter_bank:
        # get keyname and value for each letter
        bank_letter_count[letter] = bank_letter_count.get(letter, 0) + 1
    # compare the word_letter_count and bank_letter_count to see if word can be made 
    for letter, count in word_letter_count.items():
        # check if not in bank_letter_count
        if letter not in bank_letter_count or count > bank_letter_count[letter]:
            return False
    return True

def score_word(word):
    letter_values = {
        "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4,
        "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3,
        "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
        "Y": 4, "Z": 10
    }
    # intialize score to 0
    score = 0
    # default to uppercase
    word = word.upper()
    for letter in word:
        # add score from letter val to overall score 
        score += letter_values.get(letter, 0)
    # create if clause for words btwn len of 7 to 10  
    if len(word) >= 7 and len(word) <= 10:
        # add 8 to score var
        score += 8
    return score

def get_highest_word_score(word_list):
    # initialize highest_score var, int
    highest_score = 0
    # initialize winning_word var, str
    winning_word = ""
    for word in word_list:
        # get score for each word 
        score = score_word(word)
        # find highest scoring word comp'd to previous words
        if score > highest_score:
            # designate highest score and the best word
            highest_score = score
            winning_word = word
        # if score is tied btwn two dif words w/ one word being 10 char long, 10 char long word wins 
        elif score == highest_score:
            print(105, score, highest_score)
            if (len(word) == 10 and len(winning_word) < 10) or len(word) > len(winning_word):
                winning_word = word
            # create code block for if the two highest words are less than 10 choose the shortest word 
    return (winning_word, highest_score)