import statistics
student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)
print(f"Студент: { {student[0].split()[1]}, {student[0].split()[0]} }")
print(f"Возраст: в 2021 {2021 - student[1]}")
print(f"Оценки: {tuple(student[2])}")
print(*student[2], sep=", ")
print(f"Cредний балл {round(statistics.mean(student[2]), 1)}")
if round(statistics.mean(student[2]), 1)>= 8 and student[3]:
   print(True)
else:
   print(False)
