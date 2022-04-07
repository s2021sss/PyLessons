s = 0
for i in range(5):
   i = int(input("Введите число "))
   otvet = input("Добавить это число к сумме: да или нет ").lower()
   if otvet=="да":
       s+=i
print(s)
