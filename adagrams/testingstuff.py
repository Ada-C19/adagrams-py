
# import random
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
# #  [['A', 'B', 'C', 'D', 'E']]

# # letter_list = list((LETTER_POOL))
# # print(letter_list)

# # # def draw_letters():
# # #     selected_letters = []
# # #     for letter in random.choice(list(LETTER_POOL.keys())):
# # #         selected_letters += letter
# # #         if len(selected_letters) >= 10:
# # #             return selected_letters
# # #     return selected_letters


# letter_list = []
# for letter in LETTER_POOL.keys():
#     letter_list += LETTER_POOL[letter] * letter
# # print(letter_list)

# def draw_letters():
#     selected_letters = []
#     while len(selected_letters) < 10:
#         random_index = random.randint(0,  len(letter_list)-1)
#         chosen_letter = letter_list[random_index]
#         print(chosen_letter)
#         if selected_letters.count(chosen_letter) < LETTER_POOL[chosen_letter]:
#             # print(LETTER_POOL[chosen_letter])
#             selected_letters += chosen_letter
#             # print(selected_letters)
            
#         else:
#             continue
#     print(selected_letters)
#     return selected_letters

# draw_letters()



    # while len(word) > 1 and type(word) == str:
    #     while word in letter_bank:
    #         print(word)
    #         if word in letter_bank: 
    #             # print(word)
    #             return True
    #         else:
    #             return False  
    #     else:
    #         return False         
 
    # return word

# def draw_letters():
#     selected_letters = []
#     while len(selected_letters) < 10:
#         random_index = random.randint(0,  len(letter_list)-1)
#         chosen_letter = letter_list[random_index]
#         if selected_letters.count(chosen_letter) < LETTER_POOL[chosen_letter]:
#             selected_letters += chosen_letter
#             # print(selected_letters)
            
#         else:
#             continue
#     print(selected_letters)
#     return selected_letters

# def uses_available_letters(word, letter_bank):   # defining the function   
#     while len(word) > 1 and type(word) == str: 
#         if word == letter_bank[letter]:
#             return True
        

# print(uses_available_letters("anymore", ["h", "a", "n","m","o","r","e","y"]))

# def score_word(word):
#     word_score = 0
#     # word_score = 0
#     scores = { 1: "A" "E" "I" "O" "U" "L" "N" "R" "S" "T",
#     2: "D" "G"}
#     # 3 : ["B", "C", "M", "P" ,
#     # 4: ["F", "H", "V", "W", "Y"],
#     # 5: ["K"],
#     # 8:["J", "X"],
#     # 10: ["Q", "Z"]}
#     for i in scores.items():
#         print(i)
#         for letter in i:
#             # print(letter)
#             word_score += i[letter]
#             print(word_score)
    
# print(score_word("Rug"))


# def score_word(word):
#     word_score = 0
#     extra_points = 8
#    # if able to refactor try a nested list. 
#     value_1_list = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
#     value_2_list = ["D", "G"]
#     value_3_list = ["B", "C", "M", "P"]
#     value_4_list = ["F", "H", "V", "W", "Y"]
#     value_5_list = ["K"]
#     value_8_list = ["J", "X"]
#     value_10_list = ["Q", "Z"]

    
#     while len(word) < 7:
#         for character in word.upper():
#             if character in value_1_list:
#                 word_score += 1
#             elif character in value_2_list:
#                 word_score += 2
#             elif character in value_3_list:
#                 word_score += 3
#             elif character in value_4_list:
#                 word_score += 4
#             elif character in value_5_list:
#                 word_score += 5
#             elif character in value_8_list: 
#                 word_score += 8
#             elif character in value_10_list:
#                 word_score += 10
#         return word_score
#     else:
#         for character in word.upper():
#             if character in value_1_list:
#                 extra_points += 1
#             elif character in value_2_list:
#                 extra_points += 2
#             elif character in value_3_list:
#                 extra_points += 3
#             elif character in value_4_list:
#                 extra_points += 4
#             elif character in value_5_list:
#                 extra_points += 5
#             elif character in value_8_list: 
#                 extra_points += 8
#             elif character in value_10_list:
#                 extra_points += 10
#         return extra_points



# def get_highest_word_score(word_list):
  
#     winning_words = [] # setting empty list to put winning words 
#     chosen_word = '' # setting a chosen word variable to an empty string 
#     highest_score = 0 # setting a counter called highest_score to 0
#     word_string = '' # setting a word_string variable converter to an empty string
#     for word in word_list: # iterating over the word list 
#         # word_string = ''
#         word_score = score_word(word)  #calling the score word function and setting it to word_score
        
#         if word_score > highest_score:  # if word_score is greater than the highest score
            
#            highest_score = word_score # the highest score now takes that score
#            winning_words = [word] # winning words now contains the winning word
#         elif word_score == highest_score: # and if word_score is equal to the highest word
#             winning_words.append(word) # it adds that word to the list,(how we get ties)
#         # word_string = winning_words[0]
       
#         if len(winning_words) > 1:# if the length of winning _words is greater than one word 
        
#             for word in winning_words: # iterating over every word in winning_word list                # word_string = winning_words[0]
#                 if len(word) > len(chosen_word): # nested conditional, if the length of the word is greater than the chosen word 
#                     chosen_word = word # chosen word is now the word
#                     winning_words.remove(chosen_word) # the word is now removed from the list, aka the smallest word wins. 
#                 elif len(word) == 10:
#                     return word
                
#                         # print(winning_words)
#         word_string = winning_words[0]
#     return word_string, highest_score


# print(get_highest_word_score(["MMMM", "WWW"]))











# def get_highest_word_score(word_list):
  
#     winning_words = [] 
#     chosen_word = ''
#     highest_score = 0 
#     word_string = ''
#     for word in word_list: 
#         # word_string = ''
#         word_score = score_word(word) 
        
#         if word_score > highest_score: 
            
#            highest_score = word_score 
#            winning_words = [word] # winning words now contains the winning word
#         elif word_score == highest_score:
#             winning_words.append(word)
#         for word in winning_words:
#             word_string = winning_words[0]
#             if len(winning_words) > 1:
#                 # word_string = winning_words[0]
#                 if len(word) > len(chosen_word):
#                     chosen_word = word
#                     winning_words.remove(chosen_word)
#                     # word_string = winning_words
#                     # print(winning_words, highest_score)
#                 elif len(word) < 10:
#                     winning_words.remove(word)
#                     print(winning_words)
#             # elif len(word )


# #     return word_string, highest_score
# def get_highest_word_score(word_list):
  
#     winning_words = [] # setting empty list to put winning words 
#     chosen_word = '' # setting a chosen word variable to an empty string 
#     highest_score = 0 # setting a counter called highest_score to 0
#     word_string = '' # setting a word_string variable converter to an empty string
#     tie_breaker = []

#     for word in word_list: # iterating over the word list 
#         # word_string = ''
#         word_score = score_word(word)  #calling the score word function and setting it to word_score
        
#         if word_score > highest_score:  # if word_score is greater than the highest score proceed to loop
            
#            highest_score = word_score # the highest score now takes that score
#            winning_words = [word] # winning words now contains the winning word
#         elif word_score == highest_score: # and if word_score is equal to the highest word
#             winning_words.append(word) # it adds that word to the list,(how we get ties)
#         # word_string = winning_words[0]
       
#         if len(winning_words) > 1:# if the length of winning _words is greater than one word 
        
#             for word in winning_words: # iterating over every word in winning_word list                # word_string = winning_words[0]
#                 if len(word) > len(chosen_word): # nested conditional, if the length of the word is greater than the chosen word 
#                     chosen_word = word # chosen word is now the word
#                     winning_words.remove(chosen_word) # the word is now removed from the list, aka the smallest word wins. 
    
#                     for word in winning_words:
#                         # print(word)
#                         tie_breaker.append(word)
#                         # print(tie_breaker)
#                         for i in tie_breaker:
#                             if len(i)  10:
#                                 # print(i)
#                                 tie_breaker.remove(i)
#                                 # chosen_word = word
#                                 # tie_breaker.remove(chosen_word)
#                                 print(tie_breaker)

#                     # for word in winning_words:
#                     #     if len(word) < 10:
#                     #         # chosen_word = word
#                     #         winning_words.remove(word)  
#                     #         print(winning_words)                  
                    
#                     # if not len(chosen_word) == 10: # else if the length of the word is less than ten 
#                     #     # chosen_word = word # chosen word now becomes the word with the length of ten.
#                     #     winning_words.remove(chosen_word) #remove word from list. 
#                     #     print(winning_words)
                       
                


    
#     # return word_string, highest_score

















# def get_highest_word_score(word_list):
    
#      # if word_score in hand 1, greater than word score in hand 5:
#     # return hand 1
#     # if extra word score in hand 1 greater than word score in hand 5
#     # return extra_word score
#     # if extra word score greater than word_score
#     #return word score
#     # add elses statements for the oppiste.
    
#     winning_words = [] # empty list to store winning word(s)
#     #
#     # extra_points = score_word(word)

# # # winning_word gains word if the value of word score is the same as the highest score
        
        
        

# #         # for word in word_list:
            

# #         #     if extra_points > highest_score:
# #         #         highest_score = extra_points
# #         #         winning_words = [word]
# #         #     elif extra_points == highest_score:
# #         #         winning_words.append(word)    #     highest_score = extra_points
# #     # if word_score > extra_points    
# #     # extra_points = score_word(word)
# #     highest_score = 0 # setting a counter
# #     for word in word_list: # iterating through every word in word_list 
        
# #         word_score = score_word(word) #caling the score word function
# #         # print(word_score)
# #         if word_score > highest_score: # if word score greater than the highest_score
            
# #            highest_score = word_score # highest score take the value of word_score
# #            winning_words = [word] # winning words now contains the winning word
# #            for word in winning_words:
# #             #    print(word)
# #                 if len(word) < len(word):
# #                     winning_words.append(word)
# #                     print(winning_words)
# #                 my_string = word# winning_word gains word if the value of word score is the same as the highest score
# #     return my_string, highest_score










# def get_highest_word_score(word_list):
#     winning_words = [] # empty list to store winning word(s)
#     chosen_word = ''
#     word_string = ''
#     highest_score = 0 # setting a counter
#     for word in word_list: # iterating through every word in word_list 
#         word_string = word
#         word_score = score_word(word) 
#         if word_score > highest_score: 
            
#            highest_score = word_score 
#            winning_words = [word] 
#         elif word_score == highest_score:
#             winning_words.append(word)
#         for word in winning_words:
            
#             if len(winning_words) > 1:

#                 if len(word) > len(chosen_word):
#                     chosen_word = word
#                     winning_words.remove(chosen_word)
#                     # print(winning_words, highest_score)
#                 elif len(word) < 10:
#                     winning_words.remove(word)

                


    
#     return word_string, highest_score
# print(get_highest_word_score(["MMMM", "WWW"]))

# print(get_highest_word_score(["MMMM", "WWW","AAAAAAAAAA", "BBBBBB",]))
# elif len(word) > len(word):
                #     winning_words.remove(word)
                #     print(winning_words)
                # if len(word) == 10:
                #     winning_words.append(word)
                # if len(word) < 10:
               #     winning_words.append(word)


    #            def get_highest_word_score(word_list):
    # winning_words = [] # empty list to store winning word(s)
    # chosen_word = ''
    # word_string = ''
    # highest_score = 0 # setting a counter
    # for word in word_list: # iterating through every word in word_list 
    #     word_string = word
    #     word_score = score_word(word) 
    #     if word_score > highest_score: 
            
    #        highest_score = word_score 
    #        winning_words = [word] 
    #     elif word_score == highest_score:
    #         winning_words.append(word)
    #     for word in winning_words:
            
    #         if len(winning_words) > 1:

    #             if len(word) > len(chosen_word):
    #                 chosen_word = word
    #                 winning_words.remove(chosen_word)
    #                 # print(winning_words, highest_score)
    #             elif len(word) < 10:
    #                 winning_words.remove(word)
    # letter_list = []
# for letter in LETTER_POOL.keys():
#     letter_list += LETTER_POOL[letter] * letter
# # print(letter_list)

# def draw_letters():
#     selected_letters = []
#     while len(selected_letters) < 10:
#         random_index = random.randint(0,  len(letter_list)-1)
#         chosen_letter = letter_list[random_index]
#         print(chosen_letter)
#         if selected_letters.count(chosen_letter) < LETTER_POOL[chosen_letter]:
#             # print(LETTER_POOL[chosen_letter])
#             selected_letters += chosen_letter
#             # print(selected_letters)
            
#         else:
#             continue
#     print(selected_letters)
#     return selected_letters

# draw_letters()



    # while len(word) > 1 and type(word) == str:
    #     while word in letter_bank:
    #         print(word)
    #         if word in letter_bank: 
    #             # print(word)
    #             return True
    #         else:
    #             return False  
    #     else:
    #         return False         
 
    # return word

# def draw_letters():
#     selected_letters = []
#     while len(selected_letters) < 10:
#         random_index = random.randint(0,  len(letter_list)-1)
#         chosen_letter = letter_list[random_index]
#         if selected_letters.count(chosen_letter) < LETTER_POOL[chosen_letter]:
#             selected_letters += chosen_letter
#             # print(selected_letters)
            
#         else:
#             continue
#     print(selected_letters)
#     return selected_letters

# def uses_available_letters(word, letter_bank):   # defining the function   
#     while len(word) > 1 and type(word) == str: 
#         if word == letter_bank[letter]:
#             return True
        

# print(uses_available_letters("anymore", ["h", "a", "n","m","o","r","e","y"]))