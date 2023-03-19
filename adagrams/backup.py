
import random
# Hacer una funcion que me cree el dict con las 10 letras random
# Dentro de la 1ra f(x) codigo que compara contra el diccionario ppal y evalua que no se pase del numero max de letras disponibles
LETTER_POOL = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 
    'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 
    'Z': 1}

def is_valid_guess(available_letters, current_letters, guess):
    if guess not in available_letters:
        return False
    elif guess not in current_letters:
        if available_letters[guess] > 0:
            return True
        else:
            return False
    elif current_letters[guess] < available_letters[guess]:
        return True
    else:
        return False
print(is_valid_guess(LETTER_POOL, {}, "M"))

# def next_letter_dict(result_dict):
#     available_letters = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 
#     'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 
#     'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 
#     'Z': 1}
#     total_letters = 0
#     random_letter = random.choice(list(available_letters))
    
#     while total_letters < 11:
#         is_letter_valid = is_valid_guess(available_letters, result_dict, random_letter)
#         if is_letter_valid == False:



def create_dict_of_10_letters():
    available_letters = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 
    'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 
    'Z': 1}

    dict_of_10_letters = {}
    total_amount_letters = 0
    for letter in available_letters:
        letter = random.choice(list(available_letters))
        
        if letter in dict_of_10_letters:
            dict_of_10_letters[letter] += 1
            available_letters[letter] -= 1
            total_amount_letters += 1
        if total_amount_letters == 10:
            break
        else: 
            dict_of_10_letters[letter] = 1
            available_letters[letter] -= 1
            total_amount_letters += 1
    print(available_letters)
    return dict_of_10_letters       
print(create_dict_of_10_letters())

# # Crear una funcion que dado un numero de letras me devuelva 1 lista con esas letras n (num) veces
# def repeat_letter_in_list(letter, num):

#     list_of_repeated_nums = []
#     for i in range(num):
#         list_of_repeated_nums.append(letter)
#     return list_of_repeated_nums

# # Hacer una funcion que toma el diccionario y genera la lista de 10 letras
# def create_list_from_dict():
#     list_of_10_letters = []
#     dict_from_function = create_dict_of_10_letters()
#     print(dict_from_function)

#     for letter, num in dict_from_function.items():
#         # print(letter)
#         if num > 1:
#             repeated_letters_to_append = repeat_letter_in_list(letter, num)
#             for item in repeated_letters_to_append:
#                 list_of_10_letters.append(item) 
#         else:
#             list_of_10_letters.append(letter)
#     return list_of_10_letters

# #print(create_list_from_dict())

# def draw_letters():
    
    
# print(draw_letters())

# def uses_available_letters(word, letter_bank):
#     pass

# def score_word(word):
#     pass

# def get_highest_word_score(word_list):
#     pass