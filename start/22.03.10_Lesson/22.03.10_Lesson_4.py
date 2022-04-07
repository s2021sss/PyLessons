marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}
k=0
mark=int(input ("Введите оценку: "))
for item in marks:
    for i in marks[item]:
        if i>=mark:
            k=k+1
print (f"Количество оценок выше или равных {mark} равно {k} ")
