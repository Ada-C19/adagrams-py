#FIRST VERSION OF ADAGRAMS (I know this one works lol)

import random 
# key = letter
# value = [weight, score]
LETTER_DICT = {
    'A': [9, 1],
    'B': [2, 3], 
    'C': [2, 3],
    'D': [4, 2],
    'E': [12, 1],
    'F': [2, 4],
    'G': [3, 2], 
    'H': [2, 4],
    'I': [9, 1],
    'J': [1, 8],
    'K': [1, 5], 
    'L': [4, 1],
    'M': [2, 3], 
    'N': [6, 1],
    'O': [8, 1], 
    'P': [2, 3],
    'Q': [1, 10], 
    'R': [6, 1],
    'S': [4, 1],
    'T': [6, 1],
    'U': [4, 1],
    'V': [2, 4],
    'W': [2, 4],
    'X': [1, 8], 
    'Y': [2, 4],
    'Z': [1, 10]
}


def build_letter_pool():
    letter_pool = []
    letter_nested_list = []

    for letter,weight in LETTER_DICT.items():
        letter_nested_list.append([letter]* LETTER_DICT[letter][0])    
    LETTER_POOL = sum(letter_nested_list,[])
    
    return LETTER_POOL

LETTER_POOL = build_letter_pool()

def draw_letters():
    
    letters = random.sample(LETTER_POOL, k = 10)
    
    return letters 

# inputs word and letter bank and checks to see if letters in word are in letter bank + for correct amount of times
def uses_available_letters(word, letter_bank):
    outcome = True
    
    #converts all letter cases to upper
    upper_word = word.upper()

    #checks for letter in word
    for letter in upper_word:
        if letter in letter_bank and upper_word.count(letter) <= letter_bank.count(letter):
            outcome = True
        else:
            outcome = False

    return outcome

#input word, output score of word
def score_word(word):
    sum = 0
    upper_word = word.upper()
    
    # loops through word to add points together
    #create new data structure with letters and their score values 
    for letter in upper_word:
        sum += LETTER_DICT[letter][1]
        
    # adds 8 additional points if word is longer than 7
    # ** needs to have a cut off past 10 **
    if len(upper_word) >= 7 and len(upper_word) < 11:
        
        sum = 8 + sum
    return sum

# inputs list of words, outputs tuple --> (best word out of list, that word's score)
def get_highest_word_score(word_list):
    winning_word = ()
    word_score_dict = {}

    #creates a dictionary that contains the words guessed and their scores
    for word in word_list: 
        word_score_dict[word] = score_word(word)
    
    #finds the highest
    high_score = max(word_score_dict.values())
    
    #if there is only one high score in the dictionary, that word is the winner
    if list(word_score_dict.values()).count(high_score) == 1:
        winning_word = max(word_score_dict.items())
    
    #otherwise, use get_all_high_score_words function to
    #get a dictionary of all guesses with max score + their lengths
    else: 
        high_score_words = get_all_high_score_words(word_score_dict)
        
        #loops through words and their lengths
        for word,length in high_score_words.items():
            
            #initalize varibles with the shortest/longest word among dict
            shortest_word_length = min(high_score_words.values())
            longest_word_length = max(high_score_words.values())
            
            #if there is a letter longer than 10 characters, 
            # and it is the current word in the loop, 
            # that is the winning word
            if longest_word_length >= 10:
                if length >= 10:
                    winning_word = word, high_score
                    break
            
            #if we are on the first instance of the shortest word,
            #that word is the winner
            elif length == shortest_word_length:
                winning_word = word, high_score
                break
    print(winning_word)
    return winning_word

#input: dictionary of all words guess and their scores, 
#outputs: dictionary of the words with the max score and their lengths
def get_all_high_score_words(word_score_dict):  
    #calculates the max score out of all the guesses
    high_score = max(word_score_dict.values())
    #initialize dictionary of words + lengths
    high_score_words = {}

    #loops through word score dictionary
    for word, score in word_score_dict.items():
        #if the score for that word is equal to high score, add it to high_score_words dict
        if score == high_score:
            high_score_words[word] = len(word)

    return high_score_words

words = ["XXX","JJJ"]
get_highest_word_score(words)