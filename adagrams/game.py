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
def draw_letters():
    letters = []
    avail_letters = list(LETTER_POOL.keys())
    while len(letters) < 10:
        choose_letter = (random.choices(avail_letters))
        add_letter = choose_letter[0]
        if letters.count(add_letter) < LETTER_POOL[add_letter]:
            letters+=add_letter

    return letters

def uses_available_letters(word, letter_bank):
    available_letters = letter_bank[:]
    word = word.upper()
    for letter in word:
        if not letter in available_letters:
            return False
        else:
            available_letters.remove(letter)
    return True

def score_word(word):
    score = 0
    for letter in word:
        score += LETTER_SCORE.get(letter.upper())
    if len(word)>= 7:
        score += 8
    return score

def get_highest_word_score(word_list):    
    highest_score = 0
    winning_word = ""

    for word in word_list:
        score = score_word(word)
        
        if score > highest_score:
            highest_score = score
            winning_word = word
            
        elif score == highest_score:
            if (len(word) == 10 or len(word) < len(winning_word)) and len(winning_word) != 10:
                winning_word = word

    return winning_word, highest_score
        