import requests
file = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/text.txt").text
uppercase = 0
spaces = 0
digits = 0
for elem in file:
    if elem == " ":
        spaces += 1
    elif elem.isupper():
        uppercase += 1
    elif elem.isdigit():
        digits += 1
print (f"Количество заглавных букв {uppercase}, количество цифр {digits}, количество пробелов {spaces}")
