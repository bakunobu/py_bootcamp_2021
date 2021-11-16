def fiz_buzz() -> None:
    for x in range(1, 101):
        if not x % 3:
            if not x % 5:
                print('FizzBuzz')
            else:
                print('Fizz')
        elif not x % 5:
            print('Buzz')
        else:
            print(x)
            
            
fiz_buzz()