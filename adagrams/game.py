import random
def draw_letters():
    letters =[]
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
    while len(letters) <10:
        letter = random.choice(list(LETTER_POOL)) 
        if LETTER_POOL[letter] > 0:
            LETTER_POOL[letter] -= 1
        else: 
            continue
        letters.append(letter)
    return letters





def uses_available_letters(word, letter_bank):
    new_word=word.upper()
    letter_bank_copy =list(letter_bank)
    for letter in new_word:
        if letter not in letter_bank_copy:
            return False 
        elif letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
    return True 
        


        

def score_word(word):
    points =[]
    score_chart = {
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
    new_word=word.upper()
    for letter in new_word:
        if letter in score_chart:
            points.append(score_chart[letter])
    total= sum(points)
    if len(new_word) ==7 or len(new_word)==8 or len(new_word)==9 or len(new_word)==10:
        total+=8
    else:
        total+=0
    return total

def get_highest_word_score(word_list):
    scores_dict={}
    maximum = 0
    max_key = None
    word_list.sort(key=len)
    for word in word_list:
        puntos = score_word(word)
        scores_dict[word] = puntos
    for scores in scores_dict :
        if scores_dict[scores] > maximum:
            maximum = scores_dict[scores]
            max_key = scores
        elif len(word_list[-1]) == len(word_list[0]) and puntos == maximum:
            max_key = (word_list[0])
        elif len(word_list[-1]) == len(word_list[-2]) and puntos ==maximum:
            max_key = word_list[-2]
        elif len(word_list[-1]) == 10 and puntos == maximum:
            max_key = word_list[-1]
    return (max_key, maximum)

# how can I do this using max()?
# I originally had this but didn't how how to break ties according to len() using max().
#
#  def get_highest_word_score(word_list):
#     word_list.sort(key=len)
#     score_dict={}
#     for word in word_list:
#         puntos = score_word(word)
#         score_dict[word]=puntos
#     winner = max(score_dict, key=score_dict.get)
#     return(winner, score_dict[winner])