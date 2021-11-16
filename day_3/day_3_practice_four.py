def text_input(msg, options:list=None) -> str:
    while 1:
        answer = input(msg).upper()
        if options:
            if answer in options:
                return(answer)
            else:
                print('Wrong input!')
                print('Choose from:')
                print(* options, sep=', ')
        else:
            return(answer)
    

def pizza_order() -> float:
    sizes  = {'S':0,
              'M':0,
              'L':0}


    
    size = text_input('What size do you want? S, M or L: ', ['S', 'M', 'L'])
    sizes[size] += 1
    
    extra_pepp = text_input('Do you want pepperoni? Y or N: ', ['Y', 'N']) == 'Y'
    
    extra_cheese = text_input('Do you want extra cheese? Y or N: ', ['Y', 'N']) == 'Y'

    total = 15 * sizes['S'] + 20 * sizes['M'] + 25 * sizes['L']
    if extra_pepp:
        total += 2 * sizes['S'] + 3 * sizes['M'] + 3 * sizes['L']
    if extra_cheese:
        total += 1
    print(f"Your final bill is: ${total}")
    
    
def main() -> None:
    print('Welcome to Python Pizza Deliveries!')
    pizza_order()
    
    
    
if __name__ == '__main__':
    main()