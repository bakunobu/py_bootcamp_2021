#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

def guess_a_letter() -> str:
    while 1:
        guess = input('Type in your guess:\n>>> ')
        if guess.isalpha():
            if len(guess) == 1:
                return(guess)
            else:
                print('Must be a single letter!')
        else:
            print('Must be a letter, not a number or a symbol')

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
def is_in(my_word:str, letter:str) -> bool:        
    return(letter in my_word)

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
def display(my_word:str, letter:str=None) -> None:
    guess_mode = ['_' if _ != letter else letter for _ in list(my_word) ]
    print(* guess_mode)
    
my_guess = guess_a_letter()
if is_in(list(chosen_word), my_guess):
    display(chosen_word, my_guess)
    
    
