import statistics
lst=[94, 6, 8, 66, 12, 2, 95, 57, 45, 3, 89, 34]
min_i=lst.index(min(lst))
max_i=lst.index(max(lst))
if (min_i+1<max_i):
    print (f"Среднее арифметическое: {statistics.mean(lst[min_i+1:max_i])} ")
elif (max_i+1<min_i):
    mediana=statistics.median(lst[max_i+1:min_i])
    for i in range(max_i+1,min_i):
        lst[i] = mediana
    print (f"Измененный массив {lst}")
elif (min_i+1==max_i or min_i-11==max_i ):
    print ("Макс и мин числа находятся рядом ")
