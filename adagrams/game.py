# import random





# def draw_letters():
#     letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#     # weights_placeholders = [10.44, 47, 47, 23.5, 7.83, 47, 31.33, 47, 10.44, 94, 94, 23.5, 47, 15.67, 11.75, 47, 94, 15.67, 23.5, 15.67, 23.5, 47, 47, 94, 47, 94]
#     weights_placeholders = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]

#     random_hand = random.choices(letters, weights = weights_placeholders, k = 10)
#     return random_hand

# def uses_available_letters(word, letter_bank):
#     for letter in word:
#         if letter in letter_bank:
#             letter_bank.remove(letter)
#             return True
#     return False
    

def score_word(word):
    score = 0
    uniform_case_word = word.upper()
    one_pointers = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    two_pointers = ["D", "G"]
    three_pointers = ["B", "C", "M", "P"]
    four_pointers = ["F", "H", "V", "W", "Y"]
    five_pointers = ["K"]
    eight_pointers = ["J", "X"]
    ten_pointers = ["Q", "Z"]

    for letter in uniform_case_word:
        if letter in one_pointers:
            score += 1
        if letter in two_pointers:
            score += 2
        if letter in three_pointers:
            score += 3
        if letter in four_pointers:
            score += 4
        if letter in five_pointers:
            score += 5
        if letter in eight_pointers:
            score += 8
        if letter in ten_pointers:
            score += 10
        
    if len(word) >= 7:
            score += 8



    return score 

def get_highest_word_score(word_list):
    highest_word_score = ("", 0)
    for word in word_list:
        word_score = word, score_word(word)
        if word_score[1] > highest_word_score[1]:
            highest_word_score = word_score
        elif word_score[1] == highest_word_score[1]:
            if len(word_score[0]) == 10:
               highest_word_score = word_score 
            elif len(highest_word_score[0]) == 10:
                highest_word_score = highest_word_score    
            elif len(word_score[0]) < len(word_score[0]):
                highest_word_score = word_score
    return highest_word_score
            
        

    