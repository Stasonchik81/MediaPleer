# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def enterNum():
    while True:
        try:
            num = int(input('Enter the number type of int: '))
            return num
            break
        except:
            print('Type not int.')

def factorial(num:int):
    if num<0:
        print(f'{num} - the factorial for negative numbers is not calculated.')
    if num == 1:
        return num
    else:
        return num * factorial(num-1)

def MyList(num:int):
    mylist = []

    for num in range(1, num + 1):
        # list.append(math.factorial(num))
        mylist.append(factorial(num))

    print(mylist)

num = enterNum()
MyList(num)

