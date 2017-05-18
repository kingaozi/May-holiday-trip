import os
import sys, tty, termios
import csv


def open_file(hero_x,hero_y):


    column = []
    mapa = []
    text = open('secondmap.txt').readlines()
    for line in text:
        for char in line:
            column.append(char)
        mapa.append(column)
        column = []

    current_map = mapa

    return mapa, current_map

def open_current_map(hero_x, hero_y, current_map,mapa):

    current_map=mapa

    return current_map


def write_current_map(current_map):
    return


def movement(hero_x,hero_y,current_map, inventory):
    """Function that allows you to move around, not to enter banned signs and change the energy value, 
       and later calls function print(board)"""

    wsad = getch()

    exceptions = ['X', 's', 'w', 'o', '|', '_', 'Y', 'S', 'C', 'B', 'N', '~', 'W', 'Q', '▣']

    if wsad =='a':
        if current_map[hero_x][hero_y-1] not in exceptions:
            hero_y=hero_y-1
            for item in inventory:
                for i in item:
                    if i == "☕":
                        inventory[i] -= 1

    if wsad == 'd':
        if current_map[hero_x][hero_y+1] not in exceptions:
            hero_y=hero_y+1
            for item in inventory:
                for i in item:
                    if i == "☕":
                        inventory[i] -= 1



    if wsad == 'w':
        if current_map[hero_x-1][hero_y] not in exceptions:
            hero_x=hero_x-1
            for item in inventory:
                for i in item:
                    if i == "☕":
                        inventory[i] -= 1

    if wsad == 's':
        if current_map[hero_x+1][hero_y] not in exceptions:
            hero_x=hero_x+1
            for item in inventory:
                for i in item:
                    if i == "☕":
                        inventory[i] -= 1

    if wsad =='q':
        sys.exit()


    print_board_and_hero(current_map,hero_x,hero_y)

    return hero_x, hero_y, current_map, inventory



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

sign_colours = {"s": green, "S": green, "w":orange, "W":orange, "o": blue, "☔": yellow, "☕": lightred,
                "⓵": yellow,"☎": lightgreen, "⁕": pink, "▣": black}

def get_coloured_sign(sign):
    """Function returns coloured sign"""
    if sign in sign_colours:
        return sign_colours[sign] + sign + ENDC

    else:
        return sign

def print_board_and_hero(current_map,hero_x,hero_y):
    """Function prints board with colors and prints hero"""

    os. system("clear")


    for x, row in enumerate(current_map):
        for y, sign in enumerate(row):
            if y == hero_y and  x ==  hero_x:
                print("@", end="")


            else:
                print(('').join(get_coloured_sign(sign)), end="")

def add_to_inventory(inventory, hero_x, hero_y, current_map): 

    """Function adds to the inventory collected items"""

    if current_map[hero_x][hero_y] == "⓵" :
        for item in inventory:
            for i in item:
                if i == "⓵":
                    inventory[i] += +1
                    current_map[hero_x][hero_y] = '.'
    
    if current_map[hero_x][hero_y] == "☕":
        for item in inventory:
            for i in item:
                if i == "☕":
                    inventory[i] += 100
                    current_map[hero_x][hero_y] = '.'

    if current_map[hero_x][hero_y] == "☎":
        for item in inventory:
            for i in item:
                if i == "☎":
                    inventory[i] += 2
                    current_map[hero_x][hero_y] = '.'
    
    if current_map[hero_x][hero_y] == "☔":
        for item in inventory:
            for i in item:
                if i == "☔":
                    inventory[i] += 5
                    current_map[hero_x][hero_y] = '.'

    if current_map[hero_x][hero_y] == "⁕":
        for item in inventory:
            for i in item:
                if i == "⁕":
                    inventory[i] += 5
                    current_map[hero_x][hero_y] = '.'

    return inventory, current_map

         

def print_table(inventory): #displays inventory in a well-organized table
        

    print("Inventory: ")
              
    longest_word = max(inventory, key=lambda word: (len(word), word)) 
                                                                    
    lenght_of_word = len(longest_word) 


    print('{:>7} {:>{width}}'.format("count", "item name" , width=lenght_of_word))                                            
    print('-' * (lenght_of_word + 8)) 

    for item in inventory:
        print('{:>7} {:>{width}}'.format(inventory[item], item , width=lenght_of_word))


def main():

    hero_x=10
    hero_y=10
    inventory = {"☕": 100, "☔":0, "⓵":0, "☎":0, "⁕":0 }
    mapa, current_map = open_file(hero_x,hero_y)
    mapa_copy = mapa[:]

    while True:

        current_mapa = open_file(hero_x,hero_y)
        os.system('clear')
        print_board_and_hero(current_map,hero_x,hero_y)
        add_to_inventory(inventory, hero_x, hero_y, current_map)
        print_table(inventory)
        hero_x, hero_y, current_map, inventory = movement(hero_x,hero_y, current_map, inventory)
        old_map=mapa
        current_mapa = open_current_map(hero_x, hero_y,current_map,mapa)


if __name__ == '__main__':
    main()