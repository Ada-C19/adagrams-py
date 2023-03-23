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
    num_letters = 10 
    letters, weights = zip(*LETTER_POOL.items())
    hand = []
    valid_hand = False


    while not valid_hand:
        count = 0
        hand_dict = {}
        hand = random.choices(letters, weights, k = num_letters)
        for letter in hand:
            if letter in hand_dict:
                hand_dict[letter] += 1
            else:
                hand_dict[letter] = 1 
  
        for letter in hand_dict.keys():
            if hand_dict[letter] <= LETTER_POOL[letter]:
                count += 1

        if count == 10:
            valid_hand = True
        else:
            hand = random.choices(letters, weights, k = num_letters) 

    return hand


def uses_available_letters(word, letter_bank):
    word = list(word.upper())
    letter_bank = list("".join(letter_bank).upper())
    matched_letters = []
  
    if len(word) <= len(letter_bank):
        for letter in letter_bank:
            if word.count(letter) <= letter_bank.count(letter):
                continue
            elif word.count(letter) > letter_bank.count(letter):
                return False

        for letter in word:
           if letter in letter_bank:
               matched_letters.append(letter)
           else:
               return False


        if len(word) == len(matched_letters):
            for letter in word:
                if word.count(letter) <= matched_letters.count(letter):
                    continue
                else:
                    return False
        
            return True
        else:
            return False
    
    else:
        return False
    

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass