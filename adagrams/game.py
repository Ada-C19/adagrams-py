import random
letter_pool_list = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A','B','B', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']
LETTER_POOL_VALUES = {
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
    word = word.upper()
    score = 0
    if len(word) >= 7:
       score += 8
    for letter in word:
       score += LETTER_POOL_VALUES.get(letter)
    return score
    
def get_highest_word_score(word_list):
    word_list_score_dict = {}
    checked_values = set()
    duplicates = set()

    for word in word_list:
      score = score_word(word)
      word_list_score_dict[word] = score
      highest_score = max(word_list_score_dict.values())
      
    for word, score in word_list_score_dict.items():
      if score not in checked_values:
        checked_values.add(score)
      else:
        duplicates.add(score)

    if duplicates:
      tie_breaker_score = tie_breaker(word_list)
      return tie_breaker_score
    
    return (max(word_list_score_dict, key=word_list_score_dict.get)), highest_score
    

def tie_breaker(word_list):
  word_count_list = []
  shortest_word = []
  tie_breaker_result = {}

  prefers_ten_result = tie_breaker_prefers_ten(word_list)
  
  for word in word_list:
    word_count_list.append(len(word))
    tie_breaker_result[word] = (len(word))
  
  word_count_list.sort()
  shortest_word = word_count_list[0]
  if prefers_ten_result:
    return prefers_ten_result
  else:   
    for key, value in tie_breaker_result.items():
      if len(key) == shortest_word:
          return key, score_word(key)
      
def tie_breaker_prefers_ten(word_list):
  word_count_list = []
  tie_breaker_result = {}
  
  for word in word_list:
    word_count_list.append(len(word))
    tie_breaker_result[word] = (len(word))
    if len(word) == 10:
      ten_letter_word = word
      return ten_letter_word, score_word(ten_letter_word)

  return False

def tie_breaker_prefers_ten(word_list):
  word_count_list = []
  tie_breaker_result = {}
  
  for word in word_list:
    word_count_list.append(len(word))
    tie_breaker_result[word] = (len(word))
    if len(word) == 10:
      ten_letter_word = word
      return ten_letter_word, score_word(ten_letter_word)

  return False