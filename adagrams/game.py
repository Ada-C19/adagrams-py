
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

VALUE_SCORES = {
'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
'D': 2, 'G': 2,
'B': 3, 'C': 3, 'M': 3, 'P': 3,
'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
'K': 5,
'J': 8, 'X': 8,
'Q':10, 'Z':10
}


 #WAVE 1
def draw_letters():
    #pass
    #no parameters
   
    #return an array of 10 strings
    # array is a list, return list of 10 strings
    drawn_letters = []
    available_letters = []

    #each string should contain exactly one letter
    #these represent the hand of letters that the player has drawn
    # LETTER_POOL is a dict - letter, num is key, value
    #.items returns each item in a dict as tuples in a list
    for letter, num in LETTER_POOL.items():
        for i in range(num):
            available_letters.append(letter)
            

    # letters should be randomly drawn from a pool of letters
    # letter pool should reflect the distribution of letters
    # make sure the drawn letters match the rules of the letter pool
    # while length of drawn letters from pool of letters is <= 10 is True
    while len(drawn_letters) < 10:
        # draw random letter from available_letters
        # use import random to use random() which returns random float between
        # 0 and 1
        # use choice() returns a random element from the given sequence
        randomly_draw_letter = random.choice(available_letters)
        available_letters.remove(randomly_draw_letter)
        # print random drawn letter to reflect the distribution of letters
        #print(randomly_draw_letter)
        drawn_letters.append(randomly_draw_letter)
        #build a data sturcture for the letter pool
    #there are only 2 available C letters
        #draw letters cannot return more than 2 C's
    #there are 12 E's but only one Z
        #should be 12 times as likely to draw a E as a Z
    #invoking this function should NOT change the pool of letters
        #imagine user returns their hand to the pool before drawing new letterss
    return drawn_letters



#terminal vs code wave one success! -- terminal wave one success!

#WAVE 2
def uses_available_letters(word, letter_bank):
    #pass
    #letter bank describes an array of drawn letters in a hand
    for letter in list(word.upper()):
        # set is a dict unordered duplicates not allowed 
    #     #check if an input word only uses characters that are within a 
    # hand of drawn cards

    #     # word describes some input word, and is a string
        #if letter in letter_bank:  
        if word.upper().count(letter) > letter_bank.count(letter):
            return False
    #     # return False if not; if there is a letter in input that is not present in the letter_bank
            #letter_bank.remove(letter)
    # #return True if every letter in the input word is available in the letter_bank
    return True

# there should be a .lower() or .upper() but doesn't work :()

#WAVE 3
#has one parameter word
def score_word(word):
    # each letter within word has point value.
    #number of points of each letter is summed up to rep the total score of word
    # each letter's point value is described in VALUE_SCORES
    score = sum(VALUE_SCORES.get(letter.upper(), 0) for letter in word)
    #if the len of the word is 7,8,9,10 
    if len(word) in [7, 8, 9, 10]:
        # then the word gets an addtl 8 points
        score += 8
    #returns int rep number of points
    return score

#terminal vs code wave three success! -- terminal wave three success!

def get_highest_word_score(word_list):

    max_score = 0
    #find highest scoring word
    max_word = ''
    for word in word_list:
    # list of word list - one parameter - list of strings
        word_score = score_word(word)
        # calculates which of these words has the highest score, applies any ties
        if word_score > max_score:
            max_score = word_score
            max_word = word
        elif word_score == max_score:
            # for tie breaking rules - prefer the word with the fewest letters
            # unless one word has 10 letters, if top score is tied with 10 letters
            # over the one with fewer tiles
            #if there are multiple words that are the same score and the same length
            #pick the first one in the supplied list
            if len(word) < len(max_word) or (len(word) == len(max_word) 
            and len(word) == 10):
                max_word = word
    # returns the winning word in a special data stucture
    # returns a tuple that rep the data of winning word and it's score
    return (max_word, max_score)

# going home now :() hopefully clear test later today