import random

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
    
    # initiate draw_letters to record and return drawn random letters
    # initiate letter_freq to check the frequency of drawn out random letters
    draw_letters_list = []
    letter_freq = {}
    
    # create random letter picking from the letter poll
    # only append letters that are no bigger than letter poll frequency
    while len(draw_letters_list) < 10:
        cur_random_letter = random.choice(list(LETTER_POOL.keys()))
        if cur_random_letter in letter_freq.keys():
            letter_freq[cur_random_letter] += 1
        else:
            letter_freq[cur_random_letter] = 1
        if letter_freq[cur_random_letter] > LETTER_POOL[cur_random_letter]:
            continue
        else:
            draw_letters_list. append(cur_random_letter)
    return draw_letters_list

def uses_available_letters(word, letter_bank):
    
    # check each letter's frequency and record in letter_bank_freq
    letter_bank_freq = {}
    for letter in letter_bank:
        if letter in letter_bank_freq:
            letter_bank_freq[letter] += 1
        else:
            letter_bank_freq[letter] = 1

    # check if every letter or its lower-case form in word existed in letter_bank 
    # also check the occurance of each letter not bigger than its frequency in the letter_bank      
    for letter in word:
        if letter and letter.upper() not in letter_bank:
            return False
        else:
            if letter in letter_bank:
                letter_bank_freq[letter] -= 1
                if letter_bank_freq[letter] < 0:
                    return False
            else:
                letter_bank_freq[letter.upper()] -= 1
                if letter_bank_freq[letter.upper()] < 0:
                    return False
    return True
    

def score_word(word):

    # based on the score chart to create score_dic with each letter's score
    score_dic = {}
    score_dic[1] = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T" ]
    score_dic[2] = ["D", "G" ]
    score_dic[3] = ["B", "C", "M", "P"]
    score_dic[4] = ["F", "H", "V", "W", "Y" ]
    score_dic[5] = ["K"]
    score_dic[8] = ["J","X"]
    score_dic[10] = ["Q","Z"]

    # check if each letter of word existed in score_word and get its score accordingly
    score_sum = 0
    for letter in word:
        for key, value in score_dic.items():
            if letter in value or letter.upper() in value:
                score_sum += key

    # if the length of word is between 7 to 10, add 8 to sum
    if 7 <= len(word) and len(word) <= 10:
        score_sum += 8

    return score_sum

def get_highest_word_score(word_list):

    highest_score = 0
    highest_letter = ""

    # iterate word_list to update highest_score and highest_letter
    for word in word_list:
        cur_score = score_word(word)
        if cur_score > highest_score:
            highest_score = cur_score
            highest_letter = word
        elif cur_score == highest_score:
              # when two letters' scores are tied, return the first one
            if len(highest_letter) == 10 and len(word) == 10:
                continue
            # when two letters' scores are tied, return the one with 10 letters
            elif len(word) == 10:
                highest_letter = word
            # when two letters' scores are tied and both length are not 10, return the shorter one
            elif len(highest_letter) != 10 and len(word) < len(highest_letter):
                highest_letter = word

    return highest_letter, highest_score
