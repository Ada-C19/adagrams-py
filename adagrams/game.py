import random
LETTER_POOL = {
    'A' : 9,	
    'B' : 2,	
    'C' : 2,	
    'D' : 4,	
    'E' : 12,	
    'F' : 2,	
    'G' : 3,	
    'H' : 2,	
    'I' : 9,	
    'J' : 1,	
    'K' : 1,	
    'L' : 4,	
    'M' : 2,
    'N' : 6,
    'O' : 8,
    'P' : 2,
    'Q' : 1,
    'R' : 6,
    'S' : 4,
    'T' : 6,
    'U' : 4,
    'V' : 2,
    'W' : 2,
    'X' : 1,
    'Y' : 2,
    'Z' : 1
}
def draw_letters():
    hand = []
    for key in LETTER_POOL:
        #For each key, the loop runs a nested for loop that adds the letter key to the hand list the number of times specified by the value.
        for i in range(LETTER_POOL[key]):
            hand.append(key)
    #Once all the letters are added to the hand list, the list is shuffled
    random.shuffle(hand)
    #first 10 elements in the list are returned
    return hand[:10]

def uses_available_letters(word, letter_bank):
    letters = letter_bank[:]
    #loop through all the letters in the word, .upper() returns a string where all characters are in upper case
    for letter in word.upper():
        if letter not in letters:
            return False
        else:
            #removes the letter from the 'letters' list and continue looping
            letters.remove(letter)
    #If all the letters in the word are present in the letter_bank list, return True
    return True

def score_word(word):
    #set initial value of score to zero
    score = 0
    #use the .upper() function to make word upper case
    word = word.upper()
    for letter in word:
        if letter in "AEIOULNRST":
            score += 1
        elif letter in "DG":
            score += 2
        elif letter in "BCMP":
            score += 3
        elif letter in "FHVWY":
            score += 4
        elif letter == "K":
            score += 5
        elif letter in "JX":
            score += 8
        elif letter in "QZ":
            score += 10
    #check the length of the word and add 8 points if the word is between 7 and 10 characters in length. Not sure if checking upper limit length of word is necessary...
    if len(word) >= 7 and len(word) <= 10:
        score += 8

    return score

def get_highest_word_score(word_list):
    #"highest_score" and "winning_word_len" is set to 0 and "winning_word" is set to an empty string
    highest_score = 0
    winning_word = ""
    winning_word_len = 0
    #A for loop is used to iterate through the list of words in "word_list"
    for word in word_list:
        #The score for each word is calculated using the "score_word" function
        score = score_word(word)
        #The length of the word is stored in the variable "word_len"
        word_len = len(word)
        #If the current word's score is greater than the highest score 
        if score > highest_score:
            #it is set to the new highest score
            highest_score = score
            #the word and its length are stored in "winning_word"
            winning_word = word
            #and winning_word_len
            winning_word_len = word_len
        #If the current word's score is equal to the highest score, then  . .
        elif score == highest_score: 
            #a check is done to see if the "winning_word_len" is not equal to 10 and if the current word's length is either equal to 10 or less than the "winning_word_len"
            if winning_word_len != 10 and (word_len == 10 or word_len < winning_word_len):
                #If this is true, then the new winning word and its length are stored in their respective variables
                winning_word = word
                winning_word_len = word_len
    
    return (winning_word, highest_score)
    #return winning word and high score in a tuple

