# Import random module to use later
import random


#  Dictionary:
#   keys - letters of the alphabet
#    values - quantity of available letters for the game
letter_dic={
'A':9, 'B':2, 'C':2, 'D':4, 'E':12, 'F':2, 'G':3, 'H':2, 'I':9, 'J':1, 'K':1, 'L':4, 'M':2, 'N':6, 'O':8, 'P':2, 'Q':1, 'R':6, 'S':4, 'T':6, 'U':4, 'V':2, 'W':2, 'X':1,'Y':2, 'Z':1
}



#Helper function that creates letter pool for game

def make_list():
    #Inputs:Dicionary with (l)letters as keys and ints (n) as values
    #Outputs:List with n number of l letters  

    list_of_letters=[]

    for letter in letter_dic.keys():
        for number_of_letters in range(letter_dic[letter]):
            list_of_letters.append(letter)


    return list_of_letters




#Selects 10 random letters from pool
def draw_letters():
    #Inputs:List with letter pool
    #Outputs: Hand of 10 letters randomly choosen 

    letter_pool= make_list()
    letter_choices=random.sample(letter_pool,k=10)


    return letter_choices


#Checks to see if the word uses only the available letters in letter bank
#   and in the correct amounts  

def uses_available_letters(word, letter_bank):
    #Inputs:   Word-string  &  letter_bank- list of letters
    #Outputs:Boolean stating if the letters in word are contained in list (letter bank)

    available_letters= letter_bank.copy()

    for letter in word.upper(): 

        if letter in available_letters: 
            available_letters.remove(letter)
            continue
        else: 
            return False
        

    return True 



#Generates the score given to the word acording to the stated rules 
def score_word(word):

    #input: word-string of cheracters
    #output: int with points scored  

    #Dictionary to find score
        #key: int (n) points given per letter 
        #value: list of letters that give you n points 
    value_of_letters_dic={1:['A','E','I','O','U','L','N','R','S','T'],2:['D','G'],3:['B','C','M','P'],4:['F','H','V','W','Y'],5:['K'],8:['J','X'],10:['Q','Z']}
    
    #8 poitns given for words with more than 7 letters 
    if len(word)>=7:
        total_score = 8 
    else:
        total_score =0


#   Iterates over each letter in the word, then it iterates over the dic
#       each time to find the letter and its score key

    for letter in word:
        for score in value_of_letters_dic.keys():
                if letter.upper() in value_of_letters_dic[score]:
                    total_score+=score
                    break


    return total_score





#Finds the word with the highest score acording to game rules 
def get_highest_word_score(word_list):
    #input: word_list - list with string of words 
    #Output: winner_tuple- winner word string, score of word (int)

    #Variables to hold current highest score and current winner word
    winner_score= 0
    winner_word= " "


    for word in word_list:
        score=score_word(word)

        #Checks to see if the current word scores higher than all the past 
        if score > winner_score:
            winner_score=score
            winner_word=word


        #Tie Breaker
        if score == winner_score:


            #find shortes word
            if len(winner_word)!=10:

                if len(word)<len(winner_word):
                    winner_score=score
                    winner_word=word

            #Choose 10 letter word in tie
            #If current winner word is not 10 letters
            if len(word)==10 and len(winner_word)<10:
                winner_score=score
                winner_word=word   

            
    return (winner_word,winner_score)
