import random 
import pdb

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
    LENGTH_OF_HAND = 10
    hand = []
    
    # based on the desired length of the hand (in this case, 10), 
    # the loop will simulate a player 'picking' 10 random letters 
    # for their hand
    
    while len(hand) < LENGTH_OF_HAND: 
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
    # (in the right quantities) i.e. if the user's guess contains 3 Y's and
    # the hand only has 1, then it will return false
    # we cannot use a set for duplicating the letter_bank variable
    # because it only store unique elements! 
    # will not be helpful with duplicates

    word_is_in_letter_bank = True
    string_letter_bank = ""

    for letter in letter_bank: 
        string_letter_bank += letter
    
    # check to see if there are more letters in the word than 
    # in the letter_bank 
    if len(word) > len(letter_bank): 
        return False

    for character in word:
        character = str.upper(character)
        if character in string_letter_bank: 
            string_letter_bank = string_letter_bank.replace(character, '')
        else: 
            word_is_in_letter_bank = False
            break
    
    return word_is_in_letter_bank 

def score_word(word):
    # make a dictionary to create a key value pair between the letter 
    # and its' point value
    LETTER_SCORE = {
    'A': 1, 
    'B': 3,
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

    score = 0 

    # iterate through the word and use the character as 
    # a key to grab the
    # value that it's associated to in the dictionary
    for letter in word: 
        letter = str.upper(letter)
        score += LETTER_SCORE[letter]
    
    # add additional points to the score based on length of the word
    if len(word) >= 7 and len(word) <= 10: 
        score += 8

    return score


def get_highest_word_score(word_list):
    # input: list of strings
    # output: tuple (str, int)
    MAX_LENGTH = 10 
    highest_score = 0
    winner = ""

    # go through the the word list and caculate the highest score
    # for each word, keep track of the highest scoring word
    for word in word_list: 
        score = score_word(word)
        if score > highest_score: 
            highest_score = score
            winner = word
        
        # tie breaker logic
        elif score == highest_score:
            if len(word) == MAX_LENGTH and len(winner) != MAX_LENGTH: 
                winner = word
            elif len(word) < len(winner) and len(winner) < MAX_LENGTH:
                winner = word

    return winner, highest_score