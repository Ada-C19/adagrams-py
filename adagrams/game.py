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
        word_.append(i.casefold())
    for i in letter_bank:
        letter_bank_.append(i.casefold())

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
    score = 0
    # score_1 = ['A', 'E', 'I', 'O', 'U', 'L' ,'N','R','S','T']
    # score_2 = ['D', 'G']
    # score_3 = ['B', 'C', 'M', 'P']
    # score_4 = ['F', 'H', 'V', 'W','Y']
    # score_5 = ['K']
    # score_8 = ['J','X']
    # score_10 = ['Q','Z']
    score_1 = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'L', 'l','N', 'n', 'R', 'r', 'S','s', 'T','t']
    score_2 = ['D', 'd', 'G', 'g']
    score_3 = ['B', 'b', 'C', 'c', 'M', 'm','P', 'p']
    score_4 = ['F', 'f', 'H', 'h', 'V', 'v', 'W', 'w','Y', 'y']
    score_5 = ['K', 'k']
    score_8 = ['J','j','X', 'x']
    score_10 = ['Q', 'q','Z', 'z']

    word_ =  []

    for i in word:
        word_.append(i.casefold())

    counter = 0
    for i in word_: 
        # if i == 'A' or 'E' or 'I' or 'O' or 'U' or 'L' or 'N' or 'R' or 'S' or 'T':
        if i in score_1:
            score += 1
            # counter += 1
        # elif i == 'D' or 'G': 
        elif i in score_2:
            score += 2
            # counter += 1
        # elif i == 'B' or 'C' or 'M' or 'P':
        elif i in score_3:
            score += 3  
            # counter += 1
        # elif i == 'F' or 'H' or 'V' or 'W' or 'Y':
        elif i in score_4:
            score += 4
            # counter += 1
        # elif i == 'K':
        elif i in score_5:
            score += 5
            # counter += 1
        # elif i == 'J' or 'X':
        elif i in score_8:
            score += 8
            # counter += 1
        # elif i == 'Q' or 'Z':
        elif i in score_10:
            score += 10
            # counter += 1
    
    if len(word_) <= 10 and len(word_) >= 7:
        score += 8
    

    # if len(word_) == 7 or 8 or 9 or 10: # still dont understand why this doesnt work, come back
    #     score += 8
    # else: 
    #     score += 0

    # if counter == 7 or 8 or 9 or 10:
    #         score += 8
    # else:
    #         score += 0

    # counter = 0
    # while counter < 1:
    #     if len(word) == 7 or 8 or 9 or 10:
    #         score += 8
    #     counter +=1

    return score
        

def get_highest_word_score(word_list):
    tuple_list = []
    for i in word_list:
        tuple_list.append((i, score_word(i)))

    # for i in tuple_list:

    best_word_list = sorted(tuple_list, key=lambda t: t[1], reverse = True)
    
    tie_breaker_list = []

    for i in best_word_list:
        if i[1] == best_word_list[0][1]:
            tie_breaker_list.append(i)

    tie_breaker_list_sorted = sorted(tie_breaker_list, key=lambda x: len(x[0]))

    for i in tie_breaker_list_sorted:
        if len(tie_breaker_list_sorted[0][0]) == len(tie_breaker_list_sorted[1][0]):
            if tie_breaker_list_sorted[0][0] == word_list[0]:
                best_word = tie_breaker_list_sorted[0]
            else:
                best_word = tie_breaker_list_sorted[1]

                
        elif len(i[0]) == 10:
            best_word = i
        else:
            best_word = tie_breaker_list_sorted[0]

    return best_word
    

    # if best_word_list[0] > best_word_list[1]:
    #     best_word = best_word_list[0]
    # elif best_word_list[0] == best_word_list[1] and best_word_list[1] > best_word_list[2]:
    #     if len(best_word_list[0][0]) > len(best_word_list[1][0]):
    #         best_word = best_word_list[1]
    #     else:
    #         best_word = best_word_list[0]
    # elif best_word_list[0] == best_word_list[1] == best_word_list[2] and best_word_list[2] > best_word_list[3]:
    #     if len(best_word_list[0][0]) > len(best_word_list[1][0]):
    #         best_word = best_word_list[1]
    #     elif len(best_word_list[2][0]) > len(best_word_list[1][0]
    # elif best_word_list[0] == best_word_list[1] == best_word_list[2] == best_word_list[3] and best_word_list[3] > best_word_list[4]:



    return best_word
