import random
# Hacer una funcion que me cree el dict con las 10 letras random
# Dentro de la 1ra f(x) codigo que compara contra el diccionario ppal y evalua que no se pase del numero max de letras disponibles
def create_dict_of_10_letters():
    alphabet_dict = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 
    'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 
    'Z': 1}

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
        
print(create_dict_of_10_letters())

def draw_letters():
    selected_dict = create_dict_of_10_letters()
    list_of_letters = []
    for letter, num in selected_dict.items():
        for i in range(num):
            list_of_letters.append(letter)
    return list_of_letters
print(draw_letters())

def uses_available_letters(word, letter_bank):
    letters_from_word_list = list(word)
    print(letters_from_word_list)

print(uses_available_letters("dog", draw_letters()))
# def score_word(word):
#     pass

# def get_highest_word_score(word_list):
#     pass