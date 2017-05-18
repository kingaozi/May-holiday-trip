import os
import sys, tty, termios
import csv

def menu():
    column = []
    mapa = []
    yn = getch()
    loop = True
    text = open('menu.txt').readlines()
    for line in text:
        for char in line:
            column.append(char)
        mapa.append(column)
        column = []
    current_map = mapa


    return mapa, current_map


def open_file_first_map(hero_x,hero_y):


    column = []
    mapa = []
    text = open('firstmap.txt').readlines()
    for line in text:
        for char in line:
            column.append(char)
        mapa.append(column)
        column = []

    mapa[hero_x][hero_y] = "@"
    current_map = mapa

    return mapa, current_map

def open_current_map(hero_x, hero_y, current_map):

    column = []
    mapa = []
    text = open('current_map.txt').readlines()
    for line in text:
        for char in line:
            column.append(char)
        mapa.append(column)
        column = []

    #current_map[hero_x][hero_y] = "@"

    return current_map
def open_game_over_map(hero_x, hero_y, game_over_map):
    column = []
    mapa = []
    text = open('game_over.txt').readlines()
    for line in text:
        for char in line:
            column.append(char)
        mapa.append(column)
        column = []

    mapa[hero_x][hero_y] = "@"
    game_over_map = mapa

    return mapa, game_over_map
def poczatek_map(hero_x, hero_y, poczatek):
     column = []
    mapa = []
    text = open('game_over.txt').readlines()
    for line in text:
        for char in line:
            column.append(char)
        mapa.append(column)
        column = []

    mapa[hero_x][hero_y] = "@"
    poczatek = mapa

    return mapa, poczatek_map
    

def write_current_map(current_map):
    #current_map = open("current_map.txt", "w")
    for i in current_map:
        current_map.write(current_map)
    current_map.close()

    current_map = open("current_map.txt", "r")
    current_map.close()


def movement(hero_x,hero_y,current_map):

    #current_map[hero_x][hero_y] = "@"

    open_current_map(hero_x,hero_y,current_map)

    print(hero_x,hero_y)
    wsad = getch()
    exceptions = ['X', 's', 'w', 'o', '|', '_', 'Y', 'S', 'C', 'B', 'N', '~', 'W', 'Q']
    if wsad =='a':
        if current_map[hero_x][hero_y-1] not in exceptions:
            hero_y=hero_y-1

    if wsad == 'd':
        if current_map[hero_x][hero_y+1] not in exceptions:
            hero_y=hero_y+1


    if wsad == 'w':
        if current_map[hero_x-1][hero_y] not in exceptions:
            hero_x=hero_x-1

    if wsad == 's':
        if current_map[hero_x+1][hero_y] not in exceptions:
            hero_x=hero_x+1

    if wsad =='q':
        sys.exit()

    print_board(current_map,hero_x,hero_y)

    write_current_map(current_map)


    return hero_x, hero_y, current_map



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

def print_board(current_map,hero_x,hero_y):
    """Prints board."""
    #os. system("clear")

    #current_map[hero_x][hero_y] = "@"

    for row in current_map:
        for sign in row:
            print(('').join(get_coloured_sign(sign)), end="")

def add_to_inventory(inventory, hero_x, hero_y, mapa_copy, mapa): # Adds to the inventory dictionary a list



    if mapa_copy[hero_x][hero_y] == "G":
        for item in inventory:
            for i in item:
                if i == "G":
                    inventory[i] += +1
                    mapa[hero_x][hero_y] = '.'
                    print("OK")
                    print(mapa[hero_x][hero_y])


    return inventory, mapa

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

    found_items = ['G', 'F']
    hero_x=10
    hero_y=10
    inventory = {"coffee": 0, "umbrella":0, "G":0, "F": 0 }
    mapa, current_map = open_file_first_map(hero_x,hero_y)
    game_over_map = open_game_over_map(hero_x,hero_y)
    poczatek = poczate_map(hero_x,hero_y)
    menu_map = open
    mapa_copy = mapa[:]

    while True:

        mapa = open_file(hero_x,hero_y)

        os.system('clear')
        print_board(current_map,hero_x,hero_y)
        add_to_inventory(inventory, hero_x, hero_y, mapa_copy, mapa)
        print_table(inventory)
        hero_x, hero_y, mapa = movement(hero_x,hero_y, current_map)
        old_map=mapa
        #mapa = open_file(hero_x, hero_y)


if __name__ == '__main__':
    main()