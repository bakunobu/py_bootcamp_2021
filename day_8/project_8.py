import string




# PART 1. Encryption
def encryption(letter:str, shift:int=8) -> str:
    shift %= 52
    return(chr(ord(letter)+shift))



def encrypt(phrase:str, shift:int=8) -> str:
    phrase = list(phrase)
    encrypted_phrase = [encryption(letter, shift) for letter in phrase]
    return(''.join(encrypted_phrase))


# print(encrypt('hello', 9))

# PART 2. Decription
def decryption(letter:str, shift:int=8) -> str:
    shift %= 52
    return(chr(ord(letter)-shift))


def decrypt(phrase:str, shift:int=8) -> str:
    phrase = list(phrase)
    decrypted_phrase = [decryption(letter, shift) for letter in phrase]
    return(''.join(decrypted_phrase))


init_phrase = 'My name is Stephen HunTer'
my_shift = 7
encr_phrase = encrypt(init_phrase, my_shift)
decr_phrase = decrypt(encr_phrase, my_shift)
print(decr_phrase)

