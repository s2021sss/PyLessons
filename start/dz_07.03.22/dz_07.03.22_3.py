def is_digit(s):
    if s.isdigit():
       return True
    else:
        try:
            float(s)
            return True
        except ValueError:
            return False
lst=[1, 5, 6.3, 6, None, 2.0, -4, None]
s=0
k=0
for i in lst:
    if(is_digit(str(i))):
        s=s+i
        k+=1
sred=round(s/k,2)
for i in range(len(lst)):
    if (str(lst[i])=="None"):
        lst[i]=sred
print (lst)
