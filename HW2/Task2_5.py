# Реализуйте алгоритм перемешивания списка.

from random import shuffle
from random import randint

list=[]
for i in range(0,10):
    list.append(randint(0,100))
print(f'List: {list}')
shuffle (list)
print(f'Mixed list: {list}')