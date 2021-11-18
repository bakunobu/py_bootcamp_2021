espresso = {'water':50,
            'coffee': 18,
            'price': 1.50,}


latte = {'water': 50,
         'coffee': 24,
         'milk': 150,
         'price': 2.50,}


cappuccino = {'water': 50,
              'coffee': 24,
              'milk': 150,
              'price': 3.00,}


tastes = {'espresso': espresso,
          'latte': latte,
          'cappuccino': cappuccino,}


supplies = {'water': 300,
            'milk': 200,
            'coffee': 100,
            'money': 0,}


coins = {'penny': 0.01,
         'nickel': 0.05,
         'dime': 0.1,
         'quarter': 0.25,}


# print report
def print_report() -> None:
    print('Stocks:')
    print(f'Water: {supplies.get("water")}')
    print(f'Milk: {supplies.get("milk")}')
    print(f'Coffee: {supplies.get("coffee")}')
    print(f'Money: {supplies.get("money")}')
    

def get_order(msg:str, options:str) -> str:
    while 1:
        a = input(msg).lower()
        if a == 'report':
            print_report()
        elif a in options:
            return(a)
        else:
            print('Choose one of available drinks')
            
            
def int_input(msg:str) -> int:
    while 1:
        try:
            a = int(input(msg))
            if a >= 0:
                return(a)
        except ValueError:
            print('Use positive integers only!')


def check_resources(order:str):
    not_available = []
    for k, v in tastes[order].items():
        if k == 'price':
            continue
        else:
            if supplies.get(k) < v:
                not_available.append(k)
    if not_available:
        return(not_available)
    else:
        return(False)


def take_coins(price:float) -> float:
    total = 0
    q = int_input('How many quarters?: ')
    total += q * coins.get('quarter')
    d = int_input('How many dimes?: ')
    total += d * coins.get('dime')
    n = int_input('How many nickels?: ')
    total += n * coins.get('nickel')
    p = int_input('How many pennies?: ')
    total += p * coins.get('penny')

    if total > price:
        print(f'Here is {round(total - price, 2)} in change.')
        return(round(total - price, 2))
    elif total < price:
        print('Sorry that\'s not enough money. Money refunded')
        return(None)
    else:
        return(price)


def update_resources(order:str) -> None:
    supplies['money'] += tastes.get(order).get('price', 0)
    supplies['water'] -= tastes.get(order).get('water', 0)
    supplies['milk'] -= tastes.get(order).get('milk', 0)
    supplies['coffee'] -= tastes.get(order).get('coffee', 0)
    

def main():
    while 1:
        msg = 'What would you like? (espresso/latte/cappuccino): '
        options = ('espresso', 'latte', 'cappuccino', 'q')
        order = get_order(msg=msg, options=options)
        if order == 'q':
            print('Shutting down!')
            break
        else:
            if check_resources(order):
                print('Sorry there is not enough:', end=' ')
                print(* check_resources(order), sep=', ', end='.\n')
            else:
                if take_coins(tastes.get(order).get('price')) is not None:
                    update_resources(order)                    
                    print(f'Here is your {order}! Enjoy')
                else:
                    continue
                
                
if __name__ == '__main__':
    main()
# print(tastes.get('cappuccino').get('price'))
# print(tastes.get('latte').get('price'))
# print(tastes.get('espresso').get('price'))