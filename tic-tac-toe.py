from lookup import moveMap
from os import name, system
def cls():
    system("cls" if name == "nt" else "clear")
def display(board):
    print()
    print(f"   {board[0]} | {board[1]} | {board[2]}")
    print(f"  ---+---+---")
    print(f"   {board[3]} | {board[4]} | {board[5]}")
    print(f"  ---+---+---")
    print(f"   {board[6]} | {board[7]} | {board[8]}")
    print()
inp = input("Do you want to play first (Y/N)? ")
while not inp in "yYnN":
    inp = input("Do you want to play first (Y/N)? ")
playerFirst = inp in "yY"
board = "         " if playerFirst else "X        "
while moveMap[board] in moveMap:
    cls()
    display(board)
    move = int(input(" Next move (1->9):\n  1 2 3\n  4 5 6\n  7 8 9\n Enter your next move: "))
    while (board[move - 1] != ' '):
        move = int(input())
    board = board[:(move - 1)] + "OX"[playerFirst] + board[move:]
    if moveMap[board] in moveMap:
        board = moveMap[board]
cls()
print(' ' + moveMap[board], "The final board: ")
display(board)
