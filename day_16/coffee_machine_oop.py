# Variables
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


# Functions
def int_input(msg:str) -> int:
    while 1:
        try:
            a = int(input(msg))
            if a >= 0:
                return(a)
        except ValueError:
            print('Use positive integers only!')


# Classes
class CoffeeMachine():
    def __init__(self, name:str, tastes:dict, resources:dict) -> None:
        self.name = name
        self.tastes = tastes
        self.resources = resources
        self.options = ('espresso', 'latte', 'cappuccino', 'q', 'report')
    
        
    def print_resources(self):
        print('Stocks:')
        print(f'Water: {self.resources.get("water")}')
        print(f'Milk: {self.resources.get("milk")}')
        print(f'Coffee: {self.resources.get("coffee")}')
        print(f'Money: {self.resources.get("money")}')
    
    
    def check_resources(self, order:str) -> list:
        not_available = []
        for k, v in self.tastes[order].items():
            if k == 'price':
                continue
            else:
                if self.resources.get(k) < v:
                    not_available.append(k)
        if not_available:
            return(not_available)
        else:
            return(False)
        
    
    def process_coins(self, order:str) -> float:
        price = self.tastes[order].get('price', 0)
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
        
    
    def update_resources(self, order:str):
        self.resources['money'] += self.tastes.get(order).get('price', 0)
        self.resources['water'] -= self.tastes.get(order).get('water', 0)
        self.resources['milk'] -= self.tastes.get(order).get('milk', 0)
        self.resources['coffee'] -= self.tastes.get(order).get('coffee', 0)
    
    
    def get_order(self) -> None:
        msg = 'What would you like? (espresso/latte/cappuccino): '
        while 1:
            a = input(msg).lower()
            if a in self.options:
                return(a)
            else:
                print('Choose one of available drinks')
                
                
    def processing(self) -> None:
        while 1:

            order = self.get_order()
            if order == 'q':
                print('Shutting down!')
                break
            elif order == 'report':
                self.print_resources()
            else:
                if self.check_resources(order):
                    print('Sorry there is not enough:', end=' ')
                    print(* self.check_resources(order), sep=', ', end='.\n')
                else:
                    if self.process_coins(order) is not None:
                        self.update_resources(order)                    
                        print(f'Here is your {order}! Enjoy')
                    else:
                        continue
        

coffe_machine_1 = CoffeeMachine('mach1', tastes, supplies)


coffe_machine_1.processing()