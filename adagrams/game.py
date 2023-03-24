import random



def draw_letters():
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
    drawn_letters = [] 
    for letter in range(10):
        my_current_key = random.choice(list(LETTER_POOL))
        my_current_value = LETTER_POOL.get(my_current_key)
        if my_current_value != 0:
            drawn_letters.append(my_current_key)
            LETTER_POOL[my_current_key] = my_current_value -1
        if LETTER_POOL[my_current_key] == 0:
            LETTER_POOL.pop(my_current_key)
    return drawn_letters
            
       
def uses_available_letters(word, letter_bank): 
    #check parameter if characters exist in  letter_bank
    # true f all letters exist
    # false if any letter is missing
    # word is a string
    #letter_bank a list of ten characters

    bank_copy = letter_bank.copy()
    for letter in word:
        
        if not (letter.upper() in bank_copy):
            return False
        elif letter.upper() in bank_copy:
            bank_copy.remove(letter.upper())
    return True    



def score_word(word):
    score = 0
    length_of_word = len(word)
    letter_value_dict = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1,
        "N": 1, "R": 1, "S": 1, "T": 1, "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "V": 4,
        "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10,
        "Z": 10, "H":4
    }

    if length_of_word >= 7:
        score += 8
    
    for alpha in word:
       score += letter_value_dict[alpha.upper()]
    return score


def get_highest_word_score(word_list):
    
  word_dict = {}
  list_of_max_keys = []
  for word in word_list:
    word_dict[word] = score_word(word)
  max_value = max(word_dict.values())
  for key, value in word_dict.items():
    if value == max_value:
      list_of_max_keys.append(key)
  if len(list_of_max_keys) > 1:
    ten_letter_words_list = []
    for word in list_of_max_keys:
      if len(word) == 10: 
        ten_letter_words_list.append(word)
    if len(ten_letter_words_list) > 0:
      return (ten_letter_words_list[0], word_dict[ten_letter_words_list[0]])
    else:
      sorted_non_ten_letter_word_list = sorted(list_of_max_keys, key=len)
      shortest_word = sorted_non_ten_letter_word_list[0]
      return (shortest_word, word_dict[shortest_word])
  else:
    return (list_of_max_keys[0], word_dict[list_of_max_keys[0]])
