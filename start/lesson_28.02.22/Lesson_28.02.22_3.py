import statistics
import random
print(statistics.median((random.randint(-100, 100) for _ in range(100))))
