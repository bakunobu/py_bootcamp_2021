import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

new_word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
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
            
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
def is_in(my_word:list, letter:str) -> bool:
    return(letter in my_word)

my_guess = guess_a_letter()
print(is_in(list(new_word),
            my_guess))