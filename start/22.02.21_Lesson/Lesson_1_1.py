L = [3, 6, 7, 4, -5, 4, 3, -1]
s = sum(L)
if s>2:
    print (f"Сумма элементов: {len(L)}")
razn = min(L) - max(L)
if razn>10:
    print (L.sort(reverse=True))
else:
    print ("Разность меньше 10")
