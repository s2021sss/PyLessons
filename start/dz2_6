import math 
tip=input("Введите тип фигур: Круг, Треугольник или прямоугольник ")
tip=tip.replace(" ", "").title()
if (tip=="Круг"):
    r=int (input ("Введите радиус круга: "))
    print ("Площадь круга равна: ", round(pow(r, 2)*math.pi, 2))
elif (tip=="Треугольник"):
    a=int(input ("Введите длину стороны A: "))
    b=int(input ("Введите длину стороны B: "))
    c=int(input ("Введите длину стороны C: "))
    p=(a+b+c)/2
    s=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),2)
    print ("Площадь треугольника равна: ", s)
elif (tip=="Прямоугольник"):
    a=int(input ("Введите длину стороны A: "))
    b=int(input ("Введите длину стороны B: "))
    print ("Площадь прямоугольника равна: ", round(a*b,2))
else:
    print ("Вы неправильно ввели фигуру")
