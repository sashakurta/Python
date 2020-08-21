# Моя зверюшка
# Виртуальный питомец. о котором пользователь может заботиться
class Critter(object):
    """Виртуальный питомец"""
    def __str__(self):
        rep = "Меня зовут "+ self.name + "\nЯ чувствую себя " + self.mood
        rep += "\nМой уровень голода "+ str(self.hunger) +"\nМой уровень усталости " + str(self.boredom)
        return rep
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self):
        """закрытый метод робота которого увеличивать уровень голода
        и униния"""
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m
    def talk(self):
        print("Меня зовут", self.name, "и сейчас я чувствую себя", self.mood, "\n")
        self.__pass_time()
    def eat(self, food = 5):
        print("Мрр...Спасибо")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, fun = 5):
        print("Уии")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
    
def main():
    num = int(input("Введите количество зверушек"))
    creatures = []
    while num > 0:
        crit_name = input("Как вы назовете зверушку?")
        crit = Critter(crit_name)
        creatures.append(crit)
        num -= 1
    choice = None
    while choice != 0:
        print("""
        Моя зверюшка
        0 - Выйти
        1 - Узнать о самчувстивии зверюшек
        2 - Покормить зверушек
        3 - Поиграть со зверюшками
        """)
        choice = input("Ваш выбор ")
        if choice == "0":
            print("До свидания")
        elif choice == "1":
            for crit in creatures:
                crit.talk()
        elif choice == "2":
            food = 0
            try:
                food = int(input("Введите на сколько еды скормить зверушкам(1-15)"))
                for crit in creatures:
                    crit.eat(food)
            except ValueError:
                 print("ВВЕДИТЕ ЧИСЛО")
            
        elif choice == "3":
            boredom = 0
            try:
                boredom = int(input("Введите сколько минут хотите поиграть со зверушкой"))
                for crit in creatures:
                    crit.play(boredom)
            except ValueError:
                print("ВВЕДИТЕ ЧИСЛО")
        elif choice == "1975":
            for crit in creatures:
                print(crit)
        else:
            print("Извините, нет пункта в меню")

main()
