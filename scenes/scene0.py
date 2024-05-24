# Created on Thu May 16 2024
# Copyright (c) 2024 BP Feral
# Python 3.12.1

import pygame, sys, time
# ===================================================================

from classes.button import MenuButton
from classes.inputBox import inputBox
# ===================================================================

def solve_queens(n):
    def is_valid(queens, col):
        for row in range(len(queens)):
            if abs(queens[row] - col) in (0, abs(row - len(queens))):
                return False
        return True

    def backtrack(queens, row):
        if row == n:
            return queens
        for col in range(n):
            if is_valid(queens, col):
                queens.append(col)
                if row == n - 1:
                    with open("output.txt", "w") as file:
                        for i in range(n):
                            file.write(f"{i} {queens[i]}\n")
                    return queens
                solution = backtrack(queens, row + 1)
                if solution:
                    return solution
                queens.pop()
        return None

    return backtrack([], 0)

def Backtracking(screen, execution_times, clock):
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
                    tile_count = int(inputBox1.get_content())
                    start_time = time.time()
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

                                solution = solve_queens(tile_count)
                                try:
                                    NoSolution = False
                                    for _ in solution:
                                        table.blit(queen_surf, (_ * tile_size + tile_count, solution[_] * tile_size + tile_count))
                                except:
                                    NoSolution = True
                                    pass
                        started = True
                    execution_time = time.time() - start_time
                    execution_times[0] = execution_time
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