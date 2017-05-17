import os
import sys, tty, termios
import csv


def open_file(old_x, old_y):


    column = []
    mapa=[]
    text = open('firstmap.txt').readlines()
    for line in text:
       for char in line:
           column.append(char)
       mapa.append(column)
       column = []
    mapa[old_x][old_y] = "@"

    #print(mapa)
    return mapa


def movement(old_x,old_y,mapa):



    wsad = getch()
    exceptions = ['X', 's', 'w', 'o', '|', '_', 'F', 'Y', 'S', 'C', 'B', 'N', '~', 'W', 'Q']
    if wsad =='a':
        if mapa[old_x][old_y-1] not in exceptions:
            old_y=old_y-1

    if wsad == 'd':
        if mapa[old_x][old_y+1] not in exceptions:
            old_y=old_y+1

    if wsad == 'w':
        if mapa[old_x-1][old_y] not in exceptions:
            old_x=old_x-1

    if wsad == 's':
        if mapa[old_x+1][old_y] not in exceptions:
            old_x=old_x+1

    if wsad =='q':
        sys.exit()

    mapa[old_x][old_y] = "@"
    print(mapa[old_x][old_y])
    os.system('clear')
    print_board(mapa)


    return old_x, old_y, mapa



def getch():

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'

sign_colours = {"F": cyan, "s": green, "S": green, "w":orange, "W":orange, "o": darkgrey, "☔": yellow, "_": red, "|": red, "☕": lightred}
def get_coloured_sign(sign):
    if sign in sign_colours:
        return sign_colours[sign] + sign + ENDC

    else:
        return sign

def print_board(mapa):
   """Prints board."""
   os. system("clear")
   for row in mapa:
       for sign in row:
           print(('').join(get_coloured_sign(sign)), end="")

def add_to_inventory(inventory, added_items): # Adds to the inventory dictionary a list

    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def print_table(inventory): #displays inventory in a well-organized table


    print("Inventory: ")

    #sorted_words = sorted(inventory, key=len)
    #longest_word = sorted_words[-1]                    #Find the maximum value of the all words lengths
    longest_word2 = max(inventory, key=lambda word: (len(word), word)) #lambda function is a way to create small anonymous functions,
                                                                        #i.e. functions without a name
    longest_word = len(longest_word2) #Show the length of the longest word


    print('{:>7} {:>{width}}'.format("count", "item name" , width=longest_word)) #">" Align to the right
                                                        #{:>7} - Take the last 7 seats from the right for "count"
                                                    #later - space, width - The number of letters of the longest word for "item name"
    print('-' * (longest_word + 8)) #Print "-" as many times as the length of the longest word plus 8
                                    # 8 = {:>7} + 1 (space)


    for item in inventory:
        print('{:>7} {:>{width}}'.format(inventory[item], item , width=longest_word))


def main():
    old_x=10
    old_y=10
    inventory = {"coffee": 0, "umbrella":0, }
    added_items = []
    mapa = open_file(old_x, old_y)



    while True:
        #os.system('clear')
        print_board(mapa)
        inventory = add_to_inventory(inventory, added_items)
        print_table(inventory)
        old_x, old_y, mapa = movement(old_x,old_y,mapa)
        mapa = open_file(old_x, old_y)


if __name__ == '__main__':
    main()
