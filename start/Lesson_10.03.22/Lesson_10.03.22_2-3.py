marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}
kurs=int(input ("Введите курс: "))
s=0
k=0
for item in marks:
    k=k+1;
    s=s+marks[item][kurs-1]
print (f"Средняя оценка за {kurs} курс равна {round(s/k)}")
categories = {'отлично' : [8, 9, 10],
             'хорошо' : [6, 7],
             'удовлетворительно' : [4, 5],
             'неуд' : [0, 1, 2, 3]}
for item in categories:
    for num in categories[item]:
        if round(s/k)==num:
            print (f"Это оценка {item}")
