import sys
# TODO: Player can move
# TODO: AI moves accordingly
# TODO: Checks who wins at every turn

# Refer this to apply minimax algorithm: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/


board = {'topL': ' ', 'topM': ' ', 'topR': ' ',
        'midL': ' ', 'midM': ' ', 'midR': ' ',
        'bottomL': ' ', 'bottomM': ' ', 'bottomR': ' '}

# positions = ['topL', 'topM', 'topR', 'midL', 'midM', 'midR', 'bottomL', 'bottomM', 'bottomR']

def printBoard(board):
    print(' ' + board['topL'] + ' | ' + board['topM'] + ' | ' + board['topR'])
    print('-----------')
    print(' ' + board['midL'] + ' | ' + board['midM'] + ' | ' + board['midR'])
    print('-----------')
    print(' ' + board['bottomL'] + ' | ' + board['bottomM'] + ' | ' + board['bottomR'])

def countValue(board, value):
    n = 0
    colum = list()
    for key in board.keys():
        if value in board[key]:
            n += 1
            colum.append(key)
    return n, colum

def canMove(position):
    r = board.keys()
    if position in r and board[position] == ' ':
        return True
    return False

def move(move):
    whee = True
    while whee:
        position = input('Enter position to insert your move(topM,midL etc): ')
        if canMove(position):
            board[position] = move
            whee = False
        else:
            print('Insert move into a valid position')

def canWin(board, move):
    return ((board['topL'] == move and board['topM'] == move and board['topR'] == move) or
            (board['topL'] == move and board['midM'] == move and board['bottomR'] == move) or
            (board['midL'] == move and board['midM'] == move and board['midR'] == move) or
            (board['topR'] == move and board['midM'] == move and board['bottomL'] == move) or
            (board['bottomL'] == move and board['bottomM'] == move and board['bottomR'] == move) or
            (board['topL'] == move and board['midL'] == move and board['bottomL'] == move) or
            (board['topM'] == move and board['midM'] == move and board['bottomM'] == move) or
            (board['topR'] == move and board['midR'] == move and board['bottomR'] == move))

def computerMove():
    possibleMoves = countValue(board, ' ')[1]
    move = ''

    for letter in ['O', 'X']:
        for posn in possibleMoves:
            boardCopy = board.copy()
            boardCopy[posn] = letter
            if canWin(boardCopy, letter):
                move = posn
                return move

    openCorners = []
    for posn in possibleMoves:
        if posn in ['topL', 'topR', 'bottomL', 'bottomR']:
            openCorners.append(posn)
    
    if len(openCorners) > 0:
        move = selectRandom(openCorners)
        return move
    
    if 'midM' in possibleMoves:
        move = 'midM'
        return move

    openEdges = []
    for posn in possibleMoves:
        if posn in ['topM', 'midL', 'midR', 'bottomM']:
            openEdges.append(posn)
    
    if len(openEdges) > 0:
        move = selectRandom(openEdges)
        
    return move

def insertMove(letter, position):
    board[position] = letter

def selectRandom(open):
    import random
    length = len(open)
    r = random.randrange(0, length)
    return open[r]    

def boardFull():
    return (countValue(board, 'X')[0] + countValue(board, 'O')[0]) == 9

def main():
    player, computer = 'X', 'O'
    print(f'Player is [[{player}]] and Computer is [[{computer}]]')
    printBoard(board)
    
    while not boardFull():
        if not(canWin(board, 'O')):
            move('X')
            printBoard(board)
        else:
            print('Welp, you lost!')
            break
        if not(canWin(board, 'X')):
            moove = computerMove()
            if moove == '':
                print('Game tied!')
            else:
                insertMove('O', moove)
                print('Computer places \'O\' in position', moove)
                printBoard(board)
        else:
            print('You win! Now go waste your time elsewhere.')
            break
    """
    if boardFull():
        print('Tie Game!')
    """


if __name__=="__main__":
    main()