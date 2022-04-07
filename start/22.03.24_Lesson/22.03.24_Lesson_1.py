a = input ("Введите первое число:")
b = input ("Введите первое число:")
comanda = input ("Введите команду: ")
try:
    a = int(a)
    b = int(b)
    if (comanda == "/"):
        delen(a, b)
    elif (comanda == "+"):
        sym(a, b)
    elif (comanda == "-"):
        vichit(a, b)
except ValueError as err:
    print("Ошибка преобразования типов!")

def vichit(a, b):
    print (f"Результат: {a-b}")
def sym(a, b):
    print (f"Результат: {a+b}")
def delen(a, b):
    if (b != 0):
        print (f"Результат: {int(a/b)}")
    else:
        print ("Ошибка деления на ноль!")
