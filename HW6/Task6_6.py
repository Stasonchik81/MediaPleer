# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

def EnterSequence():
    while True:
        try:
            myList = list(map(int, input('Enter the list separated by a space: ').split()))
            break
        except:
            print('Number in the list must be integer.')
    return myList

def NoReplay(myList:list):
    NewList=[i for i in myList if myList.count(i)==1]
    print(f'List of non-repeating elements: {NewList}')

myList = EnterSequence()
NoReplay(myList)