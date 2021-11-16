# BMI - body mass index


def get_float_input(msg) -> float:
    while 1:
        try:
            f = float(input(msg))
            if f > 0:
                return(f)
            else:
                print('Input must be a positive float!')
        except ValueError:
            print('Use only floating point numbers!')



def get_ratio() -> float:
    h_msg = 'Enter your height in m: '
    w_msg = 'Enter your weight in kg: '
    h = get_float_input(h_msg)
    w = get_float_input(w_msg)
    return(w / h ** 2)



def eval_bmi(bmi:float) -> None:
    print(f'Your BMI is {round(bmi, 1)} which means', end=' ')
    if bmi < 18.5:
        print('Underweight!')
    elif bmi < 25:
        print('Normal weight!')
    elif bmi < 30:
        print('Owerweight!')
    else:
        print('Obese!')
        
        
def calc_bmi() -> None:
    bmi = get_ratio()
    eval_bmi(bmi)
    
    
calc_bmi()