import random 
import copy

letter_pool_frequency = {
    "A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, 
    "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1, 
}

# print (letter_pool_frequency["A"]) --> 9

letter_pool_score = {
    "A": 1,"B": 3,"C": 3,"D": 2,"E": 1,"F": 4,"G": 2,"H": 4,"I": 1,"J": 8,"K": 5,"L": 1,"M": 3,
    "N": 1,"O": 1,"P": 3,"Q": 1,"R": 1,"S": 1,"T": 1,"U": 1,"V": 4,"W": 4,"X": 8,"Y": 4,"Z": 1,
}

# print (letter_pool_score["A"]) --> 1


letter_pool = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", "D", "D", "D", "E", "E", "E", "E", "E", 
                "E", "E", "E", "E", "E", "E", "E", "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I", "I", 
                "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", "N", "O", "O", "O", "O", "O", "O", "O", 
                "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", "U", 
                "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z"]

#####WAVE_1_FUNCTION#####
def draw_letters():
    copied_letter_pool = list(letter_pool)
    hand_of_letters = []
    while len(hand_of_letters) < 10:
        new_letter = random.choice(copied_letter_pool)
        hand_of_letters.append(new_letter)
        copied_letter_pool.remove(new_letter)
    return hand_of_letters

draw_letters()
#####END OF WAVE 1 FUNCTION#####


#####WAVE_2_FUNCTION#####
def uses_available_letters(word, letter_bank):
    letters_copy = letter_bank[:]
    word = word.upper()
    for letter in word:
        if letter not in letters_copy:
            return False
        else: 
            letters_copy.remove(letter)
    return True
#####END_OF_WAVE_2_FUNCTION#####



#####WAVE_3_FUNCTION#####
def score_word(word):
    letter_scores = []
    word = word.upper()
    for letter in word:
        letter_score = (letter_pool_score[letter])
        letter_scores.append(letter_score)
    if (len(word)) >= 7:
        letter_scores.append(8)
    return sum(letter_scores)
#####END_OF_WAVE_3_FUNCTION#####



#####WAVE_4_FUNCTION#####
def get_highest_word_score(word_list):
    word_scores = []
    for word in word_list:
        word_score = score_word(word)
        winning_word_and_score = (word, word_score)
        word_scores.append(winning_word_and_score)
        print (word_scores)
        highest_score = max(word_scores)
        print (highest_score)
        if len(word) == 10:
            return winning_word_and_score
    
    
    return highest_score
    
get_highest_word_score(["BBBBBB", "AAAAAAAAD", "JQ", "KFHK"])
# best_word = ("XXXX", "32")
#####END_OF_WAVE_4_FUNCTION#####