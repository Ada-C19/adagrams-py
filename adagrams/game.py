import random

def draw_letters(): 
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
    #make an empty list that will hold all available letters
    available_letters = []
    #looping through letter pool dic keys, and adding the key the amount
    #of times the value designates to available letters list
    for letter in LETTER_POOL.keys():
        for num in range(LETTER_POOL[letter]):
            available_letters.append(letter)

    #choose 10 random letters from available letters
    chosen_letters = random.sample(available_letters,k=10)  
    return chosen_letters

def uses_available_letters(word, letter_bank):
    
    letter_bank_copy = letter_bank.copy()
    #add a loop that checks if letter in word is in letter bank copy. 
    for letter in word.upper():
        #if letter in bank copy remove the letter
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        #otherwise break out of function and return false
        else:
            return False
    return True

def score_word(word):
    
    score = 0
    score_values = {
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
    #sum up each letter in word to score, use .upper to make all caps
    for letter in word.upper():
        score+= score_values[letter]
    #add 8 points if len of word is >= 7
    if len(word) >= 7:
        score+= 8

    return score

def get_highest_word_score(word_list):
    #initialize word_score_dict and highest_score_list
    word_scores_dict = {}
    highest_score_list = []
    #add scores as keys to word_score_dict, and words as values in a list
    for word in word_list:
        score = score_word(word)
        if score in word_scores_dict:
            word_scores_dict[score].append(word)       
        else:
            word_scores_dict[score] = [word]
    #set high score by using max function on word_score_dic keys
    highest_score = max(word_scores_dict.keys())
    #set shortest word with min func using lambda to find shortest len word
    shortest_word = min(word_scores_dict[highest_score], key = lambda word: len(word))
    #loop through tie of high score words and make length ==10 best word
    for word in word_scores_dict[highest_score]:
        if len(word) == 10:
            best_word = word
            break
        else:
            best_word = shortest_word
    #add the best word and highest score to the highest_score_list   
    highest_score_list.append(best_word)
    highest_score_list.append(highest_score)

    return highest_score_list 