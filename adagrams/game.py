import random
import array

# manually typed list of all the letters (and how many of them as repeats) that are allowed
LETTER_LIST = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']

def draw_letters():
    letters = [] # empty 'letters' list 

    letters = random.sample(LETTER_LIST,10) #10 letters are randomly selected and set to the letters list
    
    return letters #returns 10 randomly selected letters 

def uses_available_letters(word, letter_bank):

    #loops through all the letters in the words and makes them lowercase strings in a new list
    word_case_insensitive =  []
    for i in word:
        word_case_insensitive.append(i.lower())

    #loops through all the letters in the letter bank and makes them lowercase strings in a new list
    letter_bank_case_insensitive = []
    for i in letter_bank:
        letter_bank_case_insensitive.append(i.lower())

    #counter for how many loops are completed
    loop_count = 0

    #for-loop that compares each item in both lists, and removes from letter bank if there's a match
    for i in word_case_insensitive:
        for j in letter_bank_case_insensitive:
            if i == j:
                loop_count += 1
                letter_bank_case_insensitive.remove(j)

    #if the loop count and length of a word are equal, it returns True and else False
    if loop_count == len(word):
        return True
    else:
        return False
        
            


def score_word(word):
    #lists of scores grouped by number of points. Upper and lower are included to cover all bases (even though it might be not needed since the letters in the word are turned into lowercase)
    score_1 = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'L', 'l','N', 'n', 'R', 'r', 'S','s', 'T','t']
    score_2 = ['D', 'd', 'G', 'g']
    score_3 = ['B', 'b', 'C', 'c', 'M', 'm','P', 'p']
    score_4 = ['F', 'f', 'H', 'h', 'V', 'v', 'W', 'w','Y', 'y']
    score_5 = ['K', 'k']
    score_8 = ['J','j','X', 'x']
    score_10 = ['Q', 'q','Z', 'z']

    # Loops through all the letters in the word variable and makes them lowercase strings in a new list
    word_ =  []
    for i in word:
        word_.append(i.lower())
    
    #variable is set and intalied to 0 to keep score
    score = 0
    #for each letter in 'word_' variable, if its in one of the lists it will add to the score accordingly 
    for i in word_: 
        if i in score_1:
            score += 1
        elif i in score_2:
            score += 2
        elif i in score_3:
            score += 3  
        elif i in score_4:
            score += 4
        elif i in score_5:
            score += 5
        elif i in score_8:
            score += 8
        elif i in score_10:
            score += 10
    
    #if the length of the word is in between (and including) 7 or 10, it will add 8 points to the score total
    if len(word_) <= 10 and len(word_) >= 7:
        score += 8

    #returns final score
    return score
        

def get_highest_word_score(word_list):
    #word list is converted into tuple pairs. First is the word, second is the score called in from the score_word function for the word
    tuple_list = []
    for i in word_list:
        tuple_list.append((i, score_word(i)))

    #a new vairable is set to the sorted list of tuple_list, in decreasing order of the scores (highest to lowest)
    highest_score_tuple_list = sorted(tuple_list, key=lambda t: t[1], reverse = True)

    #a variable set to the first item's second element for highest score as just an integer 
    highest_score = highest_score_tuple_list[0][1]
    
    #this helps group all the tuples that are tied by adding them to a new list if theyre equal to the highest score
    tuples_list_tied_scores_only = []
    for i in highest_score_tuple_list:
        if i[1] == highest_score:
            tuples_list_tied_scores_only.append(i)

    #this sorts the tied tuples by length of the first item (the word) from shortest to longest             
    tied_tuples_by_word_length = sorted(tuples_list_tied_scores_only, key=lambda x: len(x[0]))

    #this creates a new list of added winning tuples by comparing it to the orginal order  
    tuple_list_original_order = []
    for i in tuple_list:
        if i in tied_tuples_by_word_length:
            tuple_list_original_order.append(i)

    #
    best_word_list_over_ten = []
    for i in tuple_list_original_order:
        if len(i[0]) == 10:
            best_word_list_over_ten.append(i)

    if len(tuple_list_original_order) == 1:
        best_word = tuple_list_original_order[0]
    elif len(best_word_list_over_ten) > 0:
        best_word = best_word_list_over_ten[0]
    else:
        best_word = tied_tuples_by_word_length[0]
    

    return best_word
    

    