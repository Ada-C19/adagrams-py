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
    draw_letters_list = []
    letters_freq_dic = {}
    while len(draw_letters_list) < 10:
        cur_random_letter = random.choice(list(LETTER_POOL.keys()))
        if cur_random_letter in letters_freq_dic.keys():
            letters_freq_dic[cur_random_letter] += 1
        else:
            letters_freq_dic[cur_random_letter] = 1
        if letters_freq_dic[cur_random_letter] > LETTER_POOL[cur_random_letter]:
            continue
        else:
            draw_letters_list. append(cur_random_letter)
    return draw_letters_list
def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass