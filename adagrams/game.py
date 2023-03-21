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
    letter_pool_list = []
    for letter in LETTER_POOL:
        for freq in range(LETTER_POOL[letter]):
            letter_pool_list.append(letter)
    letter_bank = random.sample(letter_pool_list, 10)    
    return letter_bank

def uses_available_letters(word, letter_bank):
    ### determines whether letters used are from letter_bank
    word_cap = word.upper()
    for letter in word_cap:
        if letter not in letter_bank:
            return False
    
    ### determines whether letters are used in appropriate quantities
    ### creates dict with letters as keys and quantities for letter_bank
    letter_bank_num_dict = {}
    letter_bank_set = set(letter_bank)
    for item in letter_bank_set:
        letter_bank_count = 0
        for val in letter_bank:
            if item == val:
                letter_bank_count += 1
        letter_bank_num_dict[item] = letter_bank_count
    
    ### creates dict with letters as keys and quantities for user word
    word_set = set()
    word_num_dict = {}
    for letter in word_cap:
        word_set.add(letter)
    for item in word_set:
        word_set_count = 0
        for letter in word_cap:
            if item == letter:
                word_set_count += 1
        word_num_dict[item] = word_set_count

    ### determines whether quantity of letters in user guess exceeds
    ### available quantity of letters in letter_bank, if so returns false
    for key in letter_bank_num_dict:
        if key in word_num_dict.keys():
            if letter_bank_num_dict[key] < word_num_dict[key]:
                return False
    return True


def score_word(word):
    score = 0
    score_dict = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    if len(word) >= 7:
        score += 8

    for letter in word.upper():
        for key in score_dict:
            if letter in score_dict[key]:
                score += key

    return score

def get_highest_word_score(word_list):
    ### - Has one parameter: `word_list`, which is a list of strings
    ### - Returns a tuple that represents the data of a winning word and it's score.  The tuple must contain the following elements:
    ### - index 0 ([0]): a string of a word
    ### - index 1 ([1]): the score of that word
    ### - In the case of tie in scores, use these tie-breaking rules:
        ### - prefer the word with the fewest letters...
        ### - ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
        ### - If the there are multiple words that are the same score and the same length, pick the first one in the supplied list
    word_list_score_dict = {}
    highest_score_tracker = 0

    ### Calculating scores for each word
    ### Struggling to build dictionary with nested lists
    for word in word_list:
        if score_word(word) not in word_list_score_dict.keys():
            word_list_score_dict[score_word(word)] = [word]
        else:
            word_list_score_dict[score_word(word)] += word
    
    ### Determining highest scoring word
    for score in word_list_score_dict:
        if score > highest_score_tracker:
            highest_score_tracker = score

    print(len(word_list_score_dict[highest_score_tracker]))
    
    if len(word_list_score_dict[highest_score_tracker]) == 1:
        return word_list_score_dict[highest_score_tracker][0], highest_score_tracker
    elif len(word_list_score_dict[highest_score_tracker]) > 1:
        for word_opt in word_list_score_dict[highest_score_tracker]:
            if len(word_opt) == 10:
                return word_opt, highest_score_tracker

