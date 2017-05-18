def movement(hero_x,hero_y,mapa):



    wsad = getch()
    kill = ['z','Z']
    exceptions = ['X', 's', 'w', 'o', '|', '_', 'F', 'Y', 'S', 'C', 'B', 'N', '~', 'W', 'Q']
    if wsad =='a':
        if mapa[hero_x][hero_y-1] not in kill:
            if mapa[hero_x][hero_y-1] not in exceptions:
                hero_y=hero_y-1
        elif dead = open('game_over.txt').readlines()

    if wsad == 'd':
        if mapa[hero_x][hero_y+1] not in kill:
            if mapa[hero_x][hero_y+1] not in exceptions:
                hero_y=hero_y+1
        elif dead = open('game_over.txt').readlines()

    if wsad == 'w':
        if mapa[hero_x-1][hero_y] not in kill:
            if mapa[hero_x-1][hero_y] not in exceptions:
                hero_x=hero_x-1
        elif dead = open('game_over.txt').readlines()

    if wsad == 's':
        if mapa[hero_x+1][hero_y] not in kill:
            if mapa[hero_x+1][hero_y] not in exceptions:
                hero_x=hero_x+1
        elif dead = open('game_over.txt').readlines()

    if wsad =='q':
        enter=open('poczatek.txt').readlines()
        sys.exit()



    return hero_x, hero_y, mapa