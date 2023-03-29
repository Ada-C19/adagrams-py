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
    #applying a copy of LETTER_POOL to full_hand to avoid 
    #modifying original
    for letter in LETTER_POOL:
        while full_hand.count(letter) < LETTER_POOL[letter]:
            full_hand.append(letter)

    #take random letter from full_hand then remove once taken
    while len(my_hand) < 10:
        random_choice = random.choice(full_hand)
        my_hand.append(random_choice)
        full_hand.remove(random_choice)

    return my_hand



def uses_available_letters(word, letter_bank):
    test_word = []
    word_dict = {}
    word = word.upper()

    #storing the letter and amount from word into word_dict
    for letter in word:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1
            
    #letters in letter_bank that match letters in word
    #append to test_word
    for char in letter_bank:
        if char in word:
            test_word.append(char)
    
    #convert test_word into a string (final_word)
    final_word = ''.join(test_word)

    #check that letters don't repeat in list
    if letter in final_word and word_dict[letter] == 1:
            return True
        
    return False

def score_word(word):
    #create a constant, a variable to keep track of points, another for bonus points
    #assign word to always capitalize itself
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

    #check each letter's score and add it into score board
    #if word has more than 7 letters, provide bonus points
    for letter in word:
        if letter in LETTER_SCORE:
            score_board += LETTER_SCORE[letter]
    if len(word) >= 7:
        score_board += bonus
            
    return score_board

def get_highest_word_score(word_list):
    word_dict = {}
    winners_list = []
    len_list = []

    #obtain scores for each word and create key,value pairs for word_dict
    #line 133: first word with 10 letters gets automatic win
    for word in word_list:
        score = score_word(word)
        word_dict[word] = score
        if len(word) == 10:
            return (word, score)
        else:
            continue

    #obtain the highest value within the dictionary for the winner
    max_value = max(word_dict.values())
    
    #check each key to see which matches max score; put them in winners_list
    #continue to make sure all keys are iterated
    for key in word_dict:
        if word_dict[key] == max_value:
            test_tuple = (key, max_value)
            winners_list.append(test_tuple)

    #iterate through winners_list to collect len(string) of each word to 
    #put in len_list
    for str, value in winners_list:
        length = len(str)
        len_list.append(length)

    #create a variable that stores the smallest value in len_list
    min_tie = min(len_list)

    #tie-breaker check; return winner 
    if len(winners_list) > 0:
        for winner in winners_list:
            if len(winner[0]) == min_tie:
                return winner