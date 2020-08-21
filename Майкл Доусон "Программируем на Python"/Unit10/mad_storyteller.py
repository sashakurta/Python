# Сумасшедший сказочник
# Создает рассказ на основе пользовательского ввода
from tkinter import *
class Application(Frame):
    """приложение создающее рассказ на основе пользовательского ввода"""
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """создает элементы управления с помощью которых пользователь
        будет вводить исходные данные и получать рассказ"""
        # метка с инструкцией
        Label(self,
              text = "Введите данные для создание нового рассказа").grid(row = 0, column = 0, sticky = W)
        # метка и поле ввода для имени человека
        Label(self,
              text = "Имя человека:").grid(row = 1, column = 0, sticky = W)
        self.pearson_ent = Entry(self)
        self.pearson_ent.grid(row = 1, column = 1, sticky = W)
        # метка и поле ввода для существительного
        Label(self,
              text = "Существительное во мн.ч.:").grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = W)
        # метка и поле ввода для глагола
        Label(self,
              text = "Глагол в инфинитиве:").grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)
        # метка при группе флажков с прилагательными
        Label(self,
              text = "Прилагательные").grid(row = 4, column = 0, sticky = W)
        # флажок со словом нетерпеливый
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = "нетерпеливый",
                    variable = self.is_itchy,).grid(row = 4, column = 1, sticky = W)
        # флажок со словом радостный
        self.is_joyus = BooleanVar()
        Checkbutton(self,
                    text = "радостный",
                    variable = self.is_joyus,).grid(row = 4, column = 2, sticky = W)
        # флажок со словом пронизывающий
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text = "пронизывающий",
                    variable = self.is_electric,).grid(row = 4, column = 3, sticky = W)
        # метка при переключателе с названиями частей тела
        Label(self,
              text = "Body Part").grid(row = 5, column = 0, sticky = W)
        # переменная содержащая название одной из частей тела
        self.body_part = StringVar()
        self.body_part.set(None)
        # переключатель с названиями частей тела
        body_parts = ["пупок","большой палец ноги","продолговатый мозг"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part,
                        ).grid(row = 5, column = column, sticky = W)
            column+=1
        # кнопка отсылки данных
        Button(self,
               text = "Получить рассказ",
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)
        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid( row = 7, column = 0, columnspan = 4)
    def tell_story(self):
        """Заполняет текстовую область очередной историей на основе
        пользовательского ввода"""
        person = self.noun_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives+="нетерпеливае, "
        if self.is_joyus.get():
            adjectives += "радостное, "
        if self.is_electric .get():
            adjectives += "пронизывающее, "
        body_part = self.body_part.get()
        story = "Знаменитый путешественник "
        story += person
        story += " уже совсем отчаялся довершить дело всей своей жизни - поиск затерянного города. в котором. по легенде. обитали "
        story += noun.title()
        story += ". Но однажды "
        story += noun
        story+="и "
        story += person + " столкнулись лицом к лицу. "
        story += "Мощное. "
        story += adjectives
        story += "ни с чем не сравнимое чувство охватило душу путешественника."
        story +="После стольких лет поисков цель была наконец достигнута. "
        story += person
        story += " ощутил. как на его " + body_part + " скатилась слезинка. "
        story += "И тут внезапно "
        story += noun
        story += " перешли в атаку. и "
        story += person + " был ими мгновенно сожран."
        story += "Мораль? Если задумали "
        story += verb
        story += ". надо делать это с осторожностью."
        # вывод рассказа на экран
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

root = Tk()
root.title("Сумашедший сказочник")
app = Application(root)
root.mainloop()
