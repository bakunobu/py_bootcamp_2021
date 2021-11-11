import random, string


def int_input(msg:str) -> int:
    while 1:
        try:
            a = int(input(msg))
        except ValueError:
            print('Use integers!')
        else:
            return(abs(a))
            

def pypassword_generator() -> str:
    my_pass = []
    
    print('Welcome to PyPassword Generator!')
    q_1 = 'How many letters would you like in your password?\n'
    a_1 = int_input(q_1)
    
    my_pass += random.sample(list(string.ascii_letters), a_1)
    
    q_2 = 'How many symbols would you like?\n'
    a_2 = int_input(q_2)
    
    my_pass += random.sample(list(string.punctuation), a_2)
    
    q_3 = 'How many numbers would you like?\n'
    a_3 = int_input(q_3)
    
    my_pass += random.sample(list(string.digits), a_3)
    random.shuffle(my_pass)
    return(''.join(my_pass))


def main_loop() -> None:
    print(f'Here is yuor password: {pypassword_generator()}')
    
    
if __name__ == '__main__':
    main_loop()
