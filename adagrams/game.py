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

LETTER_SCORE = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

hand_size = 10

letter_bank = ['A', 'N', 'S', 'I', 'T', 'A', 'P', 'A', 'U', 'N']
print(f"{letter_bank = }")
word_test  = "ANSIT"
print(f"{word_test = }")



def draw_letters():

    letter_list = []
    for key, value in LETTER_POOL.items():
        letter_list.extend([key] * value)

    hand = []
    for i in range(hand_size):
        random_num = random.randint(0, len(letter_list) - 1)
        hand.append(letter_list[random_num])
        letter_list.pop(random_num)

    return hand

letter_bank = draw_letters()

def uses_available_letters(word, letter_bank):
    word = word.upper()
    result = True
    for letter in word:
        if word.count(letter) > letter_bank.count(letter):
            result = False
            break
    return result

uses_available_letters("word", letter_bank)


def score_word(word):
    total_value = 0
    for letter in word.upper():
        for key,value in LETTER_SCORE.items():
            if letter == key:
                total_value += value
    if len(word) >= 7:  
        total_value += 8
    print(f"{total_value = }")
    return total_value

score_word("word")

def get_highest_word_score(word_list):
    pass

# def draw_letters():

#     letter_list = []
#     for key, value in LETTER_POOL.items():
#         letter_list.extend([key] * value)

#     hand = []
#     for i in range(hand_size):
#         random_num = random.randint(0, len(letter_list) - 1)
#         hand.append(letter_list[random_num])
#         letter_list.pop(random_num)

#     return hand

# letter_bank = draw_letters()

# # -----------------------------------------------------
# # letter_bank = ['A', 'N', 'S', 'I', 'T', 'A', 'P', 'A', 'U', 'N']
# print(f"{letter_bank = }")
# # word_test = input("Make a word: ")
# word_test  = "aaannnsitddddd"
# print(f"{word_test = }")

# def uses_available_letters(word, letter_bank):
#     word = word.upper()
#     result = True
#     for letter in word:
#         print(f"{letter = } {word.count(letter) = } {letter_bank.count(letter) = }")
#         if word.count(letter) > letter_bank.count(letter):
#             result = False
#             break
#     return result

#     # word = word.upper()
#     # for letter in word:
#     #     if word.count(letter) > letter_bank.count(letter):
#     #         return False
#     # return True
#     # result = True
#     # result = all(letter in letter_bank for letter in word)
#     # return result
#     # word_dict = {} 
#     # letters_dict = {} 
#     # for letter in word: 
#     #     word_dict[letter] = word_dict.get(letter, 0) + 1 
#     # for letter in letter_bank: 
#     #     letters_dict[letter] = letters_dict.get(letter, 0) + 1 
#     # for letter in word: 
#     #     if letter not in letter_bank or word_dict[letter] != letters_dict[letter]:
#     #         result = False 
#     #         break
#     # print(f"{word_dict = }")
#     # print(f"{letters_dict = }")
#     # return result

#     # word = input("input word: ")

#     # word_list = []
#     # word_list[:0] = word
#     # print(f'{word_list = }')


#     # letter_bank_str = ''.join(letter_bank)
#     # letter_bank_str = letter_bank_str.casefold()
#     # print(f"{letter_bank_str = }")

#     # result = all(letter in word for letter in letter_bank_str)

#     # result = set(word).issubset(set(letter_bank))
#     # print(f"{result = }")
#     # return result

#     # letter_bank_str = ''.join(letter_bank)
#     # letter_bank_str = letter_bank_str.casefold()
#     # print(f"{letter_bank_str = }")

#     # word = word.casefold()
#     # print(f"{word = }")

#     # for letter in word:
#     #     if letter not in letter_bank_str:
#     #         return False
#     #         break
#     #     else:
#     #         return True
        
# uses_available_letters_output = uses_available_letters(word_test, letter_bank)
# print({f"{uses_available_letters_output = }"})
# # print(f"{letter_bank = }")

# def score_word(word):
#     total_value = 0
#     for letter in word.upper():
#         for key,value in LETTER_SCORE.items():
#             if letter == key:
#                 total_value += value
#     if len(word) >= 7:  
#         total_value += 8
#     print(f"{total_value = }")
#     return total_value

# score_word_return = score_word(word_test)
# print(f"{score_word_return = }")

# def get_highest_word_score(word_list):
#     pass

