# Кости
# Демонстрирует
# создаем случайные числа из диапазона 1 - 6
import random
die1 = random.randint(1,6)
die2 = random.randrange(6)+1
print("При вашем броске выпало", die1, "и", die2,
      "в сумме", die1+die2)

#Пароль
#Демонстрирует использывание if
password = input("Введите пароль для доступа")
if password == "secret":
    print("Доступ открыт")
else:
    print("Доступ забыл")

#Настроение
mood = random.randrange(2)
if mood == 0:
    print("Вы сегодня веселый")
elif mood == 1:
    print("Вы чувствуете себя так себе")
elif mood == 2:
    print("Вы чувствуете себя скверно")
else:
    print("Такого настроения нет")
    
# Симулятор трехлетнего ребенка
#Демонстрирует работу цикла while
response = ""
while response != "Потому что.":
    response = input("Почему?")
print("А ладно")

# Отгадай число
# Компьютер выбирает случайное число в диапазоне от 1 до 100
# Игрок пытается отгадать это число и компьютер говорит
# предположение больше/меньше. чем загаданное число.
# или попало в точку
import random
print( "\tДобро пожаловать в игру 'Отгадай число!'")
print("\nЯ загадал натуральное число из диапазона от 1 до 100.")
print("Постарайтесь отгадать его за минимальное число попыток.\n")
#начальные значения
num = random.randint(1,100)
guess = int(input("Ваше предположение"))
tries = 1
#цикл угадывания
while guess != num :
    if guess > num:
        print("Меньше...")
    else:
        print("Больше...")
    tries+=1
    guess = int(input("Ваше предположение"))
# вывод результата
print("Baм удалось отгадать число! Зто в самом деле", num)
print("Bы затратили на отгадывание всего лишь ", tries, " попыток!\n")

# пирожок с сюрпризом
# при запуске отображает один из пяти различных сюрпризов

num = random.randint(1,5)
if num == 1:
    print("Пирожок с вишней")
elif num == 2:
    print("Пирожок с бананом")
elif num == 3:
    print("Пирожок с мясом")
elif num == 4:
    print("Пирожок с повидлом")
elif num == 5:
    print("Пирожок с капустой")
else:
    print("Невозможный вариант")
    
# Программа которая подбрасывает монету 100 раз
# и сообщает сколько раз выпал орел а сколько решка
# начальные значения
numeagle = 0
numrechka = 0
count = 0
# цикл подкидывания 100 раз
while True:
    num = random.randrange(2)
    if not num:
        numeagle+=1
    elif num :
        numrechka+=1
    count+=1
    if count == 100:
        break
# объявление результатов
print("После 100 подбрасываний монеты \nРешка была выкинута",
      numrechka,"раз\n","Орел был выкинут ",numeagle,"раз")

# игра в которой компьютер угадывает число которое загадал пользователь
count = 1
metric = 25
num = 50
while True:
    print("Вы загадали число?",num)
    answer = input()
    if answer == "да":
        print("Компьютер угадал число которое вы загадали это число - ",
              num,"за количество попиток", count)
        break
    elif answer == "меньше":
        num-=metric
        metric//=2
        count+=1
    elif answer == "больше":
        num+=metric
        metric//=2
        count+=1
    else:
        print("Введите да, меньше , больше")
print("Конец работы програмы")

# доработка c Главы 6

# игра в которой компьютер угадывает число которое загадал пользователь
def ask_number(question,low,high):
    """Просит ввести число из диапазона"""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response
count = 1
metric = 25
num = 50
while True:
    answer = ask_number("Вы загадали число",1,100)
    print(num)
    if answer == "да":
        print("Компьютер угадал число которое вы загадали это число - ",
              num,"за количество попиток", count)
        break
    elif answer == "меньше":
        num-=metric
        metric//=2
        count+=1
    elif answer == "больше":
        num+=metric
        metric//=2
        count+=1
    else:
        print("Введите да, меньше , больше")
print("Конец работы програмы")

















