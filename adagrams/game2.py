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
    letter_pool_list = ('A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
        'B', 'B', 
        'C', 'C', 
        'D', 'D', 'D', 'D', 
        'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 
        'F', 'F', 
        'G', 'G', 'G', 
        'H', 'H', 
        'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 
        'J', 
        'K', 
        'L', 'L', 'L', 'L', 
        'M', 'M', 
        'N', 'N', 'N', 'N', 'N', 'N',
        'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 
        'P', 'P', 
        'Q', 
        'R', 'R', 'R', 'R', 'R', 'R', 
        'S', 'S', 'S', 'S', 
        'T', 'T', 'T', 'T', 'T', 'T', 
        'U', 'U', 'U', 'U', 
        'V', 'V', 
        'W', 'W', 
        'X', 
        'Y', 'Y', 
        'Z')
    draw_letters = []
    
    
    for letter in letter_pool_list:
        while len(draw_letters) < 10:
            tile = random.choice((letter_pool_list))
            if draw_letters.count(tile) < letter_pool_list.count(tile):
                draw_letters.append(tile)
        
        
        return draw_letters

    


def uses_available_letters(word, letter_bank):
    words = word.upper()

    for letters in (words):
        if (all(letters in letter_bank for letters in words)):
            while words.count(letters) <= letter_bank.count(letters):
                return True
            
    else:
            return False





def score_word(word):
    #need to create a score dictionary
    # have a score counter that loops through letter in word and adds the value from the dictionary to the score counter
    score_chart = {
        'A':1,
        'E':1,
        'I':1,
        'O':1,
        'U':1,
        'L':1,
        'N':1,
        'R':1,
        'S':1,
        'T':1,
        'D':2,
        'G':2,
        'B':3,
        'C':3,
        'M':3,
        'P':3,
        'F':4,
        'H':4,
        'V':4,
        'W':4,
        'Y':4,
        'K':5,
        'J':8,
        'X':8,
        'Q':10,
        'Z':10
    }

    sum_score = 0
    words = word.upper()
    for letter in words:
        sum_score += score_chart[letter]
    if len(words) in range(7,11):
        sum_score += 8
        

    return sum_score
        

    
    
    

def get_highest_word_score(word_list):
    # for word in word_list, call score_word(word) function?
    #create an empty tuple and append above to tuple or dict?
    #create a highest word tuple that pulls in the word with the highest score?
    #tie breaking rules: if word in word_list dict/tuple value is the highest and the same as another word,
    #if len of one word is 10 choose that word else choose the word with shortest len
    #if word_score of two words is equal and neither word is 10 letters choose the shorterst len
    #If multiple words have the same score and the same length, pick the first on in the list
    #tuple(dict.keys()to get the key which will be the word,dict[key] to get the value which will be the score)
    #Get max value using max(dict_name)
    #pull all keys with that value to implement tie breaker rules

    word_list_dict = {}
    max_word_list = []
    word_len_10_list = []
    

    for word in word_list:
        word_list_dict[word] = score_word(word)
        print(word_list_dict)
        highest_word_score = max(word_list_dict.values())
    for key, val in word_list_dict.items():
        if word_list_dict[key] == highest_word_score:
            max_word_list.append(key)

    if len(max_word_list) > 1:
        for word in max_word_list:
            if len(word) == 10:
                word_len_10_list.append(word)
                if len(word_len_10_list) > 1:
                    return tuple([word_len_10_list[0], highest_word_score])
                else:
                    return tuple([word_len_10_list[0], highest_word_score])

            else:
                return tuple([(min(max_word_list, key = len)), highest_word_score])
    else:
        return tuple([max(word_list_dict), highest_word_score ])

                    

                

    
    return word_list_dict






    