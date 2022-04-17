def numbering(firstname, lastname):
    try:
        file = open(firstname, 'r', encoding="utf8")
        data = list(filter(None, file.read().split("\n")))
        file.close
    except:
        print ("Фаил не найден")
    for i in range(len(data)):
        data[i]= str(i+1) + " " + data [i]
    print (data)
    file = open(lastname, 'w', encoding="utf8")
    for i in data:
        file.write(i + "\n")
    file.close()
numbering("text.txt","update text.txt")
