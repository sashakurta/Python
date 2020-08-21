# Бесполезные кнопки 2
# демонстрирует создание класса
# в оконном приложении
from tkinter import *

class Application(Frame):
    """Приложение с 3мя кнопками"""
    def __init__(self, master):
        """Инициадизирует рамку"""
        super(Application, self).__init__(master)
        self.grid()
        self.crete_widgets()
    def crete_widgets(self):
        """Создает три бесполезные кнопки"""
        # первая кнопка
        self.buttn1 = Button(self, text="Я ничего не делаю")
        self.buttn1.grid()
        # вторая кнопка
        self.buttn2 = Button(self)
        self.buttn2.grid()
        self.buttn2.configure(text = "И я тоже")
        # третья кнопка
        self.buttn3 = Button(self)
        self.buttn3.grid()
        self.buttn3["text"] = "И я!"

root = Tk()
root.title("Бесполезные кнопки - 2")
root.geometry("500x200")
app = Application(root)
root.mainloop()


