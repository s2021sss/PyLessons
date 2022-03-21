documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def spisokPolok():
    lst=[]
    lst2=[]
    for key in directories:
        lst.append(key)
    lst2=", ".join(lst)
    return (lst2)

def p():
    num=input("Введите номер: ")
    for doc in documents:
        if doc["number"] == num:
            print (f"Владелец документа: {doc['name']}")
            break
    else:
        print ("Документ не найден в базе")

def s():
    num=input("Введите номер: ")
    flag=False
    for key in directories:
        for i in directories[key]:
            if i == num:
                print (f"Документ хранится на полке: {key}")
                flag=True
                break
        if flag==True:
            break
    else:
        print ("Документ не найден в базе")
        
def info():
    for inf in documents:
        for key in directories:
            for i in directories[key]:
                if i == inf['number']:
                    print (f"№:{inf['number']}, тип: {inf['type']}, владелец: {inf['name']}, полка хранения: {key}")
def ads():
    num=input("Введите номер полки: ")
    flag=False
    for key in directories:
        if num==key:
            flag=True
    if flag==False:
        directories[num]=[]
        print ("Полка добавлена. Текущий перечень полок:", spisokPolok()) 
    else:
        print ("Такая полка уже существует. Текущий перечень полок:", spisokPolok())
   

def ds():
    num=input("Введите номер полки: ")
    if num in directories:
        if directories[num]==[]:
            directories.pop(num)
            print ("Полка удалена. Текущий перечень полок: ", spisokPolok() )
        else:
            print ("На полке есть документы, удалите их перед удалением полки. Текущий перечень полок:", spisokPolok())
    else:
        print ("Такой полки не существует. Текущий перечень полок:", spisokPolok()) 

def ad():
    new_dic={}
    new_dic['number']=input("Введите номер документа: ")
    new_dic['type']=input("Введите тип документа: ")
    new_dic['name']=input("Введите владельца документа: ")
    polka=input("Введите полку для хранения: ")
    if polka in directories:
        documents.append(new_dic)
        directories[polka].append(new_dic['number'])
        print ("Документ добавлен. Текущий список документов:")
        info()
    else:
        print("Такой полки не существует. Добавьте полку командой ads")
        info()

def d():
    num=input("Введите номер документа: ")
    flag=False
    flag2=False
    for inf in documents:
        if inf['number'] == num:
            flag=True
            documents.remove(inf)
            for key in directories:
                for i in directories[key]:
                    if i == num:
                        directories[key].remove(i)
                        flag2=True
                        break
                if flag2==True:
                    break 
            break
    if flag==True:
        print ("Документ удален.", "Текущий список документов:", sep="\n")
        info()
    else:
        print ("Документ не найден в базе.", "Текущий список документов:", sep="\n")
        info()
     
def m():
    num=input("Введите номер документа: ")
    polka=input("Введите номер полки: ")
    flag=False
    if polka in directories:
        for inf in documents:
            if inf['number']==num:
                flag=True
                break
        if flag==True:
            for key in directories:
                for i in directories[key]:
                    if i == num:
                        directories[key].remove(num)
                        directories[polka].append(num)
                        break
            print ("Документ перемещен.", "Текущий список документов:", sep="\n")
            info()
        else:
            print ("Документ не найден в базе.", "Текущий список документов:", sep="\n")
            info()
    else:
        print("Такой полки не существует. Текущий перечень полок:", spisokPolok() )
    
while (True):
    comanda = input("Введите команду: ")
    if (comanda=="q"):
        break
    if comanda=="p":
        p()
    elif comanda=="s":
        s()
    elif comanda=="/":
        info()
    elif comanda=="ads":
        ads()
    elif comanda=="ds":
        ds()
    elif comanda=="ad":
        ad()
    elif comanda=="d":
        d()
    elif comanda=="m":
        m()
    else:
        print("Необходимо ввести команду: p, s, /, ads, ds, ad, d, m, d, m, либо завершить программу команду q")
