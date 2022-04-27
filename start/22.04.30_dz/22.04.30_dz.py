class Hotel:
    _prices = {"SGL": 2000, "DBL": 3000, "Junior Suite": 5000, "Suite": 10000} 
    _roomTypes = list(_prices.keys())
    _rooms = dict()
    
    def __init__(self, numberOfRooms):
        for num in range(len(numberOfRooms)):
            self._rooms[self._roomTypes[num]]=[1]*numberOfRooms[num]

    def occupy (self, typeOfRoom, NumRoom):
        if (self._rooms[typeOfRoom][NumRoom-1]==1):
            self._rooms[typeOfRoom][NumRoom-1] = 0
            print (f"Номер {NumRoom} забронирован в {typeOfRoom} \n")
        else:
            raise RuntimeError("Номер занят")

    def __str__(self):
        roomsInfo = ""
        for typ in self._roomTypes:
            typeInfo = f"Тип {typ}: \n"
            for num in range(len(self._rooms[typ])):
                if self._rooms[typ][num]==1:
                    typeInfo += f"{num+1} номер свободен \n"
                else:
                    typeInfo += f"{num+1} номер занят \n"
            roomsInfo += typeInfo
        return roomsInfo


    def all_occypy(self):
        for typ in self._roomTypes:
            for num in range(len(self._rooms[typ])):
                self._rooms[typ][num]=0
        

    def all_free(self):
        for typ in self._roomTypes:
            for num in range(len(self._rooms[typ])):
                self._rooms[typ][num]=1

    def occupy_rate(self):
        occupyInfo="Процент занятых номеров: \n"
        for typ in self._roomTypes:
            occupyInfo += f"Тип {typ}: {round(self._rooms[typ].count(0)/len(self._rooms[typ])*100, 2)}% \n"
        return occupyInfo

    def income(self):
        income=0
        for typ in self._roomTypes:
            income += (self._rooms[typ].count(0)) * self._prices[typ]
        return f"Выручка {income} \n"

    def change_prices(self, typeOfRoom, newPrice): ##Изменить цену на какой-то тип номера
        self._prices[typeOfRoom] = newPrice
        price = "Новые цены на номера \n"
        for typ in self._roomTypes:
            price += f"{typ} - {self._prices[typ]} \n"
        return price
    
    def pricesAll(self): ##Цены на разные типы номеров
        price = "Текущие цены на номера \n"
        for typ in self._roomTypes:
            price += f"{typ} - {self._prices[typ]} \n"
        return price
        

hotel = Hotel((2, 3, 4, 5))
hotel.occupy("SGL", 1) 
hotel.occupy("DBL", 1)
hotel.occupy("DBL", 2)
hotel.occupy("DBL", 3)
hotel.occupy("Suite", 4)
print(hotel)
print (hotel.occupy_rate())
print (hotel.income())
print (hotel.pricesAll())
print (hotel.change_prices("SGL", 1111))
hotel.all_occypy()
print (hotel.occupy_rate())
hotel.all_free()
print (hotel.occupy_rate())
