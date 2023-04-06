# Импортируем объект Counter из модуля collections
from collections import Counter
# Создаём пустой объект Counter
c = Counter()
c['red'] += 1
print(c)
# Будет напечатано:
# Counter({'red': 1})

cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c = Counter()
for car in cars:
    c[car] += 1
print(c)
c = Counter(cars)
print(c)
# Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})


cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
print(counter_moscow)
print(counter_spb)
# Counter({'black': 4, 'yellow': 3, 'white': 2})
# Counter({'white': 3, 'red': 2, 'black': 2, 'yellow': 2})
print(counter_moscow + counter_spb)
# Counter({'black': 6, 'white': 5, 'yellow': 5, 'red': 2})


print(counter_moscow)
print(counter_spb)
# Counter({'black': 4, 'yellow': 3, 'white': 2})
# Counter({'white': 3, 'red': 2, 'black': 2, 'yellow': 2})
counter_moscow.subtract(counter_spb)
print(counter_moscow)
# Counter({'black': 2, 'yellow': 1, 'white': -1, 'red': -2})


cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
print(*counter_moscow.elements())
# black black black black white white yellow yellow yellow




