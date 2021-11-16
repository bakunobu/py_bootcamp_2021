import random


def coin_toss() -> None:
    my_dict = {1:'Heads',
            0:'Tails'}
    
    
    cast = random.randint(0,1)
    print(my_dict.get(cast, 2))
    
    
    
for x in range(10):
    coin_toss()