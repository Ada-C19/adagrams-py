import random
letter_pool_list = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A','B','B', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']


def draw_letters():
    letter_pool_list_copy = list(letter_pool_list)
    one_list = []
    for i in range(10):
        random_letter = random.choice(letter_pool_list_copy)
        one_list.append(random_letter)
        letter_pool_list_copy.remove(random_letter)
    return one_list


def uses_available_letters(word, letter_bank):
  word = word.upper()
  for letter in word:
    letter_bank_count = letter_bank.count(letter)
    word_letter_count = word.count(letter)
    if not letter in letter_bank or word_letter_count > letter_bank_count:
        return False
  return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass