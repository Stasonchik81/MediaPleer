# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 (я беру 150, чтобы было быстрее проверять, а то 2021 не натыкаешься :) ) конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint as rand

def EnterName(name:str):
    PlayerName=input(f'Enter {name} name: ')
    return PlayerName

def out_red(text):
    print("\033[31m {}".format(text))

def out_blue(text):
    print("\033[34m {}".format(text))

def out_yellow(text):
    print("\033[33m {}".format(text))

def PrintRools(FirstPlayerName:str, SecondPlayerName:str):
    print(' ',
          f'Hellow {FirstPlayerName} and {SecondPlayerName}!!!',
          ' ',
          'There is a 150 candys on the table. Two players are playing, making a move after each other.',
          'The first move is determined by drawing lots. In one move, you can pick up no more than 28 candies.',
          'All the opponents candies go to the one who made the last move.',
          'How many candies does the first player need to take in order to take all the candies from his competitor?', sep='\n')

def ChoosePlayerMove(FirstPlayerName:str, SecondPlayerName:str):

    Move = rand(1,2)

    if Move==1:
        PlayerName=FirstPlayerName
    elif Move==2:
        PlayerName=SecondPlayerName
    out_red('...')
    print(' ',
          f"{PlayerName} is beginner!!!",
          ' ', sep='\n')
    return PlayerName

def CheckCandys(PlayerName:str):
    MaxCandys=28
    PlayerMove = int(input(f"{PlayerName}'s move: "))
    while True:
        if PlayerMove > MaxCandys or PlayerMove <= 0:
            print(f'No! No! No! {PlayerName}, your must take from 1 to 28 candys!')
            PlayerMove = int(input(f'{PlayerName} move: '))
        else:
            return PlayerMove

def CheckVinner(PlayerName:str, Candys:int):
    if Candys <=28 and PlayerName == FirstPlayerName:
        out_red('...')
        out_red(f'{FirstPlayerName} is vinner!!!')
        return 1
    elif Candys <=28 and PlayerName == SecondPlayerName:
        out_red('...')
        out_red(f'{SecondPlayerName} is vinner!!!')
        return 2

def TakeCandy(FirstPlayerName:str, SecondPlayerName:str):
    PlayerName = ChoosePlayerMove(FirstPlayerName, SecondPlayerName)
    Candys = 118
    while Candys>0:
        if PlayerName == FirstPlayerName:
            Vinner = CheckVinner(PlayerName, Candys)
            if Vinner == 1:
                break
            out_blue('...')
            FirstPlayerNameMove = CheckCandys(FirstPlayerName)
            Candys -= FirstPlayerNameMove
            out_blue(f'Remained {Candys}...')
            PlayerName=SecondPlayerName
        elif PlayerName == SecondPlayerName:
            Vinner = CheckVinner(PlayerName, Candys)
            if Vinner == 2:
                break
            out_yellow('...')
            SecondPlayerNameMove = CheckCandys(SecondPlayerName)
            Candys -= SecondPlayerNameMove
            out_yellow(f'Remained {Candys}...')
            PlayerName = FirstPlayerName


FirstPlayerName = EnterName('First player name')
SecondPlayerName = EnterName('Second player name')
PrintRools(FirstPlayerName, SecondPlayerName)
TakeCandy(FirstPlayerName, SecondPlayerName)




