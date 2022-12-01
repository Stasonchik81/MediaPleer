# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на
# нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

from random import randint as rand

def enterLen():
    while True:
        try:
            num = int(input('Enter length of the list: '))
            break
        except:
            print('Mistake! Lenght must be type of the integer.')
    return num

lenOfList = enterLen()

def fillList(lenOfList:int):
    myList= [rand(1,10) for i in range(lenOfList)]
    print(myList)
    return myList

myList = fillList(lenOfList)

def sumOfList (myList:list):
    summa=myList[0]
    for i in range(len(myList)):
        if i%2!=0:
            summa+=myList[i]
    print(summa)

sumOfList(myList)
