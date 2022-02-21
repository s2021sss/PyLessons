import random
l=["самовар", "весна", "лето"]
word = l[random.randint (0, len(l)-1)]
letter=word[random.randint(0,len(word)-1)]
print (word.replace(letter, "?", 1))
letter_2=input("Угадайте букву: ")
if (letter==letter_2):
    print ("Победа!")
else:
    print ("Увы! Попробуйте в другой раз")

