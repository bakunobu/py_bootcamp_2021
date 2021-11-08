#1. Create a greeting for your program.
def greetings() -> None:
    print('Welcome to the Band Name Generator!\nFollow simple instructions to get your band\'s name.')
#2. Ask the user for the city that they grew up in.
def base_input(msg:str) -> str:
    my_input = input(msg)
    return(my_input.title())

def get_city_name() -> str:
    msg = 'What\'s the city that you grew up?\n>>> '
    return(base_input(msg=msg))

#3. Ask the user for the name of a pet.

def get_pet_name() -> str:
    msg = 'What\'s your pet\'s name?\n>>> '
    return(base_input(msg=msg))

#4. Combine the name of their city and pet and show them their band name.
def generate_band_name() -> None:
    greetings()
    city = get_city_name()
    pet = get_pet_name()
    print(f'Your band name could be: {city} {pet}!')


if __name__ == '__main__':
    generate_band_name()
