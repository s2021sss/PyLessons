def test_password (password):
    flag1=flag2=flag3=0
    if (len(password)>=8):
        for i in password:
            if (i.isupper()):
                flag1 += 1
            elif (i.islower()):
                flag2 += 1
            elif (i.isdigit()):
                flag3 += 1
    if (flag1>0 and flag2>0 and flag3>0):
        print ("True")
    else:
        print ("False")
test_password("hhhhhhhhhh")
test_password("HHHHHHHHHH")
test_password("HHgg86")
test_password("QWERTy123")
        

        
