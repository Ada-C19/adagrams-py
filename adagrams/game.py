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
    #Outputs:
    letter_pool= make_list()
    letter_choices=random.sample(letter_pool,k=10)
    return letter_choices

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass