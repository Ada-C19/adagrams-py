# ======================== Wave 1- TEST ONE ========================
# First task is to build a hand of 10 letters for the user
# Need to set a variable for the pool pf letters:

# First thought is to build a dictionary, bc of the table


# LETTER_POOL = {
#     'A': 9, 
#     'B': 2, 
#     'C': 2, 
#     'D': 4, 
#     'E': 12, 
#     'F': 2, 
#     'G': 3, 
#     'H': 2, 
#     'I': 9, 
#     'J': 1, 
#     'K': 1, 
#     'L': 4, 
#     'M': 2, 
#     'N': 6, 
#     'O': 8, 
#     'P': 2, 
#     'Q': 1, 
#     'R': 6, 
#     'S': 4, 
#     'T': 6, 
#     'U': 4, 
#     'V': 2, 
#     'W': 2, 
#     'X': 1, 
#     'Y': 2, 
#     'Z': 1
# }

# learned that there are ways to use dictionaries for frequency mapping

# learned about a dict sublass, counter
# counters are a great way to do fast tallies
# elements are stored as keys, their counts are stored as values

# To randomly select a key from a dictionary:
# https://www.moonbooks.org/Articles/How-to-select-randomly-keys-from-a-dictionary-in-python-3-/ 

# Which is great but, should reflect the distribution of letters
# a list just seems like a better choice 
# if all we need to do is pull 10 elements from the array, try using a list

LETTER_POOL  = [ 
                "A", "A", "A","A", "A", "A", "A", "A", "A", 
                "B", "B", 
                "C", "C", 
                "D", "D", "D", "D", 
                "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
                "F", "F", 
                "G", "G", "G", 
                "H", "H", 
                "I", "I", "I", "I", "I", "I", "I", "I", "I", 
                "J", 
                "K", 
                "L", "L", "L", "L", 
                "M", "M", 
                "N", "N", "N", "N", "N", "N", 
                "O", "O", "O", "O", "O", "O", "O", "O", 
                "P", "P", 
                "Q", 
                "R", "R", "R", "R", "R", "R", 
                "S", "S", "S", "S", 
                "T", "T", "T", "T", "T", "T", 
                "U", "U", "U", "U", 
                "V", "V", 
                "W", "W", 
                "X", 
                "Y", "Y", 
                "Z"]

# takes a while to type out, 
# but visually it's easier to see the frequency of the letters
# assuming at the moment we'll need to shuffle the letter pool bc lists are ordered

# letters[0] to get the value of the item in the list by its position
# random.choice(letters) - something to try

def draw_letters():
    pass
    # first test says draw letters draw 10
    # so when this function is called, 
    # it needs to return an array of 10 strings:
        # each string is exactly one letter
    # hand_of_letters = ["O", "N", "E", "S", "T", "R", "I", "M","G","A"]
    
    # letters are randomly drawn from a pool of letters
    # letter = random.choice(pool_of_letters)
    # randoM()
    

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass