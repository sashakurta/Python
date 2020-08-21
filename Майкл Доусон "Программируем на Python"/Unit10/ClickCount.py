# Cчетчик щелчков по кнопке
from tkinter import *
class Application(Frame):
    """приложение которое подсчитывает количество нажатий кнопки"""
    def __init__(self, master):
        """Инициализирует рамку"""
        super(Application, self).__init__(master)
        self.grid()
        self.buttn_clics = 0 # количество кликов
        self.create_widget()
    def create_widget(self):
        """Создает кнопку на которой отображается количество кликов"""
        self.buttn = Button(self)
        self.buttn["text"] = "Количество щелчков 0"
        self.buttn["command"] = self.update_count
        self.buttn.grid()
    def update_count(self):
        """Увеличивает количество нажатий на единицу и отображает его"""
        self.buttn_clics += 1
        self.buttn["text"] = "Количество щелчков " + str(self.buttn_clics)
        


root = Tk()
root.title("Количество щелчков")
root.geometry("500x200")
app = Application(root)
root.mainloop()
