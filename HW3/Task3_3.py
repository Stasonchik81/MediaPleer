# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

import random

def EnterNum():
    while True:
        try:
            LenOfList=int(input('Enter the length of the list: '))
            break
        except:
            print('Mistake! Lenght must be type of the integer.')
    return(LenOfList)

LenOfList=EnterNum()

def FillList(LenOfList:int):
    MyList=[]
    MyList=[random.uniform(1,9) for i in range(LenOfList)]
    print(MyList)
    return(MyList)

MyList = FillList(LenOfList)

def SumOfList(MyList:list):
    SumOfElements=0.0
    for i in range(len(MyList)):
        SumOfElements+=MyList[i]%1
    print("%.2f" % SumOfElements)

SumOfList(MyList)


