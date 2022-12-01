# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def EnterNum():
    while True:
        try:
            Num=int(input('Enter number for the transformation: '))
            break
        except:
            print('Mistake! Number must be type of the integer.')
    return(Num)

Num = EnterNum()

def Transformation(num:int):
    ListOfNum=[]
    while num!=0:
        ost = round(num % 2, 1)
        ListOfNum.append(ost)
        num = num // 2
    for i in reversed(ListOfNum):
        print(i, end='')

Transformation(Num)