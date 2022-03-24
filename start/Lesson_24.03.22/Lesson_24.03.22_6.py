import requests
file = requests.get("http://dfedorov.spb.ru/python3/src/romeo.txt").text.split()
counter_elem = {elem: file.count(elem) for elem in file}
sorted_elem = sorted(counter_elem.items(), key=lambda x: x[1])[::-1]
print ("Частота использования слов:")
for elem in sorted_elem:
    print (dict({elem}))
