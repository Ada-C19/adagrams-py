import random
def draw_letters():
    #Goal: returns array/list of 10 strings
    
    #build letter pool in the form of a dictionary
    letter_pool = {"A":9, "B":2, "C":2, "D":4, "E":12, "F":2, "G":3, "H":2, "I":9, "J":1, "K":1, "L":4,"M":2, "N":6, "O":8, "P":2, "Q":1, "R":6, "S":4, "T":6, "U":4, "V":2, "W":2, "X":1, "Y":2,"Z":1}
    #create empty list for hand
    hand = []

    #loop thru a for-loop 10 times to get 10 letters from letter pool:
    #adapted from https://stackoverflow.com/questions/69119270/randomly-selecting-a-word-from-a-dictionary-with-a-given-probability
    for i in range(10):
        #draw each letter randomly based on each letter's probability with replacement
        next_letter = random.choices(list(letter_pool.keys()),weights=list(letter_pool.values()),k = 1) [0]
        #add each letter drawn to hand list
        hand.append(next_letter)
        #print(hand) #verify
        #if the frequency of the next letter drawn exceeds the frequency of that letter in the letter_pool, then...
        if hand.count(next_letter) > letter_pool[next_letter]:
            #...remove that letter from both the letter_pool and hand so it can't be drawn again
            letter_pool.pop(next_letter)
            hand.remove(next_letter)

    #return hand of letters drawn
    return hand
    #print(hand) #verify
        
def uses_available_letters(word, letter_bank):
    #Goal: returns either True or False
    
    #turn all characters in word into upper case like those in letter_bank
    word = word.upper()
                
    #loop thru each character in word                                                
    for char in word:
        #return False for the word if the frequency of character in word is > the frequency of
        #that same character in letter_bank
        if word.count(char) > letter_bank.count(char):
            return False
    #otherwise, return True for the word
    return True

def score_word(word):
    #Goal: returns total score of a word
    
    #turn all characters in word into upper case like those in letter_bank
    word = word.upper()
    #build score chart as a dictionary
    score_chart = {("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"):1, ("D","G"):2, ("B", "C", "M", "P"):3, ("F", "H", "V", "W", "Y"):4, "K":5, ("J", "X"):8, ("Q", "Z"):10} 
    
    #initialize total score variable
    score = 0
    #loop thru each character in word
    for char in word:
        #loop thru each key in score_chart dict
        for key in score_chart:
            #if length of key is > 1. In other words, if there's > 1 letter for a point value...
            if len(key) > 1:
                #...then loop thru each letter in said key
                for letter in key:
                    #if character in word matches said letter...
                    if char == letter:
                        #...then add corresponding point value to word's score
                        score += score_chart[key]
            #if length of key is 1. In other words, if there's only 1 letter for a point value...            
            else:
                #...and if character in word matches said letter...
                if char == key:
                    #...then add corresponding point value to word's score
                    score += score_chart[key]
                    
    #if the word is greater than 6 characters...
    if len(word) > 6:
        #...then add additional 8 pts to word's score
        score += 8
    
    #return total score for word
    return score   

                

def get_highest_word_score(word_list):
    #Goal: returns tuple containing winning word and highest score
    # in the case of tie in scores, use these tie-breaking rules:
    # prefer the word with the fewest letters...
    # ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
    # If there are multiple words that are the same score and the same length, pick the first one in the supplied list
    
    #initialize winning_words_list list and word_score_dict dictionary
    winning_words_list = []
    word_score_dict = {}
    #loop thru each word in list of words
    for word in word_list:
        #invoke function score_word to calculate score of each word looped thru
        score = score_word(word)
        #populate word_score_dict dictionary with word:score pairs
        word_score_dict[word] = score
    #get the word or words with the highest score from the dict and store in string_with_highest_score variable
    string_with_highest_score = max(word_score_dict, key=word_score_dict.get)
    #get the highest score from the dict
    highest_score = word_score_dict[string_with_highest_score]
    #print(highest_score) #verify
    #loop thru dict
    for key, value in word_score_dict.items():
        #if score is equal to the highest score, then add word from dict to winning_words_list to get list of highest-scoring words
        if value == highest_score:
            winning_words_list.append(key)

    #print(winning_words_list) #verify
    
    #if there's only 1 highest-scoring word, then return such word w/ score
    if len(winning_words_list) == 1:
        #print(winning_words_list[0])
        return winning_words_list[0], score_word(winning_words_list[0])
    #if there're > 1 highest-scoring words, then...
    else:
        #...look thru list of highest-scoring words, find the first word w/ 10 letters
        winning_word_with_ten_letters = next((word for word in winning_words_list if len(word) == 10), None)
        #if there's such a 10-letter word, then return it w/ score
        if winning_word_with_ten_letters != None:
            #print(winning_word_with_ten_letters) #verify
            return winning_word_with_ten_letters, score_word(winning_word_with_ten_letters)
        #if there're no 10-letter words, then...
        else:
            #get the shortest word in list of highest-scoring words
            shortest_word = (min(winning_words_list, key=len))
            #get length of this shortest word to determine what the smallest number of letters is
            shortest_word_len = len(shortest_word)
            #look thru list, find the first word w/ the smallest number of letters
            winning_word = next(word for word in winning_words_list if len(word) == shortest_word_len)
            #print(winning_word) #verify
            #return first word w/ smallest number of letters along w/ score
            return winning_word, score_word(winning_word)
            