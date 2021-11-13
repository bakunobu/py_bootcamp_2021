#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# chosen_word = random.choice(word_list)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

def guess_a_letter(used_letters:list) -> str:
    while 1:
        guess = input('Type in your guess:\n>>> ')
        if guess.lower() in used_letters:
            print('You\'ve used this one already!')
        elif guess.isalpha():
            if len(guess) == 1:
                return(guess.lower())
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
def display(my_word:str, letters:list) -> None:
    guess_mode = ['_' if letter not in letters else letter for letter in list(my_word) ]
    print(* guess_mode)
    
    
#TODO-4: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.



def game_loop():
    lives = 6
    chosen_word = random.choice(word_list)
    print(f'Pssst, the solution is {chosen_word}.')
    letters = set(list(chosen_word))
    guessed_letters = []
    used_letters = []
    while len(set(chosen_word)) > len(guessed_letters) and lives > 0:
        my_guess = guess_a_letter(used_letters)
        used_letters.append(my_guess)
        if is_in(list(chosen_word), my_guess):
            guessed_letters.append(my_guess)
            print('Right!')
            
        else:
            lives -= 1
            print('Wrong!')
            print(f'Be careful, {lives} lives left!')
        display(chosen_word, guessed_letters)
        print(stages[lives])
        print(* used_letters, sep=', ')
    if lives > 0:
        print('Done!')
    else:
        print('You lose!')


game_loop()
