import random
import os


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


cards = {'A': 11,
         '2': 2,
         '3': 3,
         '4': 4,
         '5': 5,
         '6': 6,
         '7': 7,
         '8': 8,
         '9': 9,
         '10': 10,
         'J': 10,
         'Q': 10,
         'K': 10}


deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def count_cards(hand:list) -> int:
    total = sum(cards.get(card) for card in hand)
    if total > 21:
        total -= 10 * hand.count('A')
    return(total)


def show_cards(hand:list, is_dealer=False) -> None:
    print('\tCards: ', end=' ')
    if is_dealer:
        print(hand[0], 'X', end=', ')
        print('current score: ', end=' ')
        print(count_cards([hand[0],]))
    else:
        print(* hand, sep=' ', end=', ')
        print('current score: ', end=' ')
        print(count_cards(hand))
        
        
def deal(num_cards:int=2) -> list:
    return(random.sample(deck, num_cards))


def hit_me():
    msg = 'Type \'y\' to get another card, type \'n\' to pass: '
    while 1:
        answer = input(msg).lower()
        if answer in ('y', 'n'):
            return(answer == 'y')
        else:
            print('Use \'y\' for Yes and \'n\' for No!')
            

def wanna_play():
    msg = 'Do you want to play a game of Blackjack?'
    while 1:
        answer = input(msg+'Type \'y\' or \'n\': ').lower()
        if answer in ('y', 'n'):
            return(answer == 'y')
        else:
            print('Use \'y\' for Yes and \'n\' for No!')


def quit():
    while 1:
        answer = input('Wanna play one more round?: ').lower()
        if answer in ('y', 'n'):
            return(answer == 'n')
        else:
            print('Use \'y\' for Yes and \'n\' for No!')


def shuffle(player_score:int=20) -> None:
    print(logo)
    game_score = player_score
    while game_score > 0:
        player_hand = deal()
        dealer_hand = deal()
        print('\tPlayer\'s hand')
        show_cards(player_hand)
        print('\tDealer\'s hand')
        show_cards(dealer_hand, True)
        if count_cards(player_hand) == 21:
            if count_cards(dealer_hand) == 21:
                print('Draw!')
            else:
                print('Player wins!')
                game_score += 1
        else:
            while 1:
                if hit_me():
                    player_hand += deal(1)
                    print('\tPlayer\'s hand')
                    show_cards(player_hand)
                    if count_cards(player_hand) > 21:
                        print('Dealer wins!')
                        game_score -= 1
                        break
                else:
                    print('\tDealers\'s hand')
                    show_cards(dealer_hand)
                    while count_cards(dealer_hand) < 17:
                        dealer_hand += deal(1)
                        print('\tDealers\'s hand')
                        show_cards(dealer_hand)
                    if count_cards(dealer_hand) > 21:
                        print('Player wins!')
                        game_score += 1
                        break
                    elif count_cards(player_hand) < count_cards(dealer_hand):
                        print('Dealer wins!')
                        game_score -= 1
                        break
                    elif count_cards(dealer_hand) < count_cards(player_hand):
                        print('Player wins!')
                        game_score += 1
                        break
                    else:
                        print('Draw!')
                        break
        print(f'Player\'s score is {game_score}!')
        if quit():
            print(f'Final score is {game_score}!')
            break
        else:
            print('Starting next round!')
        clear_screen()
    else:
        print('Player have no more points to play for!')
        

if wanna_play():
    shuffle()
