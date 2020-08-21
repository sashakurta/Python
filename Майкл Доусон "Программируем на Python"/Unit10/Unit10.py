# Простейший GUI
# Демонстрирует создание окна
from tkinter import *
# создание базового окна
root = Tk()
# изменение окна
root.title("Простейший GUI")
root.geometry("300x500")

# это я метка
# внутри окна создается рамка для размещения других
# элементов
app = Frame(root)
app.grid() # метод связан с менеджером размещения с
# помощью которого  можно управлять расположением элементов в окне
# создание метки внутри рамки
lbl = Label(app, text = "Вот она я")
lbl.grid()

# бесполезные кнопки
bttn1 = Button(app, text="Я ничего не делаю")
bttn1.grid()
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Я тоже")
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "и я"
# старт событийного цикла
root.mainloop()
