from typing import Union
import math


def calc_paint_cans(h:Union[int, float],
                    w:Union[int, float],
                    coverage:float=5.0) -> int:
    area = h * w
    return(math.ceil(area / coverage))


def get_int_input(msg:str) -> int:
    while 1:
        try:
            a = int(input(msg))
            if a > 0:
                return(a)
            else:
                print('Use positive integers!')
        except ValueError:
            print('Only positive intgers allowed!')
            
            
def main():
    test_h = get_int_input('Heigth of wall: ')
    test_w = get_int_input('Width of wall: ')
    cans = calc_paint_cans(test_h, test_w)
    print(f'You\'ll need {cans} cans of paint.')

main()