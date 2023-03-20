import random 
letter_dic={
'A':9, 'B':2, 'C':2, 'D':4, 'E':12, 'F':2, 'G':3, 'H':2, 'I':9, 'J':1, 'K':1, 'L':4, 'M':2, 'N':6, 'O':8, 'P':2, 'Q':1, 'R':6, 'S':4, 'T':6, 'U':4, 'V':2, 'W':2, 'X':1,'Y':2, 'Z':1
}
def make_list():

    #Inputs:Dicionary with letters (l) as keys and a number as the value (n)
    #Outputs:List with n number of l letters  

    list_of_letters=[]

    for letter in letter_dic.keys():
        for ratio in range(letter_dic[letter]):
            list_of_letters.append(letter)

    return list_of_letters


def draw_letters():
    #Inputs:List with letter pool
    #Outputs: Hand of 10 letters randomly choosen 
    letter_pool= make_list()
    letter_choices=random.sample(letter_pool,k=10)
    return letter_choices

def uses_available_letters(word, letter_bank):
    #Inputs:Word-string with letters  letter_bank- array of letters
    #Outputs:Boolean stating if the letters used for the word are contained in list letter bank

    available_letters= letter_bank.copy()
    for letter in word.upper(): 
        print (letter)
        if letter in available_letters: 
            available_letters.remove(letter)
            continue
        else: 
            return False
    return True 

def score_word(word):

    #input: word-string of cheracters
    #output: int with points scored  
    value_of_letters_dic={1:['A','E','I','O','U','L','N','R','S','T'],2:['D','G'],3:['B','C','M','P'],4:['F','H','V','W','Y'],5:['K'],8:['J','X'],10:['Q','Z']}
    if len(word)>=7:
        total_score = 8 
    else:
        total_score =0
    for letter in word:
        for score in value_of_letters_dic.keys():
                if letter.upper() in value_of_letters_dic[score]:
                    total_score+=score
                    break
    return total_score

def get_highest_word_score(word_list):
    #input: word_list - list with string of words 
    #Output: winner_tuple- winner word string, score of word (int)
    winner_score= 0
    winner_word= " "


    for word in word_list:
        score=score_word(word)


        if score > winner_score:
            winner_score=score
            winner_word=word


        #Tie Breaker
        if score == winner_score:

            #find shortes word
            if len(word)<len(winner_word) and len(winner_word)!=10:
                winner_score=score
                winner_word=word

            #choose 10 letter word in tie
            #If current word is not 10 letters
            if len(word)==10 and len(winner_word)<10:
                winner_score=score
                winner_word=word   

            
    return (winner_word,winner_score)
