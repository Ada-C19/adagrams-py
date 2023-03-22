from random import choice

LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 
    'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 
    'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 
    'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
    'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 
    'Z': 1
}
LETTER_VALUES = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 
    'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 
    'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 
    'Z': 10
}
VOWELS = ["A", "E", "I", "O", "U", "Y"]

def draw_letters():
    # build the pool of letters as a list with all 
    # the letters the appropriate number of times
    all_letters = []
    for key, value in LETTER_POOL.items():
        for i in range(value):
            all_letters.append(key)

    # build the hand making sure at least 3 letters are vowels
    vowel_count = 0
    while vowel_count < 3:
        hand = []
        for i in range(10):
            random_letter = choice(all_letters)
        
            # make sure we dont exceed the number allowed for that letter
            random_letter_count_in_hand = hand.count(random_letter)
            while random_letter_count_in_hand == LETTER_POOL[random_letter]:
                random_letter = choice(all_letters)
                random_letter_count_in_hand = hand.count(random_letter)
            
            # add the letter to the hand
            hand.append(random_letter)
        
        # makes sure vowel_count is updated before we go through the loop again.
        vowel_count = 0
        for vowel in VOWELS:
            vowel_count += hand.count(vowel)
        print(f"{vowel_count=}")
    return hand


def uses_available_letters(word, letter_bank):
    # formats the word list
    word_list = list(word.upper())
    for letter in word_list:
        # checks if letter is in the letter bank.
        if letter not in letter_bank:
            return False
        
        # make sure there are not too many of a letter
        if word_list.count(letter) > letter_bank.count(letter):
            return False
    return True


def score_word(word):
    score = 0

    # Iterate through the word and add to the score as we go
    for letter in list(word.upper()):
        score += LETTER_VALUES[letter]
    
    # if the len of the word is > 7 add the bonus
    if len(word) >= 7:
        score += 8
    return score


def get_highest_word_score(word_list):
    # initialize the best score and the list with a word and score tuple
    words_and_scores = []
    best_score = tuple([0, 0])
    for word in word_list:
        words_and_scores.append(tuple([word, score_word(word)]))

    # Iterate through the words and scores list and check their values
    for tup in words_and_scores:
        # update best score if a score is higher than the current best score value
        if tup[1] > best_score[1]:
            best_score = tup
        # deal with a tie
        if tup[1] == best_score[1]:
            # sets best score to new tup if its len is 10 then returns becasue the first
            # one of these answers will always win so we will just return if we get here 
            if len(tup[0]) == 10:
                best_score = tup
                return best_score
            # sets best score to new tup if its shorter 
            # if there are multiple of this situation, 
            # it will continue to find the shortest
            # otherwise, it wont change, making the existing best score stand
            elif len(tup[0]) < len(best_score[0]):
                best_score = tup

    return best_score