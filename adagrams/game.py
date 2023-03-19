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
letter_score_dict ={}
for letter in ["A", "E", "I", "O", "U","L", "N", "R","S","T"]:
    letter_score_dict[letter] = 1
dict_items = {"D":2,"G":2,"K":5,"J":8,"X":8,"Q":10,"Z":10}
letter_score_dict.update(dict_items)
for letter in ["B", "C", "M", "P"]:
    letter_score_dict[letter]= 3
for letter in ["F", "H", "V", "W", "Y"]:
    letter_score_dict[letter]= 4
def draw_letters():
   
   letter_hand = random.sample(letters_list, 10)
   return letter_hand
   
def uses_available_letters(word, letter_bank):
   flag = True
   letter_bank_copy = letter_bank.copy()
   
   for char in word:
       
       if char.upper() in letter_bank_copy:
           
           letter_bank_copy.pop(letter_bank_copy.index(char.upper()))
           
       else:
           flag = False
       


   return flag
           
           
def score_word(word):
    score = 0
    for char in word:
        score += letter_score_dict[char.upper()]
    if len(word) >= 7:
        score += 8

    return score

def get_highest_word_score(word_list):
    
    pass
