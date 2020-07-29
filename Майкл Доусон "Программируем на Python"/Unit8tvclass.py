# программа имитирует телевизор как обьект
class Television(object):
    def __init__(self):
        self.__channel = 1
        self.__volume = 25
    def __str__(self):
        i = "Сейчас включен "+ str(self.__channel) + " канал" \
         "\nНа громкости " + str(self.__volume)
        return i
    @property
    def channel(self):
        return self.channel
    @property
    def volume(self):
        return self.volume
    def change_channel(self, number):
        while (120 < number) or (number <= 0):
            print("Введите число в диапазоне от 1 до 120")
            number = input("Введите число в диапазоне 1-120")
        self.__channel = number
        print("Вы на ", self.__channel, "канале")
    def change_volume(self,number):
        while (0 > number) or (number > 100):
            print("Введите число в диапазоне от 1 до 120")
            number = input("Введите число в диапазоне 0-100")
        self.__volume = number
        print("Теперь громкость", self.__volume)


def main():
    tv = Television()
    checker = None
    while checker != 0:
        print("""
        Телевизор
        0 - Выключить телевизор
        1 - Переключить канал
        2 - Изменить громкость
        3 - Текущий канал и громкость""")
        checker = input("Выберете действие ")
        if checker == "0":
            print("Выключаюсь")
            checker = 0
        elif checker == "1":
            check = True
            while check:
                try:
                    channel = int(input("На какой канал вы хотите переключится? (1-120)"))
                    tv.change_channel(channel)
                    check = False
                except:
                    print("Введите число")
        elif checker == "2":
            check = True
            while check:
                try:
                    volume = int(input("На какую громкость вы хотите переключится? (1-100) "))
                    tv.change_volume(volume)
                    check = False
                except:
                    print("Введите число")
        elif checker == "3":
            print(tv)
        else:
            print("Такого значения нет в меню ")
            
    
main()
