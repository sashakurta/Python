# Киноман-2
# Демонстрирует переключатель
from tkinter import *
class Application(Frame):
    """приложение позволяющее выбрать одни любимый жанр кино"""
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """Создает элементы с помошью которых пользователь будет выбирать"""
        # метка-описание
        Label(self,
              text = "Укажите ваш любимый жанр кино").grid(row = 0, column = 0, sticky = W)
        # метка-инструкция
        Label(self,
              text = "Выберете ровно один:").grid(row = 1, column = 0, sticky = W)
        self.favourite = StringVar()
        self.favourite.set(None)
        # положение Комедия переключателя
        rbttn1 = Radiobutton(self,
                    text = "Комедия",
                    variable = self.favourite,
                    value = "комедия",
                    command = self.update)
        rbttn1.grid(row = 2, column = 0, sticky = W )
        rbttn2 = Radiobutton(self,
                    text = "Драма",
                    variable = self.favourite,
                    value = "драма",
                    command = self.update)
        rbttn2.grid(row = 3, column = 0, sticky = W )
        rbttn3 = Radiobutton(self,
                             text = "Кино о любви",
                    variable = self.favourite,
                    value = "кино о любви",
                    command = self.update)
        rbttn3.grid(row = 4, column = 0, sticky = W )
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)
    def update(self):
        """обновляя текстовую область вписывает в нее любимый жанр"""
        message = "Ваш любимый жанр - "
        message += self.favourite.get()
        self.results_txt.delete(0.0, END)
        self .results_txt.insert(0.0, message)
# основная часть
root = Tk()
root.title("Киноман-2")
app = Application(root)
root.mainloop()
