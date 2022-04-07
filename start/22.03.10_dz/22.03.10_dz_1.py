def summa(user):
    s=0
    for item in list(user.values()):
        s=s+list(item.values())[1]*list(item.values())[0]
    print (f"Сумма заказа: {s}")
summa({'Камин комплект Старый Замок':
{'count': 1, 'price': 28490}, 
'Полусапоги Betsy':{'count': 2, 'price': 2399}, 
'Семь навыков высокоэффективных людей':{'count': 1, 'price': 437}})
