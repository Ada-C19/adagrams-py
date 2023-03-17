import random
letter_set1 = ["A","I"]* 9
letter_set2 = ["B","C","F","H","M","P","V","W","Y"] * 2
letter_set3 = ["D","L","S","U"] * 4
letter_set4 = ["E"] * 12
letter_set5 = ["G"] * 3
letter_set6 = ["J","K","Q","X","Z"]
letter_set7 = ["N","R","T"] * 6
letter_set8 = ["O"]* 8
letters_list = letter_set1 + letter_set2 + letter_set3 + letter_set4\
               + letter_set5 + letter_set6 + letter_set7 + letter_set8
def draw_letters():
   
   letter_hand = random.sample(letters_list, 10)
   return letter_hand
   
def uses_available_letters(word, letter_bank):
   
   
   for char in word:
       
       if char.upper() in letter_bank:
           
           letter_bank.remove(char.upper())
           return True
       else:
           return False
       


   return Flag
           
           
def score_word(word):
    pass

def get_highest_word_score(word_list):
    
    pass
