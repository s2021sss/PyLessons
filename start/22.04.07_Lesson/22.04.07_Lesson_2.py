def check_delimiter(stroka):
    print ("Строка: " + stroka)
    stroka=stroka.split()
    stack = []
    flag = True
    for i in stroka:
        if i in "([{":
            stack.append(i)
        else:
            if ((i == ")" and stack[-1]=="(") or (i == "]" and stack[-1]=="[") or (i == "}" and stack[-1]=="{")):
                stack.pop()
            else:
                flag=False
    return (flag)
print(check_delimiter("( ) { [ ] ( ) { } }"))
print(check_delimiter("( ) { [ ] }") )
print(check_delimiter("( ) { [ ] ( ] { } }"))
print ("Алгоритм 2: ")
def check_delimiter2(stroka):
    print ("Строка: " + stroka)
    stroka="".join(stroka.split())
    while '()' in stroka or '[]' in stroka or '{}' in stroka:
        stroka = stroka.replace('()', '')
        stroka = stroka.replace('[]', '')
        stroka = stroka.replace('{}', '')
    return not stroka
print(check_delimiter2("( ) { [ ] ( ) { } }"))
print(check_delimiter2("( ) { [ ] }") )
print(check_delimiter2("( ) { [ ] ( ] { } }"))
