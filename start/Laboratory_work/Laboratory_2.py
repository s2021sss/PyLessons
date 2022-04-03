def getdata():
    file = open("students.txt", 'r', encoding="utf8")
    data = list(filter(None, file.read().split("\n")))
    file.close()
    return data

def writedata(data):
    data.sort(key=str.lower)
    file = open("students.txt", 'w', encoding="utf8")
    for stud in data:
        file.write(stud + "\n")
    file.close()
    
def printdata():
    data=getdata()
    for i in data: 
        print (i)

def addstudent(surname, name):
    student=" ".join([surname, name])
    data=getdata()
    if not(student in data):
        data.append(student)
        writedata(data)
        return "Студент " + student + " добавлен"
    else:
        return "Студент " + student + " уже есть в списке"


def getstudent(surname, name=None):
    data=getdata()
    if (name==None):
        allsurnames = list(map(lambda x: x.split()[0], data))
        if surname in allsurnames:
           firstindex = allsurnames.index(surname)
           return "Студенты с фамилией "+ surname + ": " + ", ".join([data[i] for i in range(firstindex, firstindex+allsurnames.count(surname))])
        else:
            return "Студента с фамилией " + surname + " нет в списке"
    else:
        student=" ".join([surname, name])
        if (student in data):
            return "Студент " + student + " есть в списке"
        else:
            return "Студента " + student + " нет в списке"

def change (old_surname, old_name, new_surname=None, new_name=None):
    data=getdata()
    student=" ".join([old_surname, old_name])
    if (student in data):
        data.remove(student)
        new_student=" ".join([new_surname if (new_surname!=None) else old_surname, new_name if (new_name!=None) else old_name])
        data.append(new_student)
        writedata(data)
        return "Студент " + student + " изменен на " + new_student
    else:
        return "Студента " + student + " нет в списке"

def removestudent (surname, name=None):
    data=getdata()
    if (name!=None):
        student=" ".join([surname, name])
        if (student in data):
            data.remove(student)
            writedata(data)
            print( "Студент " + student + " удален")
        else:
            print("Студента " + student + " нет в списке")
    else:
        allsurnames = list(map(lambda x: x.split()[0], data))
        if (allsurnames.count(surname)==0):
            print( "Студента с фамилией " + surname + " нет в списке")
        elif (allsurnames.count(surname)==1):
            indexstud=allsurnames.index(surname)
            print ("Студент "+ data[indexstud] + " удален" )
            data.pop(indexstud)
            writedata(data)
        else:
            print(getstudent(surname))
            name2 = input ("Введите имя ученика, которого хотите удалить: ").replace(" ", "")
            removestudent (surname, name=name2)
            

while (True):
    comanda=input("Введите команду: ").replace(" ", "")
    if (comanda=="add"):
        surname = input ("Введите фамилию студента: ").replace(" ", "")
        name = input ("Введите имя студента: ").replace(" ", "")
        print (addstudent(surname, name))
    elif (comanda=="get"):
        surname = input ("Введите фамилию студента: ").replace(" ", "")
        name = input ("Введите имя студента или '', если надо искать студента только по фамилии: ").replace(" ", "")
        if (name=="''"):
            print(getstudent(surname))
        else:
            print (getstudent(surname, name))
    elif (comanda=="change"):
        surname = input ("Введите фамилию студента, данные которого хотите поменять: ").replace(" ", "")
        name = input ("Введите имя студента, данные которого хотите поменять: ").replace(" ", "")
        new_surname = input ("Введите новую фамилию студента или '', если не хотите менять фамилию: ").replace(" ", "")
        new_name = input ("Введите новое имя студента или '', если не хотите менять имя: ").replace(" ", "")
        if (new_name=="''" and new_surname=="''"):
            print ("Вы не ввели, как поменять фамилию и имя студента")
        elif (new_name=="''"):
            print(change(surname, name, new_surname=new_surname, new_name=None))
        else:
            print(change(surname, name, new_surname=None, new_name=new_name))
    elif (comanda=="remove"):
        surname = input ("Введите фамилию студента: ").replace(" ", "")
        name = input ("Введите имя студента или '', если надо удалять студента только по фамилии: ").replace(" ", "")
        if (name=="''"):
            removestudent (surname)
        else:
            removestudent (surname, name=name)
    elif (comanda=="data"):
        printdata()
    elif (comanda=="q"):
        break
    else:
        print ("Введите правильную команду \n"
               "add - добавить студента по имени и фамилии\n"
               "get - найти студента по фамилии и имени или только по фамилии \n"
               "change - измменить у заданного по фамилии и имени студента имя и фамилию или только фамилию \n"
               "remove - удалить студента по фамилии и имени или толкьо по фамилии \n"
               "data - вывести всех студентов \n"
               "q - конец программы")
