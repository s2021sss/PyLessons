import random
def good_password():
    k=0
    while True:
        kol = random.randrange(7, 11)
        password=""
        for i in range (1, kol+1):
            password+=chr(random.randrange(33, 126))
        flag1=flag2=flag3=0
        k +=1
        if (len(password)>=8):
            for i in password:
                if (i.isupper()):
                    flag1 += 1
                elif (i.islower()):
                    flag2 += 1
                elif (i.isdigit()):
                    flag3 += 1
        if (flag1>0 and flag2>0 and flag3>0):
            print (f"Надежный пароль {password} сгенерировался с {k} раза")
            break
good_password()
