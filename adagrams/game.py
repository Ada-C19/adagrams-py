import random
#comment to test Git push
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
    letter_pool_dict = {}
    hand = []
    i = 0

    # append LETTER_POOL keys into a list
    for key in LETTER_POOL.keys():
        letter_pool_list.append(key)
    
    # copy LETTER_POOL dict
    for key, value in LETTER_POOL.items():
        letter_pool_dict[key] = value

    # debug info
    # print(f"letter_pool is {letter_pool}")

    # random.randint() as to append a random index from letter_pool list
    while i < 10:
        letter = letter_pool_list[random.randint(0, 25)] 

        #check if letter is available in letter_pool_dict

        #debug info
        # print(f"letter to check is {letter}")
        # print(f"letter_pool_dict[letter] is {letter_pool_dict[letter]}")
        if letter_pool_dict[letter] > 0:
            hand.append(letter)
            print(f"hand is {hand}")
            letter_pool_dict[letter] -= 1
            i += 1

    return hand
    
hand = draw_letters()
print(hand)

def uses_available_letters(word, letter_bank):
    letter_bank_copy = []
    result = True

    #copy letter_bank
    for letter in letter_bank:
        letter_bank_copy.append(letter)

    for letter in word:
        letter = letter.upper()
        if letter not in letter_bank_copy:
            result = False
            break
        else:
            letter_bank_copy.remove(letter)
    
    return result

def score_word(word):
    score = 0
    VALUE_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    VALUE_2 = ["D", "G"]
    VALUE_3 = ["B", "C", "M", "P"]
    VALUE_4 = ["F", "H", "V", "W", "Y"]
    VALUE_5 = ["K"]
    VALUE_8 = ["J", "X"]
    VALUE_10 = ["Q", "Z"]
    LEN_FOR_BONUS = [7, 8, 9, 10]

    for letter in word:
        letter = letter.upper()
        if letter in VALUE_1:
            score += 1
        elif letter in VALUE_2:
            score += 2
        elif letter in VALUE_3:
            score += 3
        elif letter in VALUE_4:
            score += 4
        elif letter in VALUE_5:
            score += 5
        elif letter in VALUE_8:
            score += 8
        elif letter in VALUE_10:
            score += 10
    
    if len(word) in LEN_FOR_BONUS:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    best_word = ["W", 0]

    for word in word_list:
        word_score = score_word(word)
        if word_score == best_word[1] and len(word) < len(best_word[0]):
            best_word[0] = word
            best_word[1] = word_score
        elif word_score > best_word[1]:
            best_word[0] = word
            best_word[1] = word_score
    
    return best_word