# Долгожитель
# Демонстрирует текстовое поле. текстовую область и менеджер размещения Grid
from tkinter import *
class Application(Frame):
    """приложение владеющее секретом долголетия"""
    def __init__(self, master):
        """ инициализирует рамку """
        super().__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """ создет кнопку текстовое поле и текстовую область"""
        self.inst_lbl = Label(self, text = "Чтобы узнать секрет долголетия введитем пароль")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        # метка около ввода пароля
        self.pw_lbl = Label(self, text = "Пароль: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        # текстовое поле для ввода пароля
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        # кнопка отправки значения
        self.submit_bttn = Button(self, text = "Узнать секрет", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)
        # создание текстовой области в которую будет выведен ответ
        self.secret_text = Text(self, width = 35, height = 5, wrap = WORD )
        self.secret_text.grid(row = 3, column = 0, columnspan = 2, sticky = W)
    def reveal(self):
        """В зависимости от введенного пароля отвечает разними сообщениями"""
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "Чтоб дожить до 100 лет надо сначала дожить до 99." \
                      "а потом вести себя ОЧЕНЬ осторожно"
        else:
            message = "Вы ввели неправильный пароль. так что я не могу" \
                      "поделится тайной с вами"
        self.secret_text.delete(0.0, END)
        self.secret_text.insert(0.0, message)



# основная часть
root = Tk()
root.title("Долгожитель")
root.geometry("350x200")
app = Application(root)
root.mainloop()
