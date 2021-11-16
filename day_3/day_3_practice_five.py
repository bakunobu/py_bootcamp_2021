def letter_counter(names:list, letters:list) -> int:
    total = 0
    for letter in letters:
        print(f'{letter} occurs {names.count(letter.lower())} times ')
        total += names.count(letter.lower())
    return(total)


def name_to_list(name:str) -> list:
    first_name, last_name = name.split(' ')
    name_list = [letter.lower() for letter in list(first_name)+list(last_name)]
    return(name_list)


def calculator(value_1:int, value_2:int) -> int:
    return(value_1 * 10 + value_2)


def main():
    name_one = input('Type first persons\' name in: ')
    name_two = input('Type second persons\' name in: ')
    names = name_to_list(name_one) + name_to_list(name_two)
    value_1 = letter_counter(names, ['T', 'R', 'U', 'E'])
    value_2 = letter_counter(names, ['L', 'O', 'V', 'E'])
    score = calculator(value_1, value_2)
    if score < 10 or score > 90:
        print(f"Your score is {score}, yo go together like coke and mentos.")
    elif 40 < score < 50:
        print(f'Your score is {score}, you are alright together.')
    else:
        print(f'Your score is {score}.')
        
        
main()



