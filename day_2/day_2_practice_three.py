def get_int_input(msg:str) -> int:
    while 1:
        try:
            i = int(input(msg))
            if 0 < 91:
                return(i)
            else:
                print('A number must be a positive integer!')        
        except ValueError:
            print('Use only integers!')


def calc_d_w_m(max_age:int=90) -> None:
    msg = 'What is your current age? '
    curr_age = get_int_input(msg)
    age_diff = max_age - curr_age
    d = age_diff * 365
    w = age_diff * 52
    m = age_diff * 12
    print(f'you have {d} days, {w} weeks and {m} months left!')
    

calc_d_w_m()
            
