import random

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




def draw_letters():
    hand = []
    #Create copy of LETTER_POOL dict to modify without changing original
    copy_letter_pool = LETTER_POOL.copy()

    while len(hand) < 10:
      #Using random.choices to select a random letter after converting the copy to a list & utitlizing the weighted feature to get the weighted possibility of each letter from dict.values() & setting our population sample to 1. 
      random_letter = random.choices(list(copy_letter_pool), weights = copy_letter_pool.values(), k=1)
      #random.choices returns a list, so must index into list to retrieve the value of the random letter
      str_random_letter = random_letter[0]
      
      if copy_letter_pool[str_random_letter] > 0:
        hand.append(str_random_letter)
        copy_letter_pool[str_random_letter] += -1
    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass