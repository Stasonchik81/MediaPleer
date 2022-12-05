# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).
import Task4_4


def ReadEquation(nameOfFile:str):
    with open(f'{nameOfFile}.txt','r') as file:
        polinom = file.readline()
    return polinom

Polinom = ReadEquation('Polinom')
Polinom2 = ReadEquation('Polinom2')

print(Polinom)
print(Polinom2)

def ParsingPolinom(Polinom:str):
    Polinom = Polinom.replace('x^',' ').replace('x',' 1').replace('+',' ').replace('-',' -')
    Polinom = Polinom.split()
    Polinom = Polinom[:-2]

    return Polinom

Polinom = ParsingPolinom(Polinom)
Polinom2 = ParsingPolinom(Polinom2)

def CreateDict(Polinom:list):
    DictOfPoli={}
    for i in range(0,len(Polinom),2):
        key = int(Polinom[i+1])
        value = int(Polinom[i])
        #DictOfPoli[int(Polinom[i][1])] = int(Polinom[i][0]) - не понимаю почему, но это не работает(((
        DictOfPoli[key] = value
    return DictOfPoli

DictOfPoli = CreateDict(Polinom)
DictOfPoli2 = CreateDict(Polinom2)
print(DictOfPoli)
print(DictOfPoli2)

def SumOfDict(Dict:dict, Dict2:dict):
    SummaOfDictionary={}
    for i in range(max(len(Dict),len(Dict2)),-1,-1):
        first = Dict.get(i)
        second = Dict2.get(i)
        if first!=None or second!=None:
            SummaOfDictionary[i] = (first if first != None else 0) + (second if second != None else 0)
    return SummaOfDictionary

SummaOfDict = SumOfDict(DictOfPoli,DictOfPoli2)
print(SummaOfDict)

def WriteToFile(SummaOfDict:dict):
    with open ('SummaOfDict.txt', 'w') as Summa:
        Summa.writelines(str(SummaOfDict))

WriteToFile(SummaOfDict)

Task4_4.GenerationPolinomial(SummaOfDict, 'SummaOfDictPoli.txt')


