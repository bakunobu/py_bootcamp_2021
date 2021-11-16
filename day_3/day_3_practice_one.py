def divided_by(num:int, div:int=2) -> bool:
    return(not num % div)


def odd_even_print(num:int) -> None:
    if not divided_by(num):
        print(f'{num} is an odd number!')
    else:
        print(f'{num} is an even number!')
        
        
def get_input(msg:str) -> int:
    while 1:
        try:
            a = int(input(msg))
            return(a)
        except ValueError:
            print('Only intger input allowed')
            
            
def main() -> None:
    msg ='Type in an integer: '
    num = get_input(msg)
    odd_even_print(num)
    
    
if __name__ == '__main__':
    main()