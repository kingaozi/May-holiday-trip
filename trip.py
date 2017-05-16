import os
import sys, tty, termios


def input_width_and_height():

    """Podawanie width oraz height, sprawdzanie czy są liczbami, nastepnie zamiana do int"""

    global width
    global height

    width = 20


    height = 20


    width = int(width)
    height = int(height)

    return width, height

def create_table():

    """Tworzenie tablicy"""
    global board
    board = []
    board.append(list("X") * width)
    for value in range(height - 2):
        board.append(list("X" + " " * (width - 2) + "X"))
    board.append(board[0])
    print(board)
    return board


def print_board():

    """Drukowanie tablicy"""

    print("")
    for i in range(height):
        print(*board[i])

def maupa():
    # global old_x
    # global old_y

    old_x = 5
    old_y = 5
    board[old_x][old_y] = "@"
    #print(board)
    #for i in range(height):
    #    print(*board[i])
    return old_x,old_y

def movement(old_x,old_y,board):
    global new_x
    global new_y

    new_x = old_x
    new_y = old_y

    for i in range(height):
        print(*board[i])


    wsad = getch()
    if wsad =='a':
        if board[old_y][old_y-1] != "X":
            new_y=old_y-1

    if wsad == 'd':
        if board[old_y][old_y+1] != "X": 
            new_y=old_y+1

    if wsad == 'w':
        if board[old_x][old_x-1] != "X":
            new_x=old_x-1

    if wsad == 's':
        if board[old_x][old_x+1] != "X":
            new_x=old_x+1


    if wsad =='q':
        sys.exit()
    board[old_x][old_y] = " "
    board[new_x][new_y] = "@"

    old_x = new_x
    old_y = new_y

    return old_x, old_y



def getch():

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():


    input_width_and_height()
    create_table()
    print_board()
    old_x, old_y = maupa()
    while True:
        os.system('clear')
        old_x, old_y = movement(old_x,old_y,board)



if __name__ == '__main__':
    main()
