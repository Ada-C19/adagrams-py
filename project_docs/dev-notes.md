so i might want to start with a dictionary. wrap it inside a tuple to be safe.

letters_tuple = ( {A: 9,
    B: 2,
    N: 2,
    etc})

then in the code, you run a loop that creates a list full of all the letters.

def make_letter_string(letters_tuple):
    letters_dict = letters_tuple[0]
    for letter, frequency in letters_dict.items:

....

OK!

so.

in your draw_letters() function.

initialize a hand variable.
    (so... hand = [])
take the letter_pool_list.

*** LOOP BEGINS ***
return a random number based on the length of that list, set to a variable.
    (so... letter_selection = random.randint(0, len(letter_pool_list)))
then pick the letter item based on the random number, add it to hand
    (so... hand.append(letter_pool_list[letter_selection]))
then remove that letter from the letter_pool_list.
    (so... del letter_pool_list[letter_selection])

OK....

## WAVE 2 !!!

here you are going to do stuff with sets.

begin by turning word into a list. you do this with a loop.

so, first, initialize the list.
    (so... word_letters = [])
then, iterate through the string.
so...
for letter in word:
    word_letters.append[letter]

oh. no.
do it this way:

for letter in word:
    if letter not in letter_bank:
        return False
    elif letter in letter_bank:
        letter_bank.remove(letter)
return True