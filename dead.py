def movement(hero_x,hero_y,mapa):



    wsad = getch()
    kill = ['z','Z']
    exceptions = ['X', 's', 'w', 'o', '|', '_', 'F', 'Y', 'S', 'C', 'B', 'N', '~', 'W', 'Q']
    if wsad =='a':
        if mapa[hero_x][hero_y-1] not in kill:
            if mapa[hero_x][hero_y-1] not in exceptions:
                hero_y=hero_y-1
        elif:
             game_over()

    if wsad == 'd':
        if mapa[hero_x][hero_y+1] not in kill:
            if mapa[hero_x][hero_y+1] not in exceptions:
                hero_y=hero_y+1
        elif:
             game_over()

    if wsad == 'w':
        if mapa[hero_x-1][hero_y] not in kill:
            if mapa[hero_x-1][hero_y] not in exceptions:
                hero_x=hero_x-1
        elif:
             game_over()

    if wsad == 's':
        if mapa[hero_x+1][hero_y] not in kill:
            if mapa[hero_x+1][hero_y] not in exceptions:
                hero_x=hero_x+1
        elif:
             game_over()
             again()

    if wsad =='q':
        menu()



    return hero_x, hero_y, mapa


def game_over():

    column = []
    mapa = []
    text = open('game_over.txt').readlines()
    for line in text:
        for char in line:
            column.append(char)
        mapa.append(column)
        column = []
    ans = ['y','Y','N','n']
    yn = getch()
    loop = True
    while loop:
        if yn in ans:
            if yn == 'Y':
                loop = False
                main()
            elif: 
                sys.exit():
        elif:
            return yn