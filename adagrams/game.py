import random

#in letter out qty
letter_bank = {
"A" : 9,	
"B" : 2,
"C" : 2,	
"D" : 4,	
"E" : 12,	
"F" : 2,	
"G" : 3,	
"H" : 2,	
"I" : 9,
"J" : 1,	
"K" : 1,	
"L" : 4,
"M" : 2,
"O": 8,
"P": 2,
"Q": 1,
"R": 6,
"S": 4,
"T": 6,
"U": 4,
"V": 2,
"W": 2,
"X": 1,
"Y": 2,
"Z": 1,
}

def draw_letters():
    #each letter in the list appears as many times as its value 
    letters = []
    #count/value - how many the letter should appear
    #letter/key
    for letter, count in letter_bank.items():
        #adds to end by amount of value
        letters.extend([letter] * count)
    random.shuffle(letters)
    hand = letters[:10]
    return hand

print(draw_letters())

"""
check in any input word (word player sumbits) only uses characters
that are in the hand.
check to see if the word is an anagram
word - describes some input word, is a string
letter_bank array of drawn letters in hand. an array of 1- strings, ea string is a letter
returns as boleon, true or false
true if every letter in the input word is available (in right qty)
in letter bank
false if there is a letter not in input. not in letterbank or
too much compared to letterbank

"""
def uses_available_letters(word, letter_bank):
   
    word = word.upper()
    #create a copy of the letter bank so that we can modify it
    letter_bank_copy = list(letter_bank)
    #loop over each letter in the word
    for letter in word:
        #if the letter is not in letter bank, return False
        if letter not in letter_bank_copy:
            return False
        #if the letter is in letter bank, remove it from copy
        letter_bank_copy.remove(letter)
    # if we got here, then every letter in the word is available in the letter bank
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass