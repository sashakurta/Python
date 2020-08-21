# Война
# все игроки тянут по одной карте
# выигрывает тот у кого номинал карты самый большой
import cards, games
class War_Card(cards.Card):
    """Карты для игры в Войну"""
    ACE_VALUE = 1
    @property
    def value(self):
        if self.is_face_up:
            v = War_Card.RANKS.index(self.rank)+1
            if v > 10:
                v = 10
        else:
            v = None
        return v
class War_Deck(cards.Deck):
    """Колода для игры в блек-джек"""
    def populate(self):
        for suit in War_Card.SUITS:
            for rank in War_Card.RANKS:
                self.cards.append(War_Card(rank, suit))
class War_Hand(cards.Hand):
    """Рука одного игрока"""
    def __init__(self, name):
        super(War_Hand, self).__init__()
        self.name = name
    def __str__(self):
        rep = self.name + "\t" + super(War_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total)+ ")"
        return rep
    @property
    def total(self):
        t = 0
        for i in self.cards:
            t += i.value
        return t

class War_Game(object):
    """Игра в блек-джек"""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = War_Hand(name)
            self.players.append(player)
        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()
    def play(self):
        if len(self.deck.cards) < 26:
            self.deck.clear()
            self.deck.populate()
            self.deck.shuffle()
        self.deck.deal(self.players)
        totals = {}
        for player in self.players:
            print(player, end=' ')
            print(player.total)
            totals[player.total] = player.name
        print("Выиграл")
        print(totals[max(totals.keys())])
        

def main():
    print("\t\tДобро пожаловать за игровой стол Войны!")
    names = []
    number = None
    while number == None:
        try:
            number = games.ask_number("Сколько всего игроков (2 - 7) ", low = 2, high = 7)
        except:
            print("Введите число")
    for i in range(number):
        name = input("Введите имя игрока ")
        names.append(name)
        print()
    game = War_Game(names)
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("Хотите сыграть еще раз ")
        
main()
