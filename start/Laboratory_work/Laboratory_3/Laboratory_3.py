import json

flag=True
fileName=input("Введите имя файла: ")
if (fileName.split(".")[-1]=="json"):
    fileNameFull=fileName
else:
    fileNameFull=fileName+".json"
try:
    file = open(fileNameFull, "r+", encoding='utf-8')
    data = json.load(file)
except:
    flag=False
    print("Файл не найден. Проверьте правильность имени файла!")
while (flag):
    print("""Простой todo:
            1. Добавить задачу.
            2. Вывести список задач.
            3. Выход.""")
    comanda=input("Введите команду: ")
    if (comanda=="1"):
        task=input("Сформулируйте задачу: ")
        category=input("Добавьте категорию к задаче: ")
        time=input("Добавьте время к задаче: ")
        data.append({"Задача": task, "Категория":category, "Время": time})
        file.seek(0)
        json.dump(data, file)
    elif (comanda=="2"):
        for i in data:
            for key, value in i.items():
                print (f"{key}: {value}, ", end="")
            print("")
    elif(comanda=="3"):
        print("Задачи сохранены в файл!")
        file.close()
        flag=False
    else:
        print("Данной команды нет в спиcке!")
