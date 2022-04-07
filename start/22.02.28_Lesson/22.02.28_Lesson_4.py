import random
lst = [random.randint(100, 200) for _ in range(1000)]
print(f"Сумма: {sum(i if 170 < i < 195 else 0 for i in lst)}")
print(f"Количество: {sum(1 if 170 < i < 195 else 0 for i in lst)}")
