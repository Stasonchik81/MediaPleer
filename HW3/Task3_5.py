# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

F = int(input('Enter a number to calculate the Fibonacci series: '))
MyList=[]

def fib(n):
     if n == 0:
         return 0
     elif n ==1:
         return 1
     elif n ==-1:
         return 1
     elif n < -1:
         return fib (n+2) - fib (n+1)
     else:
         return fib (n-1) + fib (n-2)

for i in range(-F,F+1):
    MyList.append(fib(i))

print(MyList)