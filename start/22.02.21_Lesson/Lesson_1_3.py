line = ["Автово", "Кировский завод", "Нарвская", "Балтийская",  "Технологический институт 1", "Пушкинская", "Владимирская", "Площадь Восстания"]
moment=(input("Текущая станция: ")).title()
print (f"Следующая станция: {line[line.index(moment)+1]}")