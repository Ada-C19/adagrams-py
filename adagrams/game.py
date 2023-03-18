import string
import random
#list of letters in the alphabet that we're allowed to use
LETTERS_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#list of maximum amount allowed per letter in LETTERS_ALPHABET
LETTERS_MAX_ALLOWED = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
def draw_letters():
    #hand variable will storage all the 10 random letters
    hand = []
    random_letter = ""
    letters_alphabet = LETTERS_ALPHABET

    #cant_letter is a counter to make sure we don't exceed the maximum allowed per letter
    cant_letter = 0

    #while loop to loop through both lists letters_alphabet and LETTERS_MAX_ALLOWED to make
    # sure we don't use more than the maximun amount allowed per letter
    # while loop stops when we have 10 letters appended  
    while len(hand) < 10:
        random_letter = random.choice(list(letters_alphabet))
        for i in range(len(letters_alphabet)):
            if letters_alphabet[i] == random_letter and cant_letter < LETTERS_MAX_ALLOWED[i]:
                hand.append(random_letter)
                cant_letter += 1

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
    pass