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

def uses_available_letters(word, letter_bank):
    #valid variable to check whether the letter is in letter_bank or not
    valid = False
    #new list to store all elements in letter_bank but ignoring case
    letters_ignore_case = []
    #for loop to append every element from letter_bank into letter_ignore_case but ignoring case
    for letter in letter_bank:
        letters_ignore_case.append(letter.casefold())
    #variable to store string from word variable but ignoring case
    word_ignore_case = word.casefold()
    #for loop to loop through word_ignore_case string and check whether the letters are in letter_ignore_case
    #or not and in case the quantity of that letter exceeds the quantity in the list it returns False
    for elem in word_ignore_case:
        if elem in letters_ignore_case and word_ignore_case.count(elem) <= letters_ignore_case.count(elem):
            valid = True
        else:
            valid = False
            
    return valid

def score_word(word):
    #create lists storing letters that shares the same point value
    list_score1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    list_score2 = ["D", "G"]
    list_score3 = ["B", "C", "M", "P"]
    list_score4 = ["F", "H", "V", "W", "Y"]
    list_score5 = ["K"]
    list_score8 = ["J", "X"]
    list_score10 = ["Q", "Z"]
    
    #score variable to store the points earned
    score = 0
    #word_upper_case variable converts word variable elements into uppercase letters
    word_upper_case = word.upper()
    #for to loop through the elements in word_upper_case to give the right points per letter
    for letter in word_upper_case:
        if letter in list_score1:
            score += 1
        elif letter in list_score2:
            score += 2
        elif letter in list_score3:
            score += 3
        elif letter in list_score4:
            score += 4
        elif letter in list_score5:
            score += 5
        elif letter in list_score8:
            score += 8
        elif letter in list_score10:
            score += 10
    
    #if word has 7, 8, 9 or 10 letters the word gets 8 additional points
    if len(word) >= 7 and len(word)<= 10:
        score += 8
        
    return score

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