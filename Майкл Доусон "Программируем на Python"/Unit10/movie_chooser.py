# Киноман
# Демонстрирует применение флажков
from tkinter import *
class Application(Frame):
    """приложение позволяющее выбрать любимые жанры кино"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5,column = 0, columnspan = 3)
        self.likes_romance = BooleanVar()
        self.likes_drama = BooleanVar()
        self.likes_comedy = BooleanVar()
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """создает элементы с помощью которых пользователь будет выбирать"""
        # метка описание
        Label(self,
              text = "Укажите ваши любимые жары кино").grid(row = 0, column = 0, sticky = W)
        # метка инструкция
        Label(self, text = "Выберете то что вам по вкусу").grid(row = 1, column = 0, sticky = W)
        # флажок комедия
        
        chbttn1 =Checkbutton(self,text = "Комедия",variable = self.likes_comedy,command = self.update_text,onvalue=1, offvalue=0)
        chbttn1.grid(row = 2, column = 0, sticky = W)
        # флажок драма
        
        chbttn2 = Checkbutton(self,
                    text = "Драма",
                    variable = self.likes_drama,
                    command = self.update_text,
                    onvalue=1,
                    offvalue=0)
        chbttn2.grid(row = 3, column = 0, sticky = W)
        # флажок фильмы о любви
        
        chbttn3 = Checkbutton(self,
                    text = "Фильмы о любви",
                    variable = self.likes_romance,
                    command = self.update_text,)
        chbttn3.grid(row = 4, column = 0 , sticky = W)
    def update_text(self):
        """Обновляет текстовый элемент по мере того ка пользователь выбирает свои любимые киножанры"""
        likes = ""
        if self.likes_comedy.get():
            likes+= "Вам нравятся комедии\n"
        if self.likes_drama.get():
            likes += "Вас привлекает жанр драмы\n"
        if self.likes_romance.get():
            likes += "Вам по вкусу кино о любви\n"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)
# основная часть
root = Tk()
root.title("Киноман")
app = Application(root)
root.mainloop()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
