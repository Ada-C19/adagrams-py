# import everything (alphabet_list) from alphabet_letters file
from adagrams.alphabet_letters import *
import random

def draw_letters():
    """
    input: None
    output: list of 10 randomly generated letters from generate_alphabet_letters()
    """

    grab_10_elements = 10
    alphabet_list = generate_alphabet_letters() 

    return random.sample(alphabet_list, grab_10_elements)

def uses_available_letters(word, letter_bank):
    """
    input: word as string, and letter_bank as list
    output: boolean of True or False
    """

    # ignore letter casing code
    # BUT STILL NOT passing test letters_ignore_case()
    if word is not word.upper():
        word = word.upper()
        print(word)


    # if word uses all 10 available letters in list, 
    # don't do more logic, just return True
    if len(word) == 10:
        return True


    # logic for if letter in word is not in letter_bank
    for letter in word:
        if letter not in letter_bank:
            return False
        else:
            print('here')
            break



    # # logic to pass 
    # # test_uses_available_letters_true_word_in_letter_bank()
    # for letter in word:
    #     if letter in letter_bank:
    #         return True
    #     else:
    #         return False


    # # iterate through string and check if each letter is in
    # # list letter_bank without replacement


    # for letter in word:
    #     for element in letter_bank:
    #         if letter in letter_bank:
    #             letter_bank.remove(letter)
    #             print(letter_bank)



    # # not removing letter from list, need to update logic
    # for letter in word:
    #     if letter in letter_bank:
    #         letter_bank.remove(letter)
    #         return True 
    #         # print(letter_bank)
    #         # continue
    #     else:
    #         return False 



















def score_word(word):
    pass
    # """
    # input: word (string of characters/letters)
    # output: number of points integer
    # """

    # comment in later: dictionary of letters and values
    # letter_point_value_dict = {
    #     "A": 1,
    #     "E": 1,
    #     "I": 1,
    #     "O": 1,
    #     "U": 1,
    #     "L": 1,
    #     "N": 1,
    #     "R": 1,
    #     "S": 1,
    #     "T": 1,
    #     "D": 2,
    #     "G": 2,
    #     "B": 3,
    #     "C": 3,
    #     "M": 3,
    #     "P": 3,
    #     "F": 4,
    #     "H": 4,
    #     "V": 4,
    #     "W": 4,
    #     "Y": 4,
    #     "K": 5,
    #     "J": 8,
    #     "X": 8,
    #     "Q": 10,
    #     "Z": 10
    # } 


    # comment in this code later
    # user_score = 0
    # long_word_bonus = 8


    # comment this code in later
    # code to look up each letter in word by looking at key
    # in dict and then adding value to user_score




    # comment in this code later, checks if len(word) is 
    # 7, 8, 9, or 10 to add additional 8 points
    # if len(word) >= 7 and <= 10:
    #     user_score = user_score + long_word_bonus


    # return user_score





def get_highest_word_score(word_list):
    pass
    # """
    # input: word_list (list of strings)
    # output: word string, and score of word (tuple) 
    # """

    # comment in this code later, empty list to append to
    # THEN need to convert list to tuple
    # so I can return tuple for this function

    # winning_word = []


    # code for checking highest scoring word
    # code for addressing ties





    # return tuple(winning_word)