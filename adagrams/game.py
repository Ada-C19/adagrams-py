import random
from random import shuffle
from collections import Counter

def draw_letters():
    letters_pool = {
        "A" : 9,
        "B" : 2,
        "C" : 2,
        "D" : 4,
        "E" : 12,
        "F" : 2,
        "G" : 3,
        "H" : 2,
        "I" : 9,
        "J" : 1,
        "K" : 1,
        "L" : 4,
        "M" : 2,
        "N" : 6,
        "O" : 8,
        "P" : 2,
        "Q" : 1,
        "R" : 6,
        "S" : 4,
        "T" : 6,
        "U" : 4,
        "V" : 2,
        "W" : 2,
        "X" : 1,
        "Y" : 2,
        "Z" : 1
    }
    letters_probability = []
    letter_bank = []
    total = sum(letters_pool.values())
    for letter in letters_pool:
        p = letters_pool[letter] / total
        letters_probability.append(p)
    letters = list(letters_pool)

    while len(letter_bank) < 10:
        get_letter = random.choices(letters, weights=letters_probability, k=1)
        letter_count = letter_bank.count(get_letter[0])
        if letter_count < letters_pool[get_letter[0]]:   # Mistake: TypeError: unhashable type:"list"; because random() return a list.
            letter_bank.append(get_letter[0])
            continue
    return(letter_bank)

def uses_available_letters(word, letter_bank):
    word = word.upper()    # convert input word to upper case
    word_count = Counter(word)
    bank_count = Counter(letter_bank)
    return all(word_count[i] <= bank_count[i] for i in word_count)

def score_word(word):
    score_chart = {
        "A" : 1,
        "E" : 1,
        "I" : 1,
        "O" : 1,
        "U" : 1,
        "L" : 1,
        "N" : 1,
        "R" : 1,
        "S" : 1,
        "T" : 1,
        "D" : 2,
        "G" : 2,
        "B" : 3,
        "C" : 3,
        "M" : 3,
        "P" : 3,
        "F" : 4,
        "H" : 4,
        "V" : 4,
        "W" : 4,
        "Y" : 4,
        "K" : 5,
        "J" : 8,
        "X" : 8,
        "Q" : 10,
        "Z" : 10
    }
    sum = 0
    word = [elem.upper() for elem in word]     # convert input word to upper case

    for letter in word:                        # sum each letter's point
        sum += score_chart[letter]
    if len(word) >= 7:                         # chech if the word gets addtional 8 points
        sum += 8
    return sum

def get_highest_word_score(word_list):
    score_list = []
    for i in range(len(word_list)):
        score_list.append(score_word(word_list[i]))         # list of the score of every word
    
    word_score_dict = dict(zip(word_list,score_list))
    max_score = max(word_score_dict.values())             # get the max score
    all_max_words = [k for k,v in word_score_dict.items() if v == max_score]  # list of all max score words
    count_win = len(all_max_words)                          # check how many winning words
    
    # conditional statements
    if count_win == 1:                                      # if only one winning return winning
        return (all_max_words[0], max_score)
    else:                                                    # if have multiple max score
        len_10_str = [string for string in all_max_words if len(string) == 10]      # check len10 when count_win > 1
        count_len_10 = len(len_10_str)                       # count how many len10 words       
        if count_len_10 == 0:                                # if no len10
            return (min(all_max_words, key=len), max_score)  
        else:                                                # have len10
            return (len_10_str[0], max_score)
