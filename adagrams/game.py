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
        occurences = letters.count(add_letter)
        availability = LETTER_POOL[add_letter]
        if occurences < availability:
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
    score_list = []
    high_score = 0
    potential_winners = []
    winning_word = ''
    for word in word_list:
        wscore = score_word(word)
        score_list.append((word,wscore))
    ordered_list = sorted(score_list, key=lambda word_pair: word_pair[1], reverse = True)
    
    for pair in ordered_list:
        if pair[1] >= high_score:
            high_score = pair[1]
            potential_winners.append(pair)
    if len(potential_winners) ==1:
        winning_word = potential_winners[0]
    for candidate in potential_winners:
                
        if len(candidate[0]) == 10:
            winning_word=candidate
            break
                
        else:
            if candidate[0] == min(word_list, key = len):
                winning_word = candidate

    return winning_word
        