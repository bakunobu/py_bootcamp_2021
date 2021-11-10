rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random


graphics = {0: rock,
            1: paper,
            2: scissors}


def resulting(a:int, b:int) -> str:
    """
    represents outcomes.
    a - for player,
    b - for computer.
    Returns result from position of player.
    """
    if a == 0:
        if b == 0:
            return('tie')
        elif b == 1:
            return('lose')
        else:
            return('win')
    elif a == 1:
        if b == 0:
            return('win')
        elif b == 1:
            return('tie')
        else:
            return('lose')
    else:
        if b == 0:
            return('lose')
        elif b == 1:
            return('win')
        else:
            return('tie')


def int_input(msg:str, options:tuple=(0,1,2)) -> int:
    while 1:
        try:
            a = int(input(msg))
        except ValueError:
            print('Use integers!')
        else:
            if a in options:
                return(a)
            
            
def main_loop() -> None:
    user_answer = int_input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n>>> ')
    ai_answer = random.randint(0,2)
    print(graphics.get(user_answer))
    print('Computer chose:')
    print(graphics.get(ai_answer))
    print(f'You {resulting(user_answer, ai_answer)}')

        
for _ in range(10):
    main_loop()
    