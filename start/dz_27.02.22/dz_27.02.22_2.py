import random
def random_password():
    kol = random.randrange(7, 11)
    password=""
    for i in range (1, kol+1):
        password+=chr(random.randrange(33, 126))
    print (f'Ваш пароль из {kol} символов: {password}')

random_password()
