lst = ['aba', 12321, 'aaccdccaa']
print(all(map(lambda x: x == x[::-1], list(map(str, lst)))))
