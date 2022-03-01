import statistics
lst=[2, 6, 8, 66, 12, 94, 57, 45, 3, 89, 34]
min_i=lst.index(min(lst))
max_i=lst.index(max(lst))
if (min_i+1<max_i):
    print (f"Среднее арифметическое: {statistics.mean(lst[min_i+1:max_i])} ")
    mediana=statistics.median(lst[min_i+1:max_i])
    for i in range(min_i+1, max_i):
        lst[i] = mediana
    print (f"Измененный массив {lst}")
elif (min_i+1==max_i):
    print ("Макс и мин числа находятся рядом ")
else:
    print ("Минимальное число находится после максимального")
