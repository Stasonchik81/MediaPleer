# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141
# Ввод: 0.01   Вывод: 3.14
# Ввод: 0.001  Вывод: 3.141

import math

def SettingAccuracy ():
    while True:

        try:
            accuracy = float(input('Enter accuracy: '))
            if 0 < accuracy and accuracy <= 0.1:
                break
            else:
                print('The accuracy should be in the range from 0 to 0.1')
        except:
            print('Accuracy must be type of the float.')

    return accuracy

accuracy = SettingAccuracy()

def DefinitionAccuracy(accuracy: float):
    count = 1
    while accuracy!=0.1:
        accuracy*=10
        count+=1
    return count

definition = DefinitionAccuracy(accuracy)

print(f'%.{definition}f' % math.pi)


