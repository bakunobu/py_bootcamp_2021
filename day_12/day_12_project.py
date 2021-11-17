import random


welcome_msg = 'Welcome to the Number Guessing Game!'
task_msg = 'I\'m thinking of a number between 1 and 100.' 

def option_input(msg:str, options:tuple=None) -> str:
    while 1:
        a = input(msg).lower()
        if options:
            if a in options:
                return(a)
            else:
                print('Options availabe: ', end=' ')
                print(* options, sep=', ')
        else:
            return(a)


def int_input(msg:str, start:int=None, end:int=None) -> int:
    while 1:
        try:
            a = int(input(msg))
        except ValueError:
            print('Use integers.')
        else:
            if start and end:
                if start <= a <= end:
                    return(a)
                else:
                    print(f'Your guess must be between {start} and {end}')
            else:
                return(a)


def game_logic() -> None:
    print(welcome_msg)
    print(task_msg)
    
    task_num = random.randint(1,100)
    
    
    dif_q = 'Choose a difficulty. Type \'easy\' or \'hard\': '
    diff = option_input(dif_q, ('easy', 'hard',))
    
    attempts = None
    att_msg = 'You have {} remaining to guess a number.'
    
    cont_msg = 'Try again'
    
    input_msg = 'Make a guess: '
    
    if diff == 'hard':
        attempts = 5
    else:
        attempts = 10
    print(att_msg.format(attempts))
    while attempts > 0:
        guess = int_input(input_msg, 1, 100)
        if guess == task_num:
            print('You win!')
            break
        else:
            attempts -= 1
            if guess > task_num:
                print('Too high.')
            else:
                print('Too low.')
            
            print(cont_msg)
            print(att_msg.format(attempts))
    else:
        print('You\'ve run out of guesses, you lose.')
        
        
game_logic()
        