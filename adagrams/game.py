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
#Creating a letter list from dictionary!
#We're splitting letters and then throwing them in the pile :-)
split_box = []
#Pulling keys + values from the letter pool, multiplying keys by values and putting into the split_box
for letter, freq in LETTER_POOL.items():
    letter_multiplied = letter * freq
    split_box.append(letter_multiplied)
#new list for all the new letters we've split up!
letter_pile = [c for letter in split_box for c in letter]

#Wave 1
def draw_letters():
    hand = []
    #Drawing 10 letters
    for i in range(10):
        char = random.choice(letter_pile)
        hand.append(char)
    #When a letter is overused!
    for letter in hand:
        if hand.count(letter) > LETTER_POOL[letter]:
            #Removes letter if it's over the # in pool
            hand.remove(letter)
            #Adds a brand new random letter when the length is under 10.. which it should bc lol
            if len(hand) < 10:
                hand.append(random.choice(letter_pile))
    return hand

#wave 2
def uses_available_letters(word, letter_bank):
    #Ignore cases by making word all upper
    word = word.upper()
    #Loop through each letter in word, and checking if it's the letter bank
    for char in word:
        if char in letter_bank and word.count(char) == letter_bank.count(char):
            result = True
        else:
            result = False
    #Counts + compares to the letter bank
    #if word.count(char) > letter_bank.count(char):
        #return False
    return result

def score_word(word):
    score = 0
    #Setting lists for letters + points
    #one_point = ["A","E","I","O","U","L","N","R","S","T"]
    #two_pts = ["D","G"]
    #three_pts = ["B","C","M","P"]
    #four_pts = ["F","H","V","W","Y"]
    #eight_pts = ["J","X"]
    #ten_pts = ["Q","Z"]
    #Making sure words evaluated are uppercase
    word = word.upper()
    #Loop through each letter + add to get each score
    for letter in word:
        if letter != letter.isalpha():
            score += 0
        if letter == letter in ["A","E","I","O","U","L","N","R","S","T"]:
            score += 1
        elif letter == letter in ["D","G"]:
            score += 2
        elif letter == letter in ["B","C","M","P"]:
            score += 3
        elif letter == letter in ["F","H","V","W","Y"]:
            score += 4
        elif letter == "K":
            score += 5
        elif letter == letter in ["J","X"]:
            score += 8
        elif letter == letter in ["Q","Z"]:
            score += 10
        
    #Lastly, checking to see if that word's length = bonus :)
    if len(word) >= 7:
        score += 8
    return score

#scores.sort(reverse = True)
    #word_list.sort(reverse = True)
    #words_and_scores = zip(word_list, scores)
    #best_word = [word for words in words_and_scores for word in words]
def get_highest_word_score(word_list):
    #Calling scores to make scores for each word in list!
    scores = [score_word(word) for word in word_list]
    words = [word for word in word_list]
    #Zipping them in a new list
    high_scores = {word:score for (word,score) in zip(words,scores)}
    #make best_word into an empty list!
    best_word = []
    max_word = max(high_scores)
    max_score = high_scores.get(max_word)
    #for word in high_scores:
        #if len(max_word) <= len(word):
            #max_word = words[0]
    best_word.extend([max_word, max_score])
    return best_word
    

