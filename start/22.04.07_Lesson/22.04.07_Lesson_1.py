stroka= str(input("Введите постфиксную запись:")).split()
stack = []
flag=True
for i in stroka:
    if i in "+-*/": 
        a = stack [-2]
        b =  stack [-1]
        stack.pop()
        stack.pop()
        if i == "+": 
            result = a + b 
        elif i =="-":
            result = a - b
        elif i =="/":
            if (b==0):
                print("Нельзя делить на ноль")
                flag=False
                break
            else:
                result = a / b
        else: 
            result = a*b 
        stack.append(result)
    else: 
        stack.append(int(i))
if (flag==True):
    print (stack[0])
