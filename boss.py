import os
import sys, tty, termios
import csv
import hot_cold


def first_level(hero_x,hero_y):


    column = []
    mapa = []
    text = open('firstmap.txt').readlines()
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


def second_level(current_map,hero_x,hero_y):
    if current_map[hero_x][hero_y] == "2":
        column = []
        mapa = []
        text = open("secondmap.txt").readlines()
        for line in text:
           for char in line:
               column.append(char)
           mapa.append(column)
           column = []
        hero_x = 15
        hero_y = 2
        current_map = mapa
    return current_map, hero_x, hero_y


def third_level(current_map,hero_x,hero_y):
    if current_map[hero_x][hero_y] == "3":
        column = []
        mapa = []
        text = open("thirdmap.txt").readlines()
        for line in text:
            for char in line:
                column.append(char)
            mapa.append(column)
            column = []
        hero_x = 22
        hero_y = 2

        current_map = mapa
    return current_map, hero_x, hero_y


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
                "⓵": yellow,"☎": lightgreen, "⁕": pink, "▣": black, "~": blue}

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

def open_gate(hero_x, hero_y, current_map):
    if current_map[hero_x][hero_y] == "Z":
        for x, row in enumerate(current_map):
            for y, sign in enumerate(row):
                if current_map[x][y] == "Q":
           
                    current_map[x][y] ="."
        return current_map

def game_over(current_map):
    
    column = []
    mapa = []
    text = open('Game_Over.txt').readlines()
    for line in text:
        for char in line:
            column.append(char)
        mapa.append(column)
        column = []
    current_map = mapa
    ans = ['y','Y','N','n']
    yn = getch()
    loop = True

    return current_map

def boss(current_map):
    column = []
    mapa = []
    text = open("bosss.txt").readlines()
    for line in text:
        for char in line:
            column.append(char)
        mapa.append(column)
        column = []
  
    current_map = mapa
    return current_map


def play_again():
    play_again = input("\nDo you want to ply again ?: Y/N").lower()
    play = 0
    if play_again == 'y':
        os.system("clear")
    else:
        sys.exit()


def main():
    while True:
        hero_x=10
        hero_y=10
        inventory = {"☕": 100, "☔":0, "⓵":0, "☎":0, "⁕":0 }
        mapa, current_map = first_level(hero_x,hero_y)

        while True:
            #os.system('clear')
            current_map, hero_x, hero_y = second_level(current_map, hero_x,hero_y)
            current_map, hero_x, hero_y = third_level(current_map,hero_x,hero_y)
            print_board_and_hero(current_map,hero_x,hero_y)
            open_gate(hero_x, hero_y, current_map)
            add_to_inventory(inventory, hero_x, hero_y, current_map)
            print_table(inventory)
            hero_x, hero_y, current_map, inventory = movement(hero_x,hero_y, current_map, inventory)
            #boss(inventory)
            print(inventory)
            if inventory["☕"] == 0:
                current_map =game_over(current_map)
                print_board_and_hero(current_map,hero_x,hero_y)
                break            

            if inventory["⓵"] == 30:
                os.system('clear')
                current_map = boss(current_map)
                print_board_and_hero(current_map,hero_x,hero_y)
                hot_cold.main()
        play_again() 


if __name__ == '__main__':
    main()
