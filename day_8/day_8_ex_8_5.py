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
    msg = input('Type your message:\n').lower()
    shift = get_int_input('Type the shift number:\n')


def ceasar(text:str, shift:int, direction:str) -> str:
    shift %= len(alph)
    msg = list(text.replace(' ', ''))
    for i in range(len(msg)):
        s = shift 
        ind = alph.index(msg[i])
        if direction == 'encode':
            if ind + s > len(alph):
                s = (ind + s) - len(alph)
                msg[i] = alph[s]
            else:
                msg[i] = alph[s+ind]
        else:
            if ind - s < 0:
                s = len(alph) - (ind - s)
                msg[i] = alph[s]
            else:
                msg[i] = alph[ind - s]
    return(''.join(msg))
    
print(ceasar('mjqqt', 5, 'decode'))