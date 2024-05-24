# Created on Thu May 16 2024
# Copyright (c) 2024 BP Feral
# Python 3.12.1

import pygame, sys, time, random
# ===================================================================

from classes.button import MenuButton
from classes.inputBox import inputBox
# ===================================================================

def calculateObjective(board, state, N):
    attacking = 0
    for i in range(N):
        row = state[i]
        col = i - 1
        while (col >= 0 and board[row][col] != 1):
            col -= 1

        if (col >= 0 and board[row][col] == 1):
            attacking += 1

        row = state[i]
        col = i + 1
        while (col < N and board[row][col] != 1):
            col += 1

        if (col < N and board[row][col] == 1):
            attacking += 1

        row = state[i] - 1
        col = i - 1
        while (col >= 0 and row >= 0 and board[row][col] != 1):
            col -= 1
            row -= 1

        if (col >= 0 and row >= 0 and board[row][col] == 1):
            attacking += 1

        row = state[i] + 1
        col = i + 1
        while (col < N and row < N and board[row][col] != 1):
            col += 1
            row += 1

        if (col < N and row < N and board[row][col] == 1):
            attacking += 1

        row = state[i] + 1
        col = i - 1
        while (col >= 0 and row < N and board[row][col] != 1):
            col -= 1
            row += 1

        if (col >= 0 and row < N and board[row][col] == 1):
            attacking += 1

        row = state[i] - 1
        col = i + 1
        while (col < N and row >= 0 and board[row][col] != 1):
            col += 1
            row -= 1

        if (col < N and row >= 0 and board[row][col] == 1):
            attacking += 1

    return int(attacking / 2)

def compareStates(state1, state2, N):
    for i in range(N):
        if (state1[i] != state2[i]):
            return False

    return True

def getNeighbour(board, state, N):
    opBoard = [[0 for _ in range(N)] for _ in range(N)]
    opState = [0 for _ in range(N)]

    copyState(opState, state, N)
    generateBoard(opBoard, opState, N)

    opObjective = calculateObjective(opBoard, opState, N)
    NeighbourBoard = [[0 for _ in range(N)] for _ in range(N)]

    NeighbourState = [0 for _ in range(N)]
    copyState(NeighbourState, state, N)
    generateBoard(NeighbourBoard, NeighbourState, N)
    for i in range(N):
        for j in range(N):

            if (j != state[i]):

                NeighbourState[i] = j
                NeighbourBoard[NeighbourState[i]][i] = 1
                NeighbourBoard[state[i]][i] = 0
                temp = calculateObjective(NeighbourBoard, NeighbourState, N)
                if (temp <= opObjective):
                    opObjective = temp
                    copyState(opState, NeighbourState, N)
                    generateBoard(opBoard, opState, N)

                NeighbourBoard[NeighbourState[i]][i] = 0
                NeighbourState[i] = state[i]
                NeighbourBoard[state[i]][i] = 1
    copyState(state, opState, N)
    fill(board, 0, N)
    generateBoard(board, state, N)

def fill(board, value, N):
    for i in range(N):
        for j in range(N):
            board[i][j] = value

def generateBoard(board, state, N):
    fill(board, 0, N)
    for i in range(N):
        board[state[i]][i] = 1

def copyState(state1, state2, N):
    for i in range(N):
        state1[i] = state2[i]

def printBoard(board, N):
    table = []
    for i in range(N):
        row = [*board[i]]
        table.append(row)
    return table

def hillClimbing(board, state, N):
    neighbourBoard = [[0 for _ in range(N)] for _ in range(N)]
    neighbourState = [0 for _ in range(N)]

    copyState(neighbourState, state, N)
    generateBoard(neighbourBoard, neighbourState, N)

    while True:

        copyState(state, neighbourState, N)
        generateBoard(board, state, N)

        getNeighbour(neighbourBoard, neighbourState, N)

        if (compareStates(state, neighbourState, N)):

            return printBoard(board, N)

        elif (calculateObjective(board, state, N) == calculateObjective(neighbourBoard, neighbourState, N)):

            neighbourState[random.randint(0, 100000) % N] = random.randint(0, 100000) % N
            generateBoard(neighbourBoard, neighbourState, N)

def configureRandomly(board, state, N):
    for i in range(N):

        state[i] = random.randint(0, 100000) % N
        board[state[i]][i] = 1

def ProblemaRegineAlp(table_sizes):
    solving_times = []
    for i in range(len(table_sizes)):
        n = table_sizes[i]
        state = [0] * n
        board = [[0 for i in range(n)] for j in range(n)]
        configureRandomly(board, state, n)
        timp = time.time()
        time.sleep(1)
        hillClimbing(board, state, n)
        print(time.time() - timp - 1)
        solving_times.append(time.time() - timp - 1)
        matrice = [["." for _ in range(n)] for i in range(n)]

def Alpinist(screen, execution_times, clock):
    font = pygame.font.Font(None, 42)

    backButton = MenuButton(50, 720-50, 15*len('< Back'), font, '< Back', (128, 145, 71), 0)
    size_text = font.render('size: ', True, (255, 255, 255))
    inputBox1 = inputBox(screen, 280 + 15*len('< Back'), 720-50, 70, font)
    startButton = MenuButton(1080 - 20*len('Start >'), 720-50, 15*len('Start >'), font, 'Start >', (128, 145, 71), 0)
    NoSolution = False
    solText = font.render('No Solution', True, (255, 0, 0))
    queen_surf = None
    table = None
    max_tiles = 25
    tile_size = 20
    tile_count = 0
    table_pos = (300, 100)
    started = False

    running = True
    while running:

        screen.fill((0, 0, 0))

        if started:
            table = pygame.transform.scale(table, (500, 500))
            screen.blit(table, (table_pos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                inputBox1.update(event)
            if backButton.update(event):
                running = False
                return

            if startButton.update(event):
                try:
                    start_time = time.time()
                    tile_count = int(inputBox1.get_content())

                    if 0 < tile_count <= max_tiles:
                        queen_surf = pygame.Surface((tile_size, tile_size))
                        queen_surf.fill((0, 255, 0))
                        table = pygame.Surface((tile_count * tile_size + tile_count, tile_count * tile_size + tile_count))

                        for row in range(tile_count):
                            for x in range(tile_count):
                                if (x + row) % 2:
                                    color = (160, 110, 70)
                                else:
                                    color = (100, 70, 50)

                                pygame.draw.rect(table, color, ((x * tile_size + tile_count), (row * tile_size + tile_count), tile_size, tile_size))
                        NoSolution = False
                        if tile_count == 2 or tile_count == 3:
                            NoSolution = True
                            started = True

                            break
                        state = [0] * tile_count
                        board = [[0 for _ in range(tile_count)] for _ in range(tile_count)]

                        configureRandomly(board, state, tile_count)
                        tableX = hillClimbing(board, state, tile_count)

                        for ind, _x in enumerate(tableX):
                            for indd, item in enumerate(_x):
                                if item == 1:
                                    table.blit(queen_surf, (ind * tile_size + tile_count, indd * tile_size + tile_count))
                            pass

                        started = True
                    execution_time = time.time() - start_time
                    execution_times[1] = execution_time
                except:
                    pass
        if NoSolution:
            screen.blit(solText, (1080//2 - 100, 720//2))

        backButton.draw(screen)
        screen.blit(size_text, (300, 720-50))
        inputBox1.draw()
        startButton.draw(screen)

        clock.tick(60)
        pygame.display.update()