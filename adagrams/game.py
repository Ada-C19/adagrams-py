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

letter_values = {
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
    # assign empty array to variable hand
    hand = []
    letter_freq = {}
    # create a for loop to iterate 10 times
    while len(hand) < 10:
        # get random letter from letter pool
        random_letter = random.choice(list(LETTER_POOL.keys()))

        # conditional to check for letter frequency and add to letter frequency dict
        if random_letter in letter_freq:
            letter_freq[random_letter] += 1
        elif not random_letter in letter_freq:
            letter_freq[random_letter] = 1

        # conditional to check that letter frequency does not exceed number in pool
        # append letter to hand list
        if letter_freq[random_letter] < LETTER_POOL[random_letter]:
            hand.append(random_letter)

    # return list
    return hand


def uses_available_letters(word, letter_bank):
    # create variables to hold data structures
    letter_list = list(word.upper())
    letter_bank_freq = {}
    letter_list_freq = {}

    # loop through letter bank to count frequencies
    for letter in letter_bank:
        if letter in letter_bank_freq:
            letter_bank_freq[letter] += 1
        else:
            letter_bank_freq[letter] = 1

    # loop through letter list to check if letter is in bank and count frequences
    for letter in letter_list:
        if letter not in letter_bank:
            return False
        elif letter in letter_list_freq:
            letter_list_freq[letter] += 1
        elif not letter in letter_list_freq:
            letter_list_freq[letter] = 1

    # Check if letter is used more than avaiable times than in letter bank
    if letter_list_freq[letter] > letter_bank_freq[letter]:
        return False

    # Return True if inputted word is valid given letter bank
    return True

def score_word(word):
    # assign int to variable for the score
    score = 0
    letter_list = list(word.upper())

    # create a loop to add values of each letter to score
    for letter in letter_list:
        score += letter_values[letter]

    # check length of word for bonus point 
    if len(letter_list) >= 7:
        score += 8

    # return score
    return score

def get_highest_word_score(word_list):
    all_words_dict = {}
    
    for word in word_list:
        score = score_word(word)
        all_words_dict[word] = score
    
    scores = all_words_dict.values()
    score_list = list(scores)
    score_list.sort()
    best_word_list = []
    for word in all_words_dict:
        if all_words_dict[word] == score_list[-1]:
            best_word_list.append(word)
    
    best_word_list.sort()
    best_word_lengths = []

    for word in best_word_list:
        best_word_lengths.append(len(word))

    best_word_lengths.sort()

    for word in best_word_list:
        if len(word) >= 10:
            return best_word_list[0], score_list[-1]
        elif best_word_lengths[0] == len(word):
            return word, score_list[-1]

    return best_word_list[-1], score_list[-1]