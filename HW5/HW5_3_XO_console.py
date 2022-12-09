# Создайте программу для игры в "Крестики-нолики"

from random import randint as rand

def EnterName(text:str):
    PlayerName = input(f'Enter {text} name: ')
    return PlayerName

def board():
    board={}
    for i in range(1,10):
        board[i] = i
    print(board[i])
    return board

def CreateBoard(board:dict):
    count=0
    print('------------------')
    for i in board:
        if count != 2:
            print(f'{board[i]:^5}|', end='')
            count += 1

        else:
            print(f'{board[i]:^5}|')
            count = 0
            print('------------------')

def ChoosePlayersMove(FirstPlayerName:str, SecondPlayerName:str):
    move = rand(1,2)
    if move==1:
        print(f'{FirstPlayerName} goes first!')
        return FirstPlayerName
    else:
        print(f'{SecondPlayerName} goes first!')
        return SecondPlayerName

def WinnerCombinations(board:dict):
    return ((board[1] == board[2] == board[3]) or
            (board[4] == board[5] == board[6]) or
            (board[7] == board[8] == board[9]) or
            (board[1] == board[5] == board[9]) or
            (board[3] == board[5] == board[7]) or
            (board[1] == board[4] == board[7]) or
            (board[3] == board[6] == board[9]) or
            (board[2] == board[5] == board[8]))

def CheckInputMove(Name:str):
    while True:
        try:
            PlayerMove = int(input(f' {Name} is move:'))
            return PlayerMove
            break
        except:
            print('Entered "MOVE" must be type of the integer and from 1 to 9')

def CheckMatches(move:str, PlayerMove:int, board:dict):
    while True:
        if board[PlayerMove] == 'X' or board[PlayerMove] == '0':
            print(f'{move} - Cell is occupied!')
            PlayerMove = CheckInputMove(move)
        else:
            return PlayerMove

def Play(FirstPlayerName:str, SecondPlayerName:str, board:dict, move:str):
    count=0
    while count!=9:
        if move==FirstPlayerName:
            PlayerMove = CheckInputMove(FirstPlayerName)
            CheckPlayerMove = CheckMatches(move, PlayerMove,board)
            board[CheckPlayerMove] = 'X'
            CreateBoard(board)
            Winner = WinnerCombinations(board)
            if Winner == True:
                print(f'{FirstPlayerName} - You are winner!!!!!!!!!')
                break
            move = SecondPlayerName
            count += 1
        else:
            PlayerMove = CheckInputMove(SecondPlayerName)
            CheckPlayerMove = CheckMatches(move, PlayerMove, board)
            board[CheckPlayerMove] = '0'
            CreateBoard(board)
            Winner = WinnerCombinations(board)
            if Winner == True:
                print(f'{SecondPlayerName} - You are winner!!!!!!!!!')
                break
            move = FirstPlayerName
            count += 1
    print('End')


FirstPlayerName = EnterName('first player')
SecondPlayerName = EnterName('second player')

PlayerBoard = board()
DrawBoard = CreateBoard(PlayerBoard)

ChooseMove = ChoosePlayersMove(FirstPlayerName, SecondPlayerName)

Play(FirstPlayerName, SecondPlayerName, PlayerBoard,ChooseMove)





# Field={}
# for i in range(1,10):
#     Field[i] = i
#     print(Field)
#
# move = int(input('Enter your move: '))
# Field[move] = 'x'
# print(Field)







