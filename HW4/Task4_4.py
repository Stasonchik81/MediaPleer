# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

from random import randint as rand

def EnterDegree():
    while True:
        try:
            degree = int(input('Enter degree: '))
            break
        except:
            print('Degree must be type of the integer: ')
    return degree

degree = EnterDegree()
degree2 = EnterDegree()

def GenerateDictOfRatios(degree:int):
    DictOfRatios={i:rand(-10,10) for i in range(degree,-1,-1)}
    return DictOfRatios

DictOfRatios = GenerateDictOfRatios(degree)
DictOfRatios2 = GenerateDictOfRatios(degree2)
"""
def EnterNameOfFile():
    while True:
        try:
            nameOfFile = str(input('Enter name of your file: '))
            break
        except:
            print('Name must be type of the string: ')
    return nameOfFile

Polinom = EnterNameOfFile()
Polinom2 = EnterNameOfFile()
"""
Polinom = 'Polinom'
Polinom2 = 'Polinom2'

def GenerationPolinomial(DictOfRatios:dict, nameOfFile:str):
    with open(f'{nameOfFile}.txt','w') as polinom:
        a=True
        for key, value in DictOfRatios.items():
            if a == True and value>0:
                polinom.write(f'{value}x^{key}')
            elif key==1 and value > 0:
                polinom.write(f'+{value}x')
            elif key==1 and value < 0 :
                polinom.write(f'{value}x')
            elif key!=0 or key==0 and value > 0 :
                polinom.write(f'+{value}x^{key}')
            elif key!=0 or key == 0 and value < 0 :
                polinom.write(f'{value}x^{key}')
            """
            elif key == 0 and value > 0:
                polinom.write(f'+{value}')
            elif key == 0 and value < 0:
                polinom.write(f'{value}')
            """
            a = False
        polinom.write(' = 0')

GenerationPolinomial(DictOfRatios, Polinom)
GenerationPolinomial(DictOfRatios2,Polinom2)










