# Created on Thu May 16 2024
# Copyright (c) 2024 BP Feral
# Python 3.12.1

import random, time, pygame, sys
# ===================================================================

from classes.button import MenuButton
from classes.inputBox import inputBox
from copy import deepcopy
from math import exp
# ===================================================================

TEMPERATURE = 4000

def ProblemaRegineCS(table_sizes):
    solving_times = []
    for i in range(len(table_sizes)):
        n = table_sizes[i]
        timp = time.time()
        time.sleep(1)
        simulated_annealing(n)
        print(time.time() - timp - 1)
        solving_times.append(time.time() - timp - 1)
    return solving_times

def threat_calculate(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    return (n - 1) * n / 2

def create_board(n):
    chess_board = {}
    temp = list(range(n))
    random.shuffle(temp)
    column = 0

    while len(temp) > 0:
        row = random.choice(temp)
        chess_board[column] = row
        temp.remove(row)
        column += 1
    del temp
    return chess_board

def cost(chess_board):
    threat = 0
    m_chessboard = {}
    a_chessboard = {}

    for column in chess_board:
        temp_m = column - chess_board[column]
        temp_a = column + chess_board[column]
        if temp_m not in m_chessboard:
            m_chessboard[temp_m] = 1
        else:
            m_chessboard[temp_m] += 1
        if temp_a not in a_chessboard:
            a_chessboard[temp_a] = 1
        else:
            a_chessboard[temp_a] += 1

    for i in m_chessboard:
        threat += threat_calculate(m_chessboard[i])
    del m_chessboard

    for i in a_chessboard:
        threat += threat_calculate(a_chessboard[i])
    del a_chessboard

    return threat

def print_chess_board(board):
    values = []
    for column, row in board.items():
        el = [column, row]
        values.append(el)
    return values

def simulated_annealing(n):
    solution_found = False
    answer = create_board(n)

    cost_answer = cost(answer)

    t = TEMPERATURE
    sch = 0.99

    while t > 0:
        t *= sch
        successor = deepcopy(answer)
        while True:
            index_1 = random.randrange(0, n - 1)
            index_2 = random.randrange(0, n - 1)
            if index_1 != index_2:
                break

        successor[index_1], successor[index_2] = successor[index_2], successor[index_1]
        delta = cost(successor) - cost_answer

        if delta < 0 or random.uniform(0, 1) < exp(-delta / t):
            answer = deepcopy(successor)
            cost_answer = cost(answer)

        if cost_answer == 0:
            solution_found = True
            return print_chess_board(answer)

    if solution_found is False:
        return [[-100, -100]]

def Calire(screen, execution_times, clock):
    font = pygame.font.Font(None, 42)
    
    backButton = MenuButton(50, 720-50, 15 * len('< Back'), font, '< Back', (128, 145, 71), 0)
    size_text = font.render('size: ', True, (255, 255, 255))
    inputBox1 = inputBox(screen, 280 + 15 * len('< Back'), 720-50, 70, font)
    startButton = MenuButton(1080 - 20 * len('Start >'), 720-50, 15 * len('Start >'), font, 'Start >', (128, 145, 71), 0)
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
                            for _ in range(tile_count):
                                if (_ + row) % 2:
                                    color = (160, 110, 70)
                                else:
                                    color = (100, 70, 50)

                                pygame.draw.rect(table, color, (

                                    (_ * tile_size + tile_count), 
                                    (row * tile_size + tile_count),

                                tile_size, tile_size))
                        NoSolution = False
                        if tile_count == 1 or tile_count == 2 or tile_count == 3 or tile_count == 4:
                            NoSolution = True
                            started = True
                            break

                        values = simulated_annealing(tile_count)
                        for pair in values:
                            table.blit(queen_surf, (pair[0] * tile_size + tile_count, pair[1] * tile_size + tile_count))

                        started = True
                    execution_time = time.time() - start_time
                    execution_times[2] = execution_time
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