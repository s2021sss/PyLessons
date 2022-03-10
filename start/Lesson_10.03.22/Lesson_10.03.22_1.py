grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня": 10}
students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
for item in students:
    if item in grades:
        print (f"{item} оценка: {grades[item]}")
    else:
        print (f"{item} не писал кр")
print ("Отличные оценки получили: ")
good=[]
bad=[]
for item in grades:
    if grades[item]>=8:
        print (f"{item} оценка: {grades[item]}")
for item in grades:
    if grades[item]>=5:
        good.append(item)
    else:
        bad.append(item)
print(f"Плохие оценки получили {bad}") 
print(f"Хорошие оценки получили {good}") 
