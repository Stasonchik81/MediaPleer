# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

def enterNum():
    while True:
        try:
            num = float(input('Enter the number type of float: '))
            return num
            break
        except:
            print('Type not float.')

def amount(num:float):
    sum=0
    temp = str(num)
    temp=temp.replace('.','')
    for i in range(len(temp)):
        sum += int(temp[i])
    print(f'The sum of the digits of the number = {sum}')

num = enterNum()
amount(num)






