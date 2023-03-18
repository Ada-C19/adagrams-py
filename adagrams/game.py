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
print(uses_available_letters("DOG", ["D", "O", "X", "X", "X", "X", "X", "X", "X", "X"]))
# def score_word(word):
#     pass

# def get_highest_word_score(word_list):
#     pass