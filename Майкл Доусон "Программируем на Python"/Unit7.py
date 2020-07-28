# Прочитаем
# Демонстрирует чтение из текстового файла
print("Открываю и закрываю файл.")
text_file = open("file1.txt", "r", encoding='utf-8')
text_file.close()
print("\nЧитаю файл посимвольно")

text_file = open("file1.txt","r")
print(text_file.read(8))
print(text_file.read(15))
text_file.close()

print("\nЧитаю файл целиком")
text_file = open("file1.txt", "r", encoding='utf-8')
whole_text = text_file.read()
print(whole_text)
text_file.close()

print("\nЧитаю строку посимвольно")
text_file = open("file1.txt", "r", encoding='utf-8')
print(text_file.readline(2))
print(text_file.readline(2))
text_file.close

print("\nЧитаю строку целиком")
text_file = open("file1.txt", "r", encoding='utf-8')
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nЧитаю весь файл в список")
text_file = open("file1.txt", "r", encoding='utf-8')
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print("\nПеребираю файл построчно")
text_file = open("file1.txt", "r", encoding='utf-8')
for line in text_file:
    print(line)
text_file.close()


#Запишем
# Демонстрирует запись в текстовый файл
text_file = open("writefile.txt", "w", encoding='utf-8')
text_file.write("Строка 1\n")
text_file.write("Строка 2\n")
text_file.write("Этой строке достался номер 3\n")
text_file.close()

print("Читаю весь файл и вывожу его содержимое")
text_file = open("writefile.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()

print("Создаю текстовый файл методом writelines()")
text_file = open("writefile.txt", "w", encoding='utf-8')
lines = [
    "Строка 1\n",
    "Это строка 2\n",
    "Этой строке достался номер 3\n"]
text_file.writelines(lines)

print("Читаю весь файл и вывожу его содержимое")
text_file = open("writefile.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()


# Законсервируем
# Демонстрирует консервацию данных и доступ к ним через интерфейс полки
import pickle, shelve
print("Консервация списков")
variety = ["огурцы","помидоры","капуста"]
shape = ["целые","кубиками","соломкой"]
brand = ["Главпродукт","Чумак","Бондюель"]
f = open("pickles1.dat","wb")# wb для записи байтов
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()
print("\nРасконсервация списков")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

# Помещение списков на полку
print("\nПомещение списков на полку")
s = shelve.open("pickles2.dat")
s["variety"] = ["огурцы", "помидоры", "капуста"]
s["shape"] = ["целые", "кубиками", "соломкой"]
s["brand"] = ["Главпродукт", "Чумак", "Бондюэль"]

s.sync()

print("\nИзвлечение списков из файла полки")
print(s["brand"])
print(s["shape"])
print(s["variety"])

f.close()


# Обработаем
# Демонстрирует обработку исключительных ситуаций
# try/except
    
try:
    num = float(input("Введите число:"))
except ValueError:
    print("Похоже это не число")

for value in (None, "Привет","345"):
    try:
        print("Пытаюсь преобразовать в число",value,"",end=' ')
        print(float(value))
    except TypeError as e:
        print("Я умею преобразовывать только строки и числа")
        print(e)
    except ValueError as e:
        print("Я умею преобразовывать только строки составленые из цифр")
        print(e)
    else:
        print("Вы ввели число"
              )
        





