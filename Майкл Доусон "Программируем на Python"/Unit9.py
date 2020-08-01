# Гибель пришельца
# Демонстрирует взаимодействие объектов
class Player(object):
    """Игрок в экшн игре"""
    def blast(self, enemy):
        print("Игрок стреляет во врага\n")
        enemy.die()
class Alien(object):
    """Враждебный пришелец-инопланетянин в экшн-игре"""
    def die(self):
        print("Ну вот и все спета моя песенка. \n" \
        "Уже и в глазах темнеет... Передай полутора миллионам моих личинок. что я любил их\n",  "Прощай безжалостный мир " )
        
print("Гибель пришельца")
hero = Player()
invader = Alien()
hero.blast(invader)


# Карты
# Демонстрирует сочетание объектов
class Card(object):
    """Одна игральная карта"""
    RANKS = ["А", "2", "З", "4", "5", "6", "7", "В", "9", "10", "J", "Q", "К"]
    SUITS = [ "c", "d", "h", "s" ]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep
    
class Hand(object):
    """Рука - набор карт на руках у одного игрока"""
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + ""
        else:
            rep = "<пусто"
        return rep
    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
    
    
card1 = Card(rank="A",suit="c")
card2 = Card(rank="2",suit="c")
card3 = Card(rank="3",suit="c")
card4 = Card(rank="4",suit="c")
card5 = Card(rank="5",suit="c")
print(card1)
print(card2)
print(card3)
print(card4)
print(card5)
my_hand = Hand()
print("Печатаю карты на руках до раздачи")
print(my_hand)
my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("Печатаю краты на руках после раздачи")
print(my_hand)
#my_hand.clear()
#print("Печатаю краты на руках после cброса")
print(my_hand)

your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("Первые 2 из моих карт я передал вам")
print("Теперь у вас на руках")
print(your_hand)
print("А у меня на руках")
print(my_hand)

# Карты 2.0
# Демонстрирует расширение класса через наследование
class Card(object):
    """Одна игральная карта"""
    RANKS = ["А", "2", "З", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "К"]
    SUITS = [ "c", "d", "h", "s" ]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep
    
class Hand(object):
    """Рука - набор карт на руках у одного игрока"""
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + ""
        else:
            rep = "<пусто"
        return rep
    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand): # класс - Deck настледуется от Hand
    """Колода игральных карт"""
    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Не могу больше сдавать карты закончились")

# основная часть
deck1 = Deck()
print(deck1)
deck1.populate()
print(deck1)
deck1.shuffle()
print(deck1)
my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck1.deal(hands, per_hand= 5)
print("В первой руке")
print(my_hand)
print("Во второй руке")
print(your_hand)

# Карты 3.0
# Демонстрирует наследование в части переопределения методов

class Card():
    """Одна игральная карта"""
    RANKS = ["А", "2", "З", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "К"]
    SUITS = [ "c", "d", "h", "s" ]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep

class UnprintableCard(Card):
    """Карта номинал и масть которой не могут быть выведены на экран"""
    def __str__(self):
        return "<нельзя напечатать>"
    
class PositionalCard(Card):
    """Карта которую можно положить лицом или рубашкой вверх"""
    def __init__(self, rank, suit, face_up = True):
        super(PositionalCard, self).__init__(rank, suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super(PositionalCard, self).__str__()
        else:
            rep = "XX"
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up
    
# основная часть
card1 = Card("A","c")
card2 = UnprintableCard("A","d")
card3 = PositionalCard("A", "h")

print(card1)

print(card2)

print(card3)

card3.flip()
print(card3)
