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

    for letter in word:
        big_word = word.upper()
        word = big_word

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
    pass

def get_highest_word_score(word_list):
    pass