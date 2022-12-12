# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06
def enterNum():
    while True:
        try:
            num = int(input('Enter the number type of int: '))
            return num
            break
        except:
            print('Type not int.')

def sequence(num):
    if num == 0:
        return
    else:
        return (1+1/num)**num

def MyList(num):
    # myList = []
    myList = [sequence(num) for num in range(1, num + 1) ]
    # for num in range(1, num + 1):
    #     myList.append(sequence(num))
    print(myList)
    print(sum(myList))

num=enterNum()
MyList(num)