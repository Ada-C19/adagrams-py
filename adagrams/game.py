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
    full_hand = []
    my_hand = []
    main_pool = LETTER_POOL
    for letter in main_pool:
        while full_hand.count(letter) < main_pool[letter]:
            full_hand.append(letter)

    while len(my_hand) < 10:
        random_choice = random.choice(full_hand)
        my_hand.append(random_choice)
        full_hand.remove(random_choice)

    return my_hand



def uses_available_letters(word, letter_bank):
    test_word = []
    word_dict = {}
    word = word.upper()

    for letter in word:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1
            

    for char in letter_bank:
        if char in word:
            test_word.append(char)
    
    final_word = ''.join(test_word)

    if letter in final_word and word_dict[letter] == 1:
            return True
        
    return False

def score_word(word):
    #make a score chart via dictionary that holds the point values of the letters
    #make a statement that if the word's length is > 7 it get 8+ points
    #for each letter in the word, take the value and add it to the score_board
    LETTER_SCORE = {
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
    score_board = 0
    bonus = 8 
    word = word.upper()
    for letter in word:
        if letter in LETTER_SCORE:
            score_board += LETTER_SCORE[letter]
    if len(word) >= 7:
        score_board += bonus
            
    return score_board

def get_highest_word_score(word_list):
    #iterate each word in word list, obtaining the scores of each word 
    #compare the scores; take the best word and score to store it in a tuple
    #find the max
    #loop through list to see who has max
    #make a list to put in possible winners
    #compare list to len of word (shortest wins) tiebreaker
    word_dict = {}
    winners_list = []
    len_list = []

    for word in word_list:
        score = score_word(word)
        word_dict[word] = score

    max_value = max(word_dict.values())
    
    for key in word_dict:
        if word_dict[key] == max_value:
            test_tuple = (key, max_value)
            winners_list.append(test_tuple)
            continue

    for str, value in winners_list:
        length = len(str)
        len_list.append(length)

    min_tie = min(len_list)

    
    if len(winners_list) > 0:
        for winner in winners_list:
            if len(winner[0]) >= 10:
                return winner 
            else:
                continue
        for winner in winners_list:
            if len(winner[0]) == min_tie:
                return winner