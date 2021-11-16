import string

alph = list(string.ascii_lowercase)

direction = 'Type \'encode\' to encrypt, type \'decode\' to decrypt:\n'

def choose_text_option(msg:str, options:list) -> str:
    while 1:
        a = input(msg).lower()
        if a in options:
            return(a)
        

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


        
def main_menu() -> None:
    opt_1 = choose_text_option()
    if opt_1 == 'encode':
        msg = input('Type your message:\n').lower()
        shift = get_int_input('Type the shift number:\n')
        encrypt(msg, shift)
    else:
        pass


def encrypt(msg:str, shift:int) -> str:
    # msg = list(msg.replace(' ', ''))
    msg = list(msg)
    for i in range(len(msg)):
        s = shift 
        ind = alph.index(msg[i])
        if ind + s > len(alph):
            s = (ind + s) % len(alph)
            msg[i] = alph[s]
        else:
            msg[i] = alph[s+ind]
    return(''.join(msg))


print(encrypt('hello', 5))