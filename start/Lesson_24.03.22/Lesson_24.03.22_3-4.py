import requests
#задание 3
file = requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt").content.split()
replace_file = [str(elem)[2:-1].lower().replace(",", '').replace(".", '').replace("--", '') for elem in file]
with open("moby_clean.txt", "w", encoding='utf-8') as file:
    for elem in replace_file:
        file.write(elem + "\n")
#задание 4
counter_elem = {elem: replace_file.count(elem) for elem in replace_file}
sorted_elem = sorted(counter_elem.items(), key=lambda x: x[1])[::-1]
print (f"Самые частые слова {dict(sorted_elem[0:5])}, \nCамые редкие слова {dict(sorted_elem[-5:])}")

