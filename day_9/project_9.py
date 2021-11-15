
import os
import time
from art import logo



def string_question(msg:str, options:tuple=None) -> str:
    while 1:
        a = input(msg).lower()
        if options:
            if a in options:
                return(a)
            else:
                print('Type in \'yes\' or \'no\'!')
        else:
            return(a)


def int_question(msg:str) -> int:
    while 1:
        try:
            a = abs(int(input(msg)))
        except ValueError:
            print('Use integers!')
        else:
            return(a)


clear_screen = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def main_loop() -> None:
    bids = dict()
    print(logo)
    time.sleep(1)
    while 1:
        clear_screen()
        name = string_question('What is your name? ')
        bid = int_question('What\'s your bid?: $ ')
        bids[name] = bid
        if string_question('Are there any other bidders? Type \'yes\' or \'no\' ',
                           ('yes', 'no')) == 'no':
            break
        
    clear_screen()
    bidders = [(k, v) for k, v in bids.items()]
    bidders.sort(key=lambda x: x[1], reverse=True)
    print(f'The winner is {bidders[0][0].title()} with a bid of ${bidders[0][1]}')


if __name__ == '__main__':
    main_loop()
    