# Викторина
# Игра на выбор правильного варианта ответа.
# вопросы которой читаются из текстового файла
import sys
import pickle, shelve
def open_file(file_name, mode):
    """Открывает файл"""
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except  IOError as e:
        print("Невозможно открыть файл", file_name, ". Работа программы будет завершена.\n")
        sys.exit()
    else:
        return the_file
def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла"""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line
def next_block(the_file):
    """Возвращет очередной блок данных из игрового файла"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    nominal = next_line(the_file)
    explanation = next_line(the_file)
    return category, question, answers, correct, nominal, explanation
def welcome(title):
    """Приветствует игрока и сообщает тему игры."""
    print("\t\tДобро пожаловать в игру \"Викторина\"")
    print("\t\t", title, "\n")
    name = input("Введите свое имя: ")
    return name
def reconservate(score, name):
    """Розконсерирует файл и возвращает словарь с рекордами"""
    records_file = open("records.txt","rb+")
    try:
        records_dic = pickle.load(records_file)
    except:
        records_dic = {}
    if records_dic:
        records_dic[name] = score
        if len(records_dic.keys()) > 5:
            inverse = [(value, key) for key, value in records_dic.items()]
            keymin = min(inverse)[1]
            print(keymin)
            del records_dic[keymin]
    else:
        records_dic[name] = score
    records_file.close()
    return records_dic
    

def conservate(dict):
    """Консервирует словарь в файл"""
    records_file = open("records.txt","wb+")
    pickle.dump(dict, records_file)
    records_file.close()
    
def dicout(dict):
    """Ввиводит словарь в консоль"""
    for i in dict.keys():
        print("\t", i, "\t", dict[i])
    
    

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    name = welcome(title)
    score = 0
    category, question, answers, correct, nominal, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t",i+1,"-",answers[i])
        answer = input("Ваш ответ: ")

        if answer == correct:
            print("Да!",end=' ')
            score += int(nominal)
        else:
            print("\nНет...",end=' ')
        print(explanation)
        print("Счет: ", score, "\n\n")
        category, question, answers, correct, nominal, explanation = next_block(trivia_file)
    trivia_file.close()
    print("Это был последний вопрос")
    print("На вашем счету: ", score)
    records = reconservate(score, name)
    print("\tИмя\tСчет")
    dicout(records)
    conservate(records)
  
  
        
main()
