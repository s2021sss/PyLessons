lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 14, 46, 273, 22, 99, 15, 1000]
s=0
for i in lst:
    if ((i>10 and i<100) or (i>200 and i<500)):
        s += i;
print (s)