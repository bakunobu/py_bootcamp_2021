import os
from typing import Union
from art import logo

clear_screen = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def user_add(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    if abs(a + b  - int(a + b)) < 1e-10:
        return(int(a + b))
    else:
        return(a + b)


def user_subst(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    if abs(a - b  - int(a - b)) < 1e-10:
        return(int(a - b))
    else:
        return(a - b)


def user_prod(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    if abs(a * b  - int(a * b)) < 1e-10:
        return(int(a * b))
    else:
        return(a * b)


def user_div(a:Union[int, float], b:Union[int, float]) -> Union[int, float]:
    if abs(a / b  - int(a / b)) < 1e-10:
        return(int(a / b))
    else:
        return(a / b)
    
    
operations = {'+': user_add,
              '-': user_subst,
              '*': user_prod,
              '/': user_div}


def num_input(msg:str) -> Union[int, float]:
    while 1:
        try:
            a = float(input(msg))
        except ValueError:
            print('Only numbers allowed!')
        else:
            if abs(a) - int(a) < 1e-10:
                return(int(a))
            else:
                return(a)

            
def optional_input(msg:str, options:tuple=None) -> str:
    while 1:
        a = input(msg).lower()
        if options:
            if a in options:
                return(a)
            else:
                print('Use allowed options: ')
                print(* options, sep=', ')
        else:
            return(a) 


def main_loop() -> None:
    while 1:
        print(logo)
        more_actions = True
        value = 0
        first_num = 0 
        second_num = 0
        q_1 = 'What\'s the first number? '
        first_num = num_input(q_1)
        while more_actions:
            q_2 = 'Pick an operation: '
            print(* operations.keys(), sep='\n')
            my_operations = ('+', '-', '*', '/',)
            oper = optional_input(q_2, my_operations)
            oper_func = operations.get(oper)
            q_3 = 'What\'s next number? '
            second_num = num_input(q_3)
            value = oper_func(first_num, second_num)
            q_4 = f'Type \'y\' to continue calculating with {value}, or type \'n\' to start a new calculation: '
            answer = optional_input(q_4, ('y', 'n'))
            if answer == 'n':
                more_actions = False
                clear_screen()
            else:
                first_num = value
                
if __name__ == '__main__':
    main_loop()
        