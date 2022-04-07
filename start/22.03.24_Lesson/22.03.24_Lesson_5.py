import requests
import random
answers = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/responses.txt").text.split("\n")
print ("Чтобы заврешить программу введите q")
while (True):
    comanda = input("Введите вопрос: ")
    if (comanda=="q"):
        break
    print (random.choice(answers))
