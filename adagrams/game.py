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

    return random.choices(alphabet_list, k = grab_10_elements)

def uses_available_letters(word, letter_bank):
    """
    input: word as string, and letter_bank as list
    output: boolean of True or False
    """

    for letter in word:
        if letter in letter_bank:
            return True
        else:
            return False 

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
