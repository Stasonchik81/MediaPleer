# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint as rand

def EnterLenOfList():
    while True:
        try:
            LenOfList=int(input('Enter the length of the list: '))
            break
        except:
            print('Mistake! Lenght must be type of the integer.')
    return LenOfList

def FillList (LenOfList:int):
    MyList=[rand(1,9) for i in range(LenOfList)]
    print(MyList)
    return MyList

def SumOfElements(MyList:list):
    # NewList=[]
    if len(MyList)%2==0:
        size = len(MyList)//2
    else:
        size = (len(MyList) // 2)+1

    NewList=list(map(lambda i: MyList[i] * MyList[-(i + 1)], range(size)))

    # for i in range(size):
    #     NewList.append(MyList[i] * MyList[-(i + 1)])
    print(NewList)

LenOfList = EnterLenOfList()
MyList=FillList(LenOfList)
SumOfElements(MyList)