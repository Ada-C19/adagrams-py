import random
import array

LETTER_LIST = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']

def draw_letters():
    letters = []

    letters = random.sample(LETTER_LIST,10)

    # random.shuffle(LETTER_LIST)
    # letters = LETTER_LIST[:10]

    # while len(letters) < 10:
    #     letter = random.choice(LETTER_LIST)
    #     letters.append(letter)
        # LETTER_LIST.remove(letter)
    
    return letters

def uses_available_letters(word, letter_bank):
    # for i in word:
    #     if i not in letter_bank:
    #         return False
    #     else:
    #         # letter_bank.remove(i)
    #         return True
    word_ =  []
    letter_bank_ = []

    for i in word:
        word_.append(i)
    for i in letter_bank:
        letter_bank_.append(i)

    counter = 0
    for i in word_:
        for j in letter_bank_:
            if i == j:
                counter += 1
                letter_bank_.remove(j)
    if counter == len(word):
        return True
    else:
        return False
        
            


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass