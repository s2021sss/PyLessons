s = int(input("Введите число "))
lst = {1, 3, 6, 49, 40, 62, 71, 31, 10, 70, 11, 55, 26, 86, 15}
lst=sorted(lst)
razn = max(lst)
for i in lst:
   if abs(s - i)<razn:
       razn = abs(s - i)
       num = i
print(num)
