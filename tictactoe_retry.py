from random import randrange, triangular 

board = [[i+j*3+1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'

def displayBoard(board):
    print('+-------' * 3 + '+\n', end='')
    for row in range(3):
        print('|       ' * 3 + '|')
        for column in range(3):
            print('|   ' + str(board[row][column]) + '   ', end='')
        print('|')
        print('|       ' * 3 + '|')
        print('+-------' * 3 + '+\n', end='')
    return board

def playerMove(board):
    sign = ['O', 'X']
    correct = False
    while not correct:
        move = input('Enter a move: ')
        correct = move >= '1' and move <= '9'
        if not correct:
            print('Invalid move! Try again.')
            continue
        move = int(move) - 1
        column = move % 3
        if move < 3:
            if board[0][column] not in sign:
                board[0][column] = 'O'
                break
            else:
                print('The space is filled.')
                correct = False
                continue
        elif move >= 3 and move <= 5:
            if board[1][column] not in sign:
                board[1][column] = 'O'
            else:
                print('The space is filled.')
                correct = False
                continue
        else:
            if board[2][column] not in sign:
                board[2][column] = 'O'
            else:
                print('The space is filled.')
                correct = False
                continue
    return displayBoard(board)

def freeFields(board):
    freeSqrs = []
    sign = ['O', 'X']
    for row in range(3):
        for column in range(3):
            if board[row][column] not in sign:
                freeSqrs.append((row, column))
    return freeSqrs

def computerMove(board):
    cell = freeFields(board)
    ok = False
    while not ok:
        move = randrange(10)
        for row in range(3):
            for column in range(3):
                if board[row][column] == move and (row, column) in cell:
                    board[row][column] = 'X'
                    ok = True
                else:
                    continue
    return displayBoard(board)

def victory(board, sign):
    if sign == 'O':
        winner = 'player'
    elif sign == 'X':
        winner = 'computer'

    diagonal1 = 0 
    diagonal2 = 0
    for cell in range(3):
        if board[0][cell] == sign and board[1][cell] == sign and board[2][cell] == sign:
            return winner
        elif board[cell][0] == sign and board[cell][1] == sign and board[cell][2] == sign:
            return winner
        elif board[cell][cell] == sign:
            diagonal1 += 1
        if board[cell][2-cell] == sign:
            diagonal2 += 1
    if diagonal1 == 3 or diagonal2 == 3:
        return winner
    return None

displayBoard(board)
# gameOver = len(freeFields(board)) == 0
winner = None
while len(freeFields(board)) != 0:
    playerMove(board)
    if victory(board, 'O'):
        winner = 'player'
        break
    computerMove(board)
    if victory(board, 'X'):
        winner = 'computer'
        break

if winner == 'computer':
    print('You lose.')
elif winner == 'player':
    print('You win!')
else:
    print('Tie.')