import random
#dictionary with the letters as keys and the allowed amount as values
LETTERS_ALPHABET = {
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
#helper function to get a random letter from LETTERS_ALPHABET dictionary
def random_selected_letter():
    letters_alphabet = list(LETTERS_ALPHABET.keys())
    #randint() is part of random library and random_index will return a random index between 0 and the higher limit in the length of letters_alphabet list
    #every time we use this function it will retrieve a random index number
    random_index = random.randint(0, len(letters_alphabet)-1)
    #we'll use that random_index to retrieve the element (letter) that is in that position in the list
    random_letter = letters_alphabet[random_index]

    return random_letter

def draw_letters():
    #hand variable will storage all the 10 random letters
    hand = []
    random_letter = ""

    #while loop to loop through both lists letters_alphabet and LETTERS_MAX_ALLOWED to make
    # sure we don't use more than the maximun amount allowed per letter
    # while loop stops when we have 10 letters appended  
    while len(hand) < 10:
        random_letter= random_selected_letter()
        if hand.count(random_letter) < LETTERS_ALPHABET[random_letter]:
            hand.append(random_letter)

    return hand

#helper function to convert a string or list into a dictionary with the amount of times that element appears
#as it value
def word_letter_dictionaries(data_to_convert):
    dict_convert = {}

    for elem in data_to_convert:
        if elem in dict_convert:
            dict_convert[elem] +=1
        else:
            dict_convert[elem]= 1
    return dict_convert
    
def uses_available_letters(word, letter_bank):
    #valid variable to check whether the letter is in letter_bank or not
    valid = False
    word_upper = word.upper()
    #dict_word and dict_letter_bank store a dictionary with each letter as key and the amount of that that letter
    #appears as value
    dict_word = word_letter_dictionaries(word_upper)
    dict_letter_bank = word_letter_dictionaries(letter_bank)
    #for loop to loop through dict_word  and check whether the letters are in dict_letter_bank
    #or not and in case the amount of that letter exceeds the amount in dict_letter_bank it returns False
    for elem in dict_word:
        if elem not in letter_bank or dict_word[elem] > dict_letter_bank[elem]:
            valid = False
            break
        else:
            valid = True

    return valid

def score_word(word):
    #create dict_score to store letters that shares the same point value
    dict_score = {1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
                  2: ["D", "G"],
                  3: ["B", "C", "M", "P"],
                  4: ["F", "H", "V", "W", "Y"],
                  5: ["K"],
                  8: ["J", "X"],
                  10: ["Q", "Z"]}
    #score variable to store the points earned
    result = 0
    #word_upper_case variable converts word variable elements into uppercase letters
    word_upper = word.upper()
    #for to loop through the elements in word_upper to give the right points per letter
    for letter in word_upper:
        for score, letters in dict_score.items():
            if letter in letters:
                result += score
            
    #if word has 7, 8, 9 or 10 letters the word gets 8 additional points
    if len(word) >= 7 and len(word)<= 10:
        result += 8
        
    return result

def get_highest_word_score(word_list):
    #tuple to store the word with the high score
    high_score_tuple = ()
    #dictionary to store all the words with their score
    score_dict = {}
    score = 0
    #append every word with its score in the dictionary
    for word in word_list:
        score = score_word(word)
        score_dict[word]= score
    
    #get the word with the maximun score in score_dict
    word_high_score = max(score_dict)
    #get the word with the maximun score in score_dict
    value_high_score = max(score_dict.values())
    # list to store every word that share the same maximum score
    list_high_word = []
    
    #append the words that share the same store into list_high_word
    for key, value in score_dict.items():
        if value == value_high_score:
            list_high_word.append(key)
    
    #loop through list_high_word to get the word and value that should be stored in high_score_tuple
    for word in list_high_word:
        if len(word) == 10 and high_score_tuple == ():
            high_score_tuple = (word, value_high_score)
        elif len(word) == 10 and len(word) > len(high_score_tuple[0]):
            high_score_tuple = (word, value_high_score)
        elif len(word) < len(word_high_score) and high_score_tuple == ():
            high_score_tuple = (word, value_high_score)
        elif word == word_high_score and high_score_tuple == ():
            high_score_tuple = (word, value_high_score)

              
    return high_score_tuple