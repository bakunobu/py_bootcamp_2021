def get_int_input(msg:str) -> int:
    while 1:
        try:
            i = int(input(msg))
            if is_two_digit(i):
                return(i)
            else:
                print('A number must be a two digit!')        
        except ValueError:
            print('Use only integers!')


def is_two_digit(num:int) -> bool:
    return(9 < num < 100)


def get_digits(num:int) -> tuple:
    dec = num // 10
    units = num % 10
    return(dec, units)


def print_sum() -> None:
    msg = 'Type a two digit number: '
    num = get_int_input(msg)
    sum_dig = sum(get_digits(num))
    print(f'A sum of digits of {num} is {sum_dig}!')
    
    
print_sum()