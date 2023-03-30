from random import sample

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

# hand_size = 10
HAND_SIZE = 10

# def draw_letters():
    # letter_list = []
    # hand = []

    # for key, value in LETTER_POOL.items():
    #     letter_list.extend([key] * value)
    
    # for i in range(hand_size):
    #     random_num = random.randint(0, len(letter_list) - 1)
    #     hand.append(letter_list[random_num])
    #     letter_list.pop(random_num)

    # return hand
def draw_letters():
    letter_list = []

    for key, value in LETTER_POOL.items():
        letter_list.extend([key] * value)

    return sample(letter_list, HAND_SIZE)

# def uses_available_letters(word, letter_bank):
#     word = word.upper()
#     result = True
#     for letter in word:
#         if word.count(letter) > letter_bank.count(letter):
#             result = False
#             break
#     return result

def uses_available_letters(word, letter_bank):
    word = word.upper()
    for letter in word:
        if letter in letter_bank:
            # letter_bank(letter).pop()
            letter_bank.remove(letter)
        else:
            return False
    return True

def uses_available_letters(word, letter_bank):

    word = word.upper()
    for letter in set(word):
        if word.count(letter) > letter_bank.count(letter):
            return False
    return True

def score_word(word):
    total_value = 0
    for letter in word.upper():
        for key,value in LETTER_SCORE.items():
            if letter == key:
                total_value += value
    if len(word) >= 7:  
        total_value += 8
    return total_value

def get_highest_word_score(word_list):
    words_scored = []

    for word in word_list:
        score = score_word(word)
        words_scored.append((word, score))

    highest_score = max(pair[1] for pair in words_scored)
    winners = [pair for pair in words_scored if pair[1] == highest_score]
    word_list_short = sorted(winners, key=lambda x: len(x[0]))
    word_list_long = sorted(winners, key=lambda x: len(x[0]), reverse=True)

    short_winner = word_list_short[0]
    long_winner = word_list_long[0]

    if len(long_winner[0]) == 10:
        return long_winner
    else:
        return short_winner
    


# -----------------------------------------------------

# FIRST ATTEMPT

# def uses_available_letters(word, letter_bank):

    # result = all(letter in letter_bank for letter in word)
    # return result


    # result = set(word).issubset(set(letter_bank))
    # print(f"{result = }")
    # return result



    # word_dict = {} 
    # letters_dict = {} 
    # for letter in word: 
    #     word_dict[letter] = word_dict.get(letter, 0) + 1 
    # for letter in letter_bank: 
    #     letters_dict[letter] = letters_dict.get(letter, 0) + 1 
    # for letter in word: 
    #     if letter not in letter_bank or word_dict[letter] != letters_dict[letter]:
    #         result = False 
    #         break
    # print(f"{word_dict = }")
    # print(f"{letters_dict = }")
    # return result

    
    # word_list = []
    # word_list[:0] = word
    # print(f'{word_list = }')


    # letter_bank_str = ''.join(letter_bank)
    # letter_bank_str = letter_bank_str.casefold()
    # print(f"{letter_bank_str = }")

    # word = word.casefold()
    # print(f"{word = }")
    # for letter in word:
    #     if letter not in letter_bank_str:
    #         return False
    #         break
    #     else:
    #         return True
        






# def get_highest_word_score(word_list):

#     print(f"before sort {word_list = }")
#     word_list_short = sorted(word_list, key=len)
#     word_list_long = sorted(word_list, key=len, reverse = True)
#     print(f"after sorted {word_list_short = }")
#     print(f"after sorted {word_list_long = }")

#     for word in word_list_short:
#         score = score_word(word)
#         words_scored.append((word, score))
#     print(f"{words_scored = }")

#     # words_scored.append((word_list_low[0], score),(word_list_high[0], score))

#     highest_score = max(pair[1] for pair in words_scored)
#     winners = [pair for pair in words_scored if pair[1] == highest_score]
#     last_word = winners[-1][0]

#     if len(last_word) == 10:
#         return winners[-1]
#     else:
#         return winners[0]

#     print(f"{words_scored = }")
#     print(f"{scores = }")
#     print(f"{highest_score = }")
#     print(f"{winners = }")

#     winner_list = []
    
#     for word in word_list:
#         word_score = score_word(word)
#         tuple_score = word, word_score
#         winner_list.append(tuple_score)

#     result = sorted(winner_list, key=lambda x: x[1], reverse=True)
#     word_lenght_list = []

#     for item in result:
#         if item[1] == result[0][1]:
#             word_lenght_list.append(item)
    
#     word_lenght_sort = sorted(word_lenght_list, key=lambda x: len(x[0]))
#     word_lenght_sort_ten = sorted(word_lenght_list, key=lambda x: len(x[0]), reverse=True)
#     first_item = word_lenght_sort_ten[0]
#     if len(first_item[0]) == 10:
#         return word_lenght_sort_ten[0]
#     else:
#         return word_lenght_sort[0]
    
# get_highest_word_score_results = get_highest_word_score(test_word_list)
# print(f"{get_highest_word_score_results = }")
# def get_highest_word_score(word_list):
#     words_scored = []
#     scores = []

#     print(f"before sort {word_list = }")
#     word_list_short = sorted(word_list, key=len)
#     word_list_long = sorted(word_list, key=len, reverse = True)
#     print(f"after sorted {word_list_short = }")
#     print(f"after sorted {word_list_long = }")

#     for word in word_list:
#         score = score_word(word)
#         words_scored.append((word, score))
#     print(f"{words_scored = }")

#     words_scored.append((word_list_low[0], score),(word_list_high[0], score))

#     highest_score = max(pair[1] for pair in words_scored)
#     winners = [pair for pair in words_scored if pair[1] == highest_score]
#     print(f"{winners = }")
#     print(f"{highest_score = }")
#     word_list_short = sorted(winners, key=lambda x: len(x[0]))
#     word_list_long = sorted(winners, key=lambda x: len(x[0]), reverse=True)
#     print(f"after sorted {word_list_short = }")
#     print(f"after sorted {word_list_long = }")

#     short_winner = word_list_short[0]
#     long_winner = word_list_long[0]
#     winners = [pair for pair in words_scored if pair[1] == highest_score]
#     last_word = winners[-1][0]

#     if len(long_winner[0]) == 10:
#         return long_winner
#     else:
#         return short_winner

#     print(f"{words_scored = }")
#     print(f"{scores = }")
#     print(f"{highest_score = }")
#     print(f"{winners = }")

#     print(f"before sort {word_list = }")
#     word_list_short = sorted(words_scored, key=lambda x: len(x[0]))
#     word_list_long = sorted(words_scored, key=lambda x: len(x[0]), reverse=True)
#     print(f"after sorted {word_list_short = }")
#     print(f"after sorted {word_list_long = }")

#     for word in word_list_short:
#         score = score_word(word)
#         words_scored.append((word, score))
#     print(f"{words_scored = }")

#     # words_scored.append((word_list_low[0], score),(word_list_high[0], score))

#     highest_score = max(pair[1] for pair in words_scored)
#     winners = [pair for pair in words_scored if pair[1] == highest_score]
#     last_word = winners[-1][0]

#     if len(last_word) == 10:
#         return winners[-1]
#     else:
#         return winners[0]

#     print(f"{words_scored = }")
#     print(f"{scores = }")
#     print(f"{highest_score = }")
#     print(f"{winners = }")

#     winner_list = []
    
#     for word in word_list:
#         word_score = score_word(word)
#         tuple_score = word, word_score
#         winner_list.append(tuple_score)

#     result = sorted(winner_list, key=lambda x: x[1], reverse=True)
#     word_lenght_list = []

#     for item in result:
#         if item[1] == result[0][1]:
#             word_lenght_list.append(item)
    
#     word_lenght_sort = sorted(word_lenght_list, key=lambda x: len(x[0]))
#     word_lenght_sort_ten = sorted(word_lenght_list, key=lambda x: len(x[0]), reverse=True)
#     first_item = word_lenght_sort_ten[0]
#     if len(first_item[0]) == 10:
#         return word_lenght_sort_ten[0]
#     else:
#         return word_lenght_sort[0]
    
# get_highest_word_score_results = get_highest_word_score(test_word_list)
# print(f"{get_highest_word_score_results = }")




# FIRST ATTEMPT/WORKING CODE


# def get_highest_word_score(word_list):
#     winner_list = []
    
#     for word in word_list:
#         word_score = score_word(word)
#         print(f"{word_score = }")
#         tuple_score = word, word_score
#         print(f"{tuple_score = }")
#         winner_list.append(tuple_score)
#         print(f"{winner_list = }")

#     result = sorted(winner_list, key=lambda x: x[1], reverse=True)
#     print(f"{result = }")

#     word_lenght_list = []

#     for item in result:
#         if item[1] == result[0][1]:
#             word_lenght_list.append(item)
#     print(f"{word_lenght_list = }")
    
#     word_lenght_sort = sorted(word_lenght_list, key=lambda x: len(x[0]))
#     print(f"{word_lenght_sort = }")
#     word_lenght_sort_ten = sorted(word_lenght_list, key=lambda x: len(x[0]), reverse=True)
#     print(f"{word_lenght_sort_ten = }")
#     first_item = word_lenght_sort_ten[0]
#     print(f"{first_item = }")
#     if len(first_item[0]) == 10:
#         return word_lenght_sort_ten[0]
#     else:
#         return word_lenght_sort[0]

# get_highest_word_score_results = get_highest_word_score(test_word_list)
# print(f"{get_highest_word_score_results = }")






# def get_highest_word_score(word_list):

#     # print(f"before sort {word_list = }")
#     # word_list_short = sorted(word_list, key=len)
#     # word_list_long = sorted(word_list, key=len, reverse = True)
#     # print(f"after sorted {word_list_short = }")
#     # print(f"after sorted {word_list_long = }")

#     # words_scored.append((word_list_low[0], score),(word_list_high[0], score))

#     highest_score = max(pair[1] for pair in words_scored)
#     winners = [pair for pair in words_scored if pair[1] == highest_score]
#     print(f"{winners = }")
#     print(f"{highest_score = }")
#     word_list_short = sorted(winners, key=lambda x: len(x[0]))
#     word_list_long = sorted(winners, key=lambda x: len(x[0]), reverse=True)
#     print(f"after sorted {word_list_short = }")
#     print(f"after sorted {word_list_long = }")

#     short_winner = word_list_short[0]
#     long_winner = word_list_long[0]
#     # winners = [pair for pair in words_scored if pair[1] == highest_score]
#     # last_word = winners[-1][0]

#     if len(long_winner[0]) == 10:
#         return long_winner
#     else:
#         return short_winner

    # print(f"{words_scored = }")
    # print(f"{scores = }")
    # print(f"{highest_score = }")
    # print(f"{winners = }")

    
    # for word in word_list:
    #     word_score = score_word(word)
    #     tuple_score = word, word_score
    #     winner_list.append(tuple_score)

    # result = sorted(winner_list, key=lambda x: x[1], reverse=True)
    # word_lenght_list = []

    # for item in result:
    #     if item[1] == result[0][1]:
    #         word_lenght_list.append(item)
    
    # word_lenght_sort = sorted(word_lenght_list, key=lambda x: len(x[0]))
    # word_lenght_sort_ten = sorted(word_lenght_list, key=lambda x: len(x[0]), reverse=True)
    # first_item = word_lenght_sort_ten[0]
    # if len(first_item[0]) == 10:
    #     return word_lenght_sort_ten[0]
    # else:
    #     return word_lenght_sort[0]
    
# get_highest_word_score_results = get_highest_word_score(test_word_list)
# print(f"{get_highest_word_score_results = }")










