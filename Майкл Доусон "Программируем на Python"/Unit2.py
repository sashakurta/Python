# Game Over - версия 2
# Показывает разные приемы работы со строками
#1
print( "Программа'GameOver' 2. О")


print( "Тоже", "самое","сообщение")
print("Только",
      "чуть-чуть",
      "побольше")
print("Boт",end=" " )
print( "оно...")
print("""
        _____        ___        ___  ___    _____
       /  ___|      /   |      /   |/   |  | ____|
       | |         / /| |     / /|   /| |  | |___
       | |  _     / ___ |    / / |__/ | |  |  ___|
       | |_| |   / /  | |   / /       | |  | |___
       \_____/  / /   | |  / /        | |  |____ |
        _____    _     _    _____    ______
       /  _  \  | |   / /  | ____|  |   _  \.
       | | | |  | |  / /   | |___   |  |_| |
       | | | |  | | / /    |  ___|  |   _  /
       | |_| |  | |/ /     | |___   |  | \ \.
       \_____/  |___/      |_____|  |__|  \_\.
       """)
#2
# Воображаемые благодарности
# Образец применения еsсаре-последовательностей
print("\t\t\tВоображаемые благодарности")
print("\t\t\t\\\\\\\\\\\\\\")
print("\t\t\tразработчика игры")
print("\t\t\tКурты Олександра")
print("\t\t\t\\\\\\\\\\\\\\\n")
print("Отдельное спасибо хотелось бы сказать:\n")
print("бла бла бла строка")
print("\a \a \a")

#3
# Забавные строки
# Демонстрирует сцепление и повторение строк
print("Две строки можно "+ "сцепить с помошью оператора +.")
print("Повторить текст можно оператором * \n", "Пироженые"*10, )

#4
# Привет
# Демонстрирует использование переменых
name = "Вася"
print(name)
print("Привет", name)

#5
# Персональный
# Демонстрирует получение пользовательского ввода
name = input("Привет. Как тебя зовут?")
print(name)
print("Привет", name)

#6
# Манипуляции с цитатой
# Демонстрирует строковые методы

quote = "Думаю на мировом ринке можно будет продать \
штук пять компьютеров"
print("\nИсходная цитата")
print(quote)
print("\nОна же в верхнем регистре")
print(quote.upper())
print("\nВ нижнем регистре")
print(quote.lower())
print("\nКак заголовок")
print(quote.title())
print("\nC маленькой заменой")
print(quote.replace("штук пять", "несколько миллионов"))
print("\nА вот исходная цитата")
print(quote)


#7
# Любимые блюда
firstdish = input("Какое ваше первое любимое блюдо")
seconddish = input("Какое ваше второе любимое блюдо")
res = firstdish+seconddish
print(res)

#8
# Щедрый посетитель

bill = int(input("Введите сумму счета\n"))
bill1 = bill*0.2 + bill
bill2 = bill*0.15 + bill
print("Сумма с 20 процентами чаевых", bill1, "c 15 процентами чаевых", bill2)

#9
#Автодиллер
price = int(input("Введите стоимость машины"))
fee = price*0.12
regfee = price*0.03
agfee = 150
delivery = 200
print("Окончательная цена со всеми налогами и добавочной стоимостью",price + fee +regfee + agfee + delivery)



input("\n\nHaжмитe Enter. чтобы выйти . ")
