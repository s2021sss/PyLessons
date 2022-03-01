import math
def my_log(lst):
    print([math.log(i) if i>0 else None for i in lst ])
my_log([1, 3, 2.5, -1, 9, 0, 2.71])
