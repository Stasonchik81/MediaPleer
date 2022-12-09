# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open ('RLE.txt', 'w') as RLE:
    text = input('Введите даннные для сжатия: ')
    RLE.write(text)

def RLEplus(text:str):
    MyList = []
    num = None
    count = 0
    for i in text:
        if i != num:
            if count>=1:
                MyList.append(count)
            count = 0
            num = i
            count += 1
            MyList.append(i)
        elif i == num:
            count += 1
    MyList.append(count)
    print(f'Запакованный файл: {MyList}')
    return MyList

MyList2 = RLEplus(text)

with open ('RLEplus.txt','w+') as plus:
    plus.write(str(MyList2))

def RLEunpack(MyList2:list):
    MyL = []
    for i in range(0, len(MyList2), 2):
        count = MyList2[i + 1]
        while count != 0:
            MyL.append(MyList2[i])
            count -= 1
    return MyL

MyList3 = RLEunpack(MyList2)
print(f'Распакованный файл: {MyList3}')

with open ('RLEunpack.txt', 'w+') as RLEU:
    RLEU.write(str(MyList3))