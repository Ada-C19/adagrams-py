import random
from collections import Counter

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

LETTER_SCORES = {
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

def draw_letters():
    """""""""
    input: no parameters
    output: 10 letters, each letter repeats proper # of times
    """""""""
# created a space to store our letters list
    letter_list = []
# we want to loop 10 times
    while len(letter_list) < 10:
# populate a letter randomly in 10x loop
        letter = random.choice(list(LETTER_POOL.keys()))
# letter frequency is saved in dict using Counter function
        letter_counts = Counter(letter_list)
        if letter not in letter_list:
            letter_list.append(letter)
# only add letter after chekcing its limit
        elif letter_counts[letter] < LETTER_POOL[letter]:
            letter_list.append(letter)
    return letter_list
    
def uses_available_letters(word, letter_bank):
# create new dicts with letters and their counts
    letter_dict = Counter(letter_bank)
    word_dict = Counter(list(word.upper()))
# loop for every letter/character thats in the word
    for char in word_dict.keys():
# check to see if the letter from the word is present enough times
        if word_dict[char] <= letter_dict[char]:
            letter_dict[char]
        else:
            return False
    return True
    

def score_word(word):
# create a space for all the scores and ................................
    scores = []
    total = 0
# loop for ever letter/character in the word
    for char in list(word.upper()):
# retrieve the letter value and add to scores list
        scores.append(LETTER_SCORES[char])
# add extra points to total if word is 7 - 10 characters long
    if len(scores) >= 7 and len(scores) <= 10:
        total += 8
# sum all values and add to total
    for value in scores:
        total += value
    return total

def get_highest_word_score(word_list):
# collect all words from word_list and use it as a key and its score will be the value
    all_scores_dict = {}
    for word in word_list:
        all_scores_dict[word] = score_word(word)
# variable for the word with the highest score
    highest_word = [None, 0]
# loop through the dictionary that has all words and their scores
    for word, score in all_scores_dict.items():
# assign the tuple values of words with the highest scores
        if score > highest_word[1]:
            highest_word[0] = word
            highest_word[1] = score
# if there is a tie for the highest score
        elif score == highest_word[1]:
# if the currently highest score word is 10 chars long, keep it
            if len(highest_word[0]) == 10:
                continue
# if the incomming word is 10 char long, update tuple
            if len(word) == 10:
                highest_word[0] = word
                highest_word[1] = score
# if none are 10 chars long, keep the shortest word in tuple
            elif len(word) < len(highest_word[0]):
                highest_word[0] = word
                highest_word[1] = score
        else:
            continue

    return tuple(highest_word)