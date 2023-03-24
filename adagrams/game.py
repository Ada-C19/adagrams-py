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

def draw_letters():
    big_list = []
    for letter, letter_quantity in LETTER_POOL.items():
        big_dict = letter * letter_quantity
        for single_char in big_dict:
            big_list.append(single_char)

    draw_of_10_letters = []
    while len(draw_of_10_letters) < 10:
        random_letter = random.choice(big_list)
        draw_of_10_letters.append(random_letter)
        big_list.remove(random_letter)
    return draw_of_10_letters

draw_letters()   

def uses_available_letters(word, letter_bank):

        word = word.upper()
        for letter in word:
            word_count = word.count(letter)
            letter_bank_count = letter_bank.count(letter)
            if letter not in letter_bank:
                return False
            if word_count > letter_bank_count:
                return False
        return True

def score_word(word):

    score_chart = {
    **dict.fromkeys(["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 1),
    **dict.fromkeys(["D", "G"], 2),
    **dict.fromkeys(["B", "C", "M", "P"], 3),
    **dict.fromkeys(["F", "H", "V", "W", "Y"], 4),
    **dict.fromkeys(["K"], 5),
    **dict.fromkeys(["J", "X"], 8),
    **dict.fromkeys(["Q", "Z"], 10),
    **dict.fromkeys([""], 0)
    }

    word = word.upper()
    total_score = 0
    for letter in word:
        if word == "":
            return False
        else:
            total_score += score_chart[letter]
    if 7 <= len(word) <= 10:
        total_score += 8
    return total_score

def get_highest_word_score(word_list):

    best_words_list = []

    for word in word_list:
        word = word.upper()
        score_one_word = score_word(word)
        best_words_list.append((word, score_one_word))
    # print(best_words_list)
    
    for word, score in best_words_list:
        if len(word) == 10:
            return ((word, score))
    else:
        top_score = 0
        best_word = []
        for word, score in best_words_list:
            if score > top_score:
                top_score = score
                best_word = [word]
            elif score == top_score:
                best_word.append(word)

        short_word = best_word[0]
        for word in best_word:
            if len(short_word) > len(word):
                short_word = word
        return short_word, top_score






    # max_word_score = max(best_words_list, key=lambda x: x[1])
    # if len(best_words_list) == 1:
    #     return best_words_list
    # else:
    #     max_score = max(best_words_list, key=lambda x: x[1])[1]
    #     max_words = [word for word, score in best_words_list if score == max_score]
    #     if len(max_words) == 1:
    #         return max(best_words_list, key=lambda x: x[1])
    #     else:
    #         ten_letter_words = [word for word in max_words if len(word) == 10]
    #         if ten_letter_words:
    #             return (ten_letter_words[0], max_score)
    #         else:
    #             min_length_word = min(max_words, key=lambda x: len(x))
    #             return (min_length_word, max_score)