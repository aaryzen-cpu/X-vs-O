def sum(a,b,c):
    return a + b + c

def printBoard(xState, yState):

    board = []

    for i in range(9):
        value = 'X' if xState[i] else ('O' if yState[i] else i)
        board.append(value)

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def checkWin(xState, yState):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]] 
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match..")
            return 1
        if(sum(yState[win[0]], yState[win[1]], yState[win[2]]) == 3):
            print("O Won the match..")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0]
    yState = [0,0,0,0,0,0,0,0,0]

    turn = 1   # 1 for X, 0 for O

    print("Welcome to Tic Tac Toe")

    while True:

        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1

        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            yState[value] = 1

        printBoard(xState, yState)

        cwin = checkWin(xState,yState)
        if(cwin != -1):
            print("Match Over")
            break

        turn = 1 - turn