def is_prime(n:int) -> bool:
    if n <= 3:
        return(True)
    for x in range(2, int(n**0.5) + 1):
        if not n % x:
            return(False)
    else:
        return(True)
    
    
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
    msg = 'Check this number: '
    num = get_int_input(msg)
    if is_prime(num):
        print(f'{num} is a prime number!')
    else:
        print(f'{num} is a not prime number!')