#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

from typing import Union

def get_numerical_input(msg:str, if_float:bool=False) ->  Union[int, float]:
    if if_float:
        while 1:
            try:
                my_input = int(input(msg))
            except ValueError:
                print('Use integers!')
            else:
                return(my_input)

    else:
        while 1:
            try:
                my_input = float(input(msg))
            except ValueError:
                print('Use numeric values!')
            else:
                return(my_input)
    



def count_tips(total:float, tip:float, num_people:int) -> None:
    tips = total / num_people * (1 + tip / 100)
    print(f'Each person should pay: {tips:.2f}')
    
    
def tip_calculator() -> None:
    total_bill = get_numerical_input('What\'s your total?\n>>> ', True)
    num_people = get_numerical_input('How many people have this meal?\n>>> ')
    tip_size = get_numerical_input('What\'s tip size (in %)?\n>>> ', True)
    count_tips(total_bill, tip_size, num_people)
    
    
if __name__ == '__main__':
    tip_calculator()
    
