import random
num = random.randrange(1, 11)
while True:
    guess=int(input("Попробуйте угадать число от 1 до 10: "))
    if (num==guess):
        print ("Вы угадали число!")
        break
    elif(num>guess):
        print ("Неправильно, загаданное число больше! ")
    else:
        print ("Неправильно, загаданное число меньше! ")
