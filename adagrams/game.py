import random
LETTER_POOL = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
            'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1,'R': 6, 'S': 4, 
            'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1}
def create_dict_of_10_letters():
    alphabet_dict = LETTER_POOL.copy()

    dict_of_10_letters = {}
    total_letters_dict = 0
    while total_letters_dict < 10:
        letter = random.choice(list(alphabet_dict))
        if alphabet_dict[letter] < 1:
            continue
        elif letter in dict_of_10_letters:
            dict_of_10_letters[letter] += 1
            alphabet_dict[letter] -= 1
            total_letters_dict += 1
        else: 
            dict_of_10_letters[letter] = 1
            alphabet_dict[letter] -= 1
            total_letters_dict += 1
    return dict_of_10_letters

def draw_letters():
    selected_dict = create_dict_of_10_letters()
    list_of_letters = []
    for letter, num in selected_dict.items():
        for i in range(num):
            list_of_letters.append(letter)
    return list_of_letters

def uses_available_letters(word, letter_bank):
    copy_letter_bank = letter_bank.copy()
    letters_from_word_list = list(word.upper())
    while len(letters_from_word_list) > 0:
        letter = letters_from_word_list[0]
        if letter in copy_letter_bank:
            copy_letter_bank.remove(letter)
            letters_from_word_list.remove(letter)
        else:
            return False
    return True

def score_word(word):
    score_chart = {
                    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'L': 1, 'N': 1, 
                    'R': 1, 'S': 1, 'T': 1, 'D': 2, 'G': 2,'B': 3, 
                    'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 
                    'W': 4, 'Y': 4,'K': 5, 'J': 8, 'X': 8,'Q': 10, 
                    'Z': 10
                }
    list_from_word = list(word.upper())
    total_points = 0
    for letter in list_from_word:
        if letter in score_chart:
            total_points += score_chart[letter]
    if len(word) == 7 or len(word) == 8 or len(word) == 9 or len(word) == 10:
        total_points += 8
    return total_points

#Esta f(x) va a tomar 2 tuples y devuelve la de mayor puntaje.
#Con el valor que devuelve get_highest_word_score la va a comparar contra el ELEMENTO que tiene en el for en ese momento y retorna
def find_max_of_2_tuples(tuple1, tuple2):
    if tuple1 == None:
        return tuple2
    
    score_tuple1 = tuple1[1]
    score_tuple2 = tuple2[1]
    len_tuple1 = len(tuple1[0])
    len_tuple2 = len(tuple2[0])
    if score_tuple1 == score_tuple2 and len_tuple1 == 10:
        return tuple1
    elif score_tuple1 == score_tuple2 and len_tuple2 == 10:
        return tuple2
    elif score_tuple1 == score_tuple2 and len_tuple1 < len_tuple2:
        return tuple1
    elif score_tuple1 == score_tuple2 and len_tuple1 == len_tuple2:
        return tuple1
    elif score_tuple1 > score_tuple2:
        return tuple1
    else: 
        return tuple2

def get_highest_word_score(word_list):
    compare_scores = {}
    for word in word_list:
        score_per_word = score_word(word)
        compare_scores[word] = score_per_word
    
    sorted_tuple_scores = sorted(compare_scores.items(), key=lambda x:x[1])
    highest_score = None
    for i in range(len(sorted_tuple_scores)):
        tuple_element = sorted_tuple_scores[i]
        check_higher_score = find_max_of_2_tuples(highest_score, tuple_element)
        highest_score = check_higher_score

    return highest_score
