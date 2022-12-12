# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

def enterNum():
    while True:
        try:
            num = int(input('Enter the number type of int: '))
            return num
            break
        except:
            print('Type not int.')

num=enterNum()

def row (num):
    mylist = [i for i in range(-num, num+1)]
    # for i in range(-num, num+1):
    #     mylist.append(i)

    return mylist

myList = row(num)
print(myList)

myIndex = list(map(int, input('Enter the index: ').split()))

sum=1
for i in myIndex:
    sum*=myList[i]

print(sum)