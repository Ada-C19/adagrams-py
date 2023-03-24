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
    
    def transform_to_dictionary_without_replacement(data_type):
        output = {}
        
        for element in data_type:
            if element in output:
                output[element] += 1
            else:
                output[element] = 1

        return output
    

    if len(word) == 0:
        return False

    if word is not word.upper():
        word = word.upper()

    # calling transform_to_dictionary_without_replacement on word string and
    # letter_bank list to turn the inputs of uses_available_letters into dicts
    word_dict = transform_to_dictionary_without_replacement(word)
    letters_dict = transform_to_dictionary_without_replacement(letter_bank)
        
    for key, value in word_dict.items():
        if key in letters_dict:
            letters_dict[key] = letters_dict[key] - value
        else:
            return False

    # transforming letter_dict_values into a list to check if value is < 0
    letter_dict_values = letters_dict.values()

    for value in letter_dict_values:
        if value < 0:
            return False

    return True


def score_word(word):
    """
    input: word (string of characters/letters)
    output: number of points integer
    """

    letter_point_value_dict = {
        "A": 1,
        "E": 1,
        "I": 1,
        "O": 1,
        "U": 1,
        "L": 1,
        "N": 1,
        "R": 1,
        "S": 1,
        "T": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10
    } 

    user_score = 0
    long_word_bonus = 8

    if len(word) > 10 or len(word) == 0:
        return False
    
    if word is not word.upper():
        word = word.upper()

    # updates user_score through every iteration of letter in word
    for letter in word:
        user_score = user_score + letter_point_value_dict[letter]
            
    # if checks if user will get long_word_bonus
    if len(word) > 6:
        user_score = user_score + long_word_bonus


    return user_score


def get_highest_word_score(word_list):
    """
    input: word_list (list of strings)
    output: word string, and score of word (tuple) 
    """

    word_and_point_value_dict = {}

    # iterating through each element in word_list 
    for element in word_list:
        word_and_point_value_dict[element] = score_word(element)

    # gets highest scoring word
    highest_score = max(word_and_point_value_dict.values())
    print(highest_score)

    # gets word with the highest score
    word_with_highest_score = max(word_and_point_value_dict, key=word_and_point_value_dict.get)
    print(word_with_highest_score)
    

    return tuple([word_with_highest_score, highest_score])
