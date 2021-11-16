import random


def get_input(msg:str) -> list:
    name_list = input(msg).split(',')
    return(name_list)


def banker_roulette() -> None:
    msg = 'Who is having a meal today: (use \',\' as separator): '
    name_list = get_input(msg)
    winner = random.choice(name_list)
    print(f'{winner.lstrip()} is going to buy the meal today!')
    
    
    
banker_roulette()


