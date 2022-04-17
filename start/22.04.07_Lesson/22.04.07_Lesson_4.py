file = open("sber.txt", "r", encoding="utf8")
slovar = {}
for i in file:
    stroka = i.split(",")
    if stroka[0]=='Количество заявок на потребительские кредиты':
        if stroka[2][:4]=="2017":
            if stroka[1] in slovar:
                slovar[stroka[1]] += int(stroka[3])
            else:
                slovar[stroka[1]] = int(stroka[3])
del slovar['Россия']
key_max=max(slovar, key=slovar.get)
print(str(key_max) + ": "+ str(slovar[key_max])+ " заявок")
