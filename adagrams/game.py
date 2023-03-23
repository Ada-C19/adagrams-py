import random 

# pool_of_letters_amount = [
#     {"A": 9}, {"B": 2}, {"C": 2}, {"D": 4}, {"E": 1}, {"F": 2}, {"G": 3}, {"H": 2}, {"I": 9}, {"J": 1}, {"K": 1}, {"L": 4}, {"M": 2}, 
#     {"N": 6}, {"O": 8}, {"P": 2}, {"Q": 1}, {"R": 6}, {"S": 4}, {"T": 6}, {"U": 4}, {"V": 2}, {"W": 2}, {"X": 1}, {"Y": 2}, {"Z": 1}, 
# ]

# pool_of_letters_score = [
#     {"A": 1},{"B": 3},{"C": 3},{"D": 2},{"E": 1},{"F": 4},{"G": 2},{"H": 4}, {"I": 1},{"J": 8},{"K": 5},{"L": 1},{"M": 3},
#     {"N": 1},{"O": 1},{"P": 3},{"Q": 1},{"R": 1},{"S": 1},{"T": 1},{"U": 1},{"V": 4},{"W": 4}, {"X": 8},{"Y": 4},{"Z": 1},
# ]

pool_of_letters = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", "D", "D", "D", "E", "E", "E", "E", "E", 
                "E", "E", "E", "E", "E", "E", "E", "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I", "I", 
                "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", "N", "O", "O", "O", "O", "O", "O", "O", 
                "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", "U", 
                "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z"]

#####WAVE_1_FUNCTION#####
def draw_letters():
    
    letters_drawn = 0
    hand_of_letters = []
    while len(hand_of_letters) < 10:
        copied_pool_of_letters = pool_of_letters.copy()
        new_letter = random.choice(copied_pool_of_letters)
        hand_of_letters.append(new_letter)
        copied_pool_of_letters.remove(new_letter)
        letters_drawn += 1
    return hand_of_letters




draw_letters()
#####DON'T_TOUCH!!!#####

#testing if these are the same files 


letter_bank = draw_letters()
# print (letter_bank)
# word = input("What word do you pick?")

def uses_available_letters(word, letter_bank):
    print (letter_bank)
    for letter in word:
        print (letter)
        if letter not in letter_bank:
            print ("False")
            return False
        else: 
            letter_bank.remove(letter)
    #         print (letter_bank)
    # print ("True")
    # return True
        

uses_available_letters("AAA", ["A", "X", "X", "X", "X", "X", "X", "X", "X", "X"])





def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass