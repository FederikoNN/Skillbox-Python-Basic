import random


class Card:
    def __init__(self, suit, card_view, value):
        self.suit = suit
        self.value = value
        self.card_view = card_view

    def card_info(self):
        print(f'{self.card_view}-{self.suit}', end=' ')


class Deck:
    suits = ['пики', 'червы', 'бубны', 'трефы']
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
    cards_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'В': 10, 'Д': 10,
                    'К': 10, 'Т': 11}

    def __init__(self):
        self.deck = [Card(suit, card, self.cards_values[card]) for card in self.cards for suit in self.suits]

    def deck_info(self):
        for card in self.deck:
            card.card_info()

    def card_dealing(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def first_dealing(self):
        players_cards = []
        for _ in range(2):
            card = random.choice(self.deck)
            players_cards.append(card)
            self.deck.remove(card)
        return players_cards

# TODO, предлагаю реализовать игру полностью на классах,
#  Стоит перенести эту функцию в методы класса Игрок. И возможно, было бы правильней создать класс Игрок.
def player_cards_info(cards_list, unit='Игрок'):
    count = 0
    ace = 0
    print(f'У {unit}а на руках:')
    for card in cards_list:
        card.card_info()
        count += card.value
        if card.value == 11:
            ace += 1
    if count > 21 and ace > 0:
        count -= 10
        ace -= 1
    elif count > 21:
        print('\nПеребор! Вы проиграли!')
        return False
    elif count == 21:
        print(f'\n{unit} выиграл!')
        return False
    print('\nКоличество очков: ', count)
    return count


while True:
    deck_deal = Deck()
    player = deck_deal.first_dealing()
    dealer = deck_deal.first_dealing()
    count_player = player_cards_info(player)
    while True:
        if not count_player:
            break
        choice = input('Добавить карту? (да/нет): ')
        if choice.lower() == 'да':
            player.append(deck_deal.card_dealing())
            count_player = player_cards_info(player)
        elif choice.lower() == 'нет':
            count_dealer = player_cards_info(dealer, 'Дилер')
            if count_player > count_dealer:
                print('Вы выиграли!')
            elif count_player < count_dealer:
                print('Вы проиграли!')
            else:
                print('Ничья!')
            break
        else:
            print('Ошибка выбора!')
    input()
