def protsent_zaprosov(queries: list):
    k=0
    kolzaprosov = dict()
    for item in queries:
        k +=1
        if len(item.split()) in kolzaprosov:
            kolzaprosov[len(item.split())]+=1
        else:
            kolzaprosov[len(item.split())]=1
    for i in kolzaprosov:
        print (f"Поисковых запросов, содержащих {i} слов(а): {round(kolzaprosov[i]/k*100, 2)}%")

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

protsent_zaprosov(queries)
