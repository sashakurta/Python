# Просто зверюшка
# Демонстрирует простейшие класс и объект
class Critter(object):
    """Виртуальный питомец"""
    def talk(self):
        print("Привет. Я зверюшка - экземпляр класса")


crit = Critter()
crit.talk()

# Зверюшка с конструктором
# Демонстрирует
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self):
        print("Появилась новая зверюшка")
    def talk(self):
        print("\nПpивeт. Я зверюшка - экземпляр класса C r i t t e r . " )
# основная
critl = Critter()
crit2 = Critter()
critl.talk()
crit2.talk()

# Зверюшка с атрибутами
# Демонстрирует создание атрибутов объекта и доступ к ним
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверюшка")
        self.name = name
    def __str__(self):
        rep = "Обьект класса Crittre\n"
        rep += "имя: " + self.name + "\n"
        return rep
    def talk(self):
        print("Привет. Меня зовут", self.name, "\n")
        
crit1 = Critter("Бобик")
crit1.talk()
crit2 = Critter("Мурзик")
crit2.talk()
print("Вивод обьекта crit1 на экран:")
print(crit1)
print("Непосредственный доступ к атрибуту crit1.name")
print(crit1.name)

# Классово верная зверюшка
# Демонстрирует атрибуты класса и статические методы
class Critter(object):
    """Виртуальный питомец"""
    total = 0
    @staticmethod
    def status():
        print("\nBcero зверюшек сейчас" ,Critter.total)
    def __init__ (self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        Critter.total += 1
# основная часть
print("Haxoжy значение атрибута класса Critter.total :", end=" ")
print(Critter.total)
print("\nCoздaю зверюшек.")
critl = Critter("зверюшка 1")
crit2 = Critter("зверюшка  2")
critЗ= Critter("зверюшка  3")
Critter .status()
print("\nOбpaщaюcь к атрибуту класса через объект:")
print(critl.total)


# Закрытая зверюшка
# Демонстрирует закрытые переменные и методы class Critter(object):

class Critter1(object):
    """Виртуальный питомец"""
    def __init__(self, name, mood):
        print("Появилась на свет новая зверюшка")
        self.name = name # открытый атрибут
        self.__mood = mood # закрытый атрибут
    def talk(self):
        print("\nМеня зовут", self.name)
        print("Сейчас я чувствую себя", self.__mood,"\n")
    def __private_method(self):
        print("Это закрытый метод.")
    def public_method(self):
        print("Это открытый метод")
        self.__private_method()
    
#основная часть
creature = Critter1("Бобик","прекрасно")
creature.talk()
creature.public_method()
creature._Critter1__private_method()
print(creature.name)


# Зверюшка со свойствами
# Демонстрирует свойства
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.__name = name
    @property # свойство - обьект с методами которые позволяют косвенно
    # обращатся к атрибутам и зачастую в чем-либо ограничивают такой косвенный доступ
    def name(self):
        return self.__name
    @name.setter # декоратор обращаясь к которому я говорю что метод далее
    # устанавливает новое значение свойства name метод сеттер имеет тоже имя что и свойство
    def name(self, new_name):
        if new_name == "":
            print("Имя зверюшки не может быть пустой строкой")
        else:
            self.__name = new_name
            print("Имя успешно изменено")
    def talk(self):
        print("\nПривет меня зовут", self.name)

creit = Critter("бобик")
creit.talk()
print("Мою зверюшку зовут", creit.name)
print("Попробую изменить имя на мурзик")
creit.name = "Мурзик"
print("Мою зверюшку зовут", creit.name)
print("Попробую изменить имя на пустую строку")
creit.name = ""
print("Мою зверюшку зовут", creit.name)
