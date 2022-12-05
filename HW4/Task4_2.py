# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def EnterNum():
    while True:
        try:
            num = int(input('Enter your number for the definition prime factors: '))
            break
        except:
            print('Number must be type of the integer.')
    return num

num = EnterNum()
print(num)

def DefinitionPrimeFactors(num:int):
    factord=[]
    divider=2
    while num != 1:
        if num % divider == 0:
            factord.append(divider)
            num //= divider
        else:
            divider+=1
    return factord

factord = DefinitionPrimeFactors(num)
print(factord)



