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


class Player:
    def __init__(self, cards_list, name='Игрок'):
        self.name = name
        self.cards_list = cards_list

    def player_cards_info(self):
        count = 0
        ace = 0
        print(f'У {self.name}а на руках:')
        for card in self.cards_list:
            card.card_info()
            count += card.value
            if card.value == 11:
                ace += 1
        if count > 21 and ace > 0:
            count -= 10
            ace -= 1
        if count > 21:
            print('\nПеребор! Вы проиграли!')
            return False
        elif count == 21:
            print(f'\n{self.name} выиграл!')
            return False
        print('\nКоличество очков: ', count)
        return count

    def add_card(self, card):
        self.cards_list.append(card)


while True:
    deck_deal = Deck()
    player_deal = deck_deal.first_dealing()
    dealer_deal = deck_deal.first_dealing()
    player = Player(player_deal)
    dealer = Player(dealer_deal, 'Дилер')
    count_player = player.player_cards_info()
    while True:
        if not count_player:
            break
        choice = input('Добавить карту? (да/нет): ')
        if choice.lower() == 'да':
            player.add_card(deck_deal.card_dealing())
            count_player = player.player_cards_info()
        elif choice.lower() == 'нет':
            count_dealer = dealer.player_cards_info()
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

# зачёт!
