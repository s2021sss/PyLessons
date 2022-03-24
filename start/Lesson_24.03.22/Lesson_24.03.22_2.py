import matplotlib.pyplot as plt
import requests
import statistics
file_lst = requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat")
file_float = [float(x) for x in file_lst.text.split()]
print (f"Максимальная температура {max(file_float)}")
print (f"Минимальная температура {min(file_float)}")
print (f"Средняя температура {round(statistics.mean(file_float), 2)}")
print (f"Количество уникальных значений: {len(list(set(file_float)))}")
y = file_float
plt.plot(y)
plt.show()
