# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

# def enterNum():
#     while True:
#         try:
#             num = float(input('Enter the number type of float: '))
#             return num
#             break
#         except:
#             print('Type not float.')
#
# def amount(num:float):
#     sum=0
#
#     temp = str(num)
#     temp=temp.replace('.','')
#
#     for i in range(len(temp)):
#         sum += int(temp[i])
#     print(f'The sum of the digits of the number = {sum}')
#
# num = enterNum()
# amount(num)

num = list(map(str, input('Enter float num: ') + ' '))
summa=0
newList = [i for i in num if i.isdigit()]
newList = list(map(int,newList))
res = list(summa:= summa + i for i in newList)
print(newList)
print(res)
