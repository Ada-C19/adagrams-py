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
    # (in the right quantities) i.e. if the user's guess contains 3 Y's and
    # the hand only has 1, then it will return false
    # we cannot use a set because it only store unique elements! 
    # will not be helpful with duplicates

    word_list = []
    word_is_in_letter_bank = True
    string_letter_bank = ""

    # place each character from word in a list
    # all upper case to do accurate comparisons
    for character in word: 
        word_list.append(character.upper())
    
    # make a string from the letter bank to compare
    # each letter in the word 
    for letter in letter_bank: 
        string_letter_bank += letter
    
    # check to see if there are more letters in the word than 
    # in the letter_bank 
    if len(word) > len(letter_bank): 
        return False

    for character in word_list: 
        if character in string_letter_bank: 
            string_letter_bank = string_letter_bank.replace(character, '')
        else: 
            word_is_in_letter_bank = False
            break
    
    return word_is_in_letter_bank 

def score_word(word):
    # data structure for the score chart
    SCORE_CHART = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 
    2: ['D', 'G'], 
    3: ['B', 'C', 'M', 'P'], 
    4: ['F', 'H', 'V', 'W', 'Y'], 
    5: ['K'], 
    8: ['J', 'X'],  
    10: ['Q', 'Z']

}
    # make the word upper case for case insenstive comparison
    # a score variable to keep track of the points
    word_case = str.upper(word)
    score = 0

    # iterate through the word and check to see if it is within the score
    # chart dictionary
    for char in word_case:
        for key, letters in SCORE_CHART.items():  
            if char in letters: 
                score += key

    # add additional points to the score based on length of the word
    if len(word_case) >= 7 and len(word_case) <= 10: 
        score += 8

    return score

def get_highest_word_score(word_list):
    # input: list of strings
    # output: tuple (str, int)

    highest_score = 0
    winner = "" 

    # go through the the word list and caculate the highest score
    # for each word (ignoring case), keep track of the highest scoring word

    for word in word_list: 
        score = score_word(word)
        if score > highest_score: 
            highest_score = score
            winner = str.upper(word)

    return winner, highest_score