from colorama import Fore, Style, init

init()

def lineSum(a, b, c):
    return a + b + c


def printBoard(xState, yState):

    board = []

    for i in range(9):

        if xState[i]:
            board.append(Fore.RED + "X" + Style.RESET_ALL)
        elif yState[i]:
            board.append(Fore.BLUE + "O" + Style.RESET_ALL)
        else:
            board.append(str(i))

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def checkWin(xState, yState):
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for win in wins:

        if lineSum(
            xState[win[0]],
            xState[win[1]],
            xState[win[2]]
        ) == 3:
            print(Fore.GREEN + "X Wins!" + Style.RESET_ALL)
            return 1

        if lineSum(
            yState[win[0]],
            yState[win[1]],
            yState[win[2]]
        ) == 3:
            print(Fore.GREEN + "O Wins!" + Style.RESET_ALL)
            return 0

    return -1


if __name__ == "__main__":

    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    turn = 1

    print("Welcome to Tic Tac Toe")
    printBoard(xState, yState)

    moves = 0

    while True:

        if turn == 1:
            print(Fore.RED + "X's Chance" + Style.RESET_ALL)
        else:
            print(Fore.BLUE + "O's Chance" + Style.RESET_ALL)

        try:
            value = int(input("Please enter a value (0-8): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if value < 0 or value > 8:
            print("Please enter a number between 0 and 8!")
            continue

        if xState[value] == 1 or yState[value] == 1:
            print("That square is already occupied!")
            continue

        if turn == 1:
            xState[value] = 1
        else:
            yState[value] = 1

        moves += 1

        printBoard(xState, yState)

        cwin = checkWin(xState, yState)

        if cwin != -1:
            print("Match Over")
            break

        if moves == 9:
            print(Fore.YELLOW + "It's a Draw!" + Style.RESET_ALL)
            break

        turn = 1 - turn