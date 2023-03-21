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

    aux_letter_pool = LETTER_POOL.copy()
    
    available_letters_list = []

    while len(available_letters_list) < 10:
        numbers = (random.randint(65,90))
        letters_for_user = chr(numbers)

        if aux_letter_pool[letters_for_user] > 1:
            available_letters_list.append(letters_for_user) 
            aux_letter_pool[letters_for_user] -= 1

    return available_letters_list



def uses_available_letters(word, letter_bank):
    word = word.upper()
    if len(letter_bank) < len(word):
        return False
    aux_letter_bank = letter_bank.copy()
    for letter in word:
        if letter in aux_letter_bank:
            aux_letter_bank.remove(letter)
        else:
            return False
            
    return True


def score_word(word):
    
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
    'Z': 10}

    score = 0

    for letter in word:
        score += LETTER_SCORE[letter.upper()]

    if len(word) >= 7:
        score = score + 8
    
    return score


def get_highest_word_score(word_list):
        
    score_list = []
    dict_word_score = {}
        
    
    for word in word_list:
        score_for_each_word = score_word(word)
        score_list.append(score_for_each_word)
        score_list  
        
    dict_word_score = dict(zip(word_list,score_list))
        
    max_value = max(dict_word_score.values())
    #crear diccionario con los top scores
    dict_top_score = {}
    list_max_score = []
    #list_min_score = []

    #guardamos todas las palabras que hayan conseguido el score maximo.
    #E.g. si el score maximo era 20, guardamos todos los key que tengan value == 20
    for key in dict_word_score:
        if dict_word_score[key] == max_value:
            dict_top_score[key] = max_value
            
    # si solo habia una palabra con el valor maximo, entonces esa es la ganadora
    if len(dict_top_score) == 1:
        for key in dict_top_score:
            list_max_score.insert(0,key)
            list_max_score.insert(1,dict_top_score[key])
            return list_max_score
        #return list[0] = word [1] = score
    ############# sino ############################################################################
    else:
    # buscamos la primera palabra que tenga len == 10, si es que hay.
        for key in dict_top_score:
            if len(key) == 10:
                list_max_score.insert(0,key)
                list_max_score.insert(1,score)
                return list_max_score
                #return list[0] = key list[1] = score
    
    #por ultimo, si es que no encontramos una palabra de largo 10, entonces
    #buscamos la palabra con la menor longitud.
    #e.g. si tenemos palabra "[casa, 20]", "[perro, 20]", el len minimo es de casa.


    #busco el valor minimo
    min_value = min(dict_word_score.values())
    for key in dict_top_score:
        if len(key) < min_value:
            min_value = len(key)

    #y al final, solo retornamos la primera palabra que tenga el largo minimo calculado anteriormente
    for key in dict_top_score:
        if dict_top_score[key] == min:

            #return list[0] = key list[1] = score