# Created on Thu May 16 2024
# Copyright (c) 2024 BP Feral
# Python 3.12.1

import pygame, sys, time
# ===================================================================

from classes.button import MenuButton
from classes.inputBox import inputBox
# ===================================================================

counter = 0
FIRST_GEN = 500

class GAChess:
    def __init__(self, n):
        self.board = self.createBoard(n)
        self.solutions = []
        self.size = n
        self.env = []
        self.goal = None
        self.goalIndex = -1

    def createBoard(self, n):
        board = [[0 for i in range(n)] for j in range(n)]
        return board

    def setBoard(self, board, gen):
        for i in range(self.size):
            board[gen[i]][i] = 1

    def generateDNA(self):
        from random import shuffle
        DNA = list(range(self.size))
        shuffle(DNA)
        while DNA in self.env:
            shuffle(DNA)
        return DNA

    def initializeFirstGeneration(self, val):
        for i in range(val):
            self.env.append(self.generateDNA())

    def utilityFunction(self, gen):
        hits = 0
        board = self.createBoard(self.size)
        self.setBoard(board, gen)
        col = 0

        for dna in gen:
            try:
                for i in range(col-1, -1, -1):
                    if board[dna][i] == 1:
                        hits += 1
            except IndexError:
                quit()
            for i, j in zip(range(dna-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 1:
                    hits += 1
            for i, j in zip(range(dna+1, self.size, 1), range(col-1, -1, -1)):
                if board[i][j] == 1:
                    hits += 1
            col += 1
        return hits

    def isSolution(self, gen):
        if self.utilityFunction(gen) == 0:
            return True
        return False

    def crossover(self, firstGen, secondGen):
        for i in range(1, len(firstGen)):
            if abs(firstGen[i-1] - firstGen[i]) < 2:
                firstGen[i], secondGen[i] = secondGen[i], firstGen[i]
            if abs(secondGen[i-1] - secondGen[i]) < 2:
                firstGen[i], secondGen[i] = secondGen[i], firstGen[i]

    def mutation(self, gen):
        bound = self.size // 2
        from random import randint as rand
        leftSideIndex = rand(0, bound)
        RightSideIndex = rand(bound+1, self.size-1)
        newGen = []
        for dna in gen:
            if dna not in newGen:
                newGen.append(dna)
        for i in range(self.size):
            if i not in newGen:
                newGen.append(i)

        gen = newGen
        gen[leftSideIndex], gen[RightSideIndex] = gen[RightSideIndex], gen[leftSideIndex]
        return gen

    def reproduce(self):
        for i in range(1, len(self.env), 2):
            firstGen = self.env[i-1][:]
            secondGen = self.env[i][:]
            self.crossover(firstGen, secondGen)
            firstGen = self.mutation(firstGen)
            secondGen = self.mutation(secondGen)
            self.env.append(firstGen)
            self.env.append(secondGen)

    def makeSelection(self):
        genUtilities = []
        newEnv = []

        for gen in self.env:
            genUtilities.append(self.utilityFunction(gen))
            if min(genUtilities) == 0:
                self.goalIndex = genUtilities.index(min(genUtilities))
                self.goal = self.env[self.goalIndex]
                return self.env
        minUtil = None
        while len(newEnv) < self.size:
            minUtil = min(genUtilities)
            minIndex = genUtilities.index(minUtil)
            newEnv.append(self.env[minIndex])
            genUtilities.remove(minUtil)
            self.env.remove(self.env[minIndex])

        return newEnv

    def solveGA(self):
        self.initializeFirstGeneration(FIRST_GEN)
        count = 0
        while True:
            self.reproduce()
            self.env = self.makeSelection()

            count += 1
            if self.goalIndex >= 0:
                try:
                    print(count)
                    return self.goal
                except IndexError:
                    print(self.goalIndex)
            else:
                continue

def Genetic(screen, execution_times, clock):
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
                        if tile_count == 1 or tile_count == 2 or tile_count == 3 or tile_count == 4 or tile_count == 5:
                            started = True
                            NoSolution = True
                            break

                        chess = GAChess(tile_count)
                        solution = chess.solveGA()
                        for indexY, valY in enumerate(solution):
                            table.blit(queen_surf, (indexY * tile_size + tile_count, valY * tile_size + tile_count))

                        started = True
                    execution_time = time.time() - start_time
                    execution_times[3] = execution_time
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