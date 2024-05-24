# Created on Thu May 16 2024
# Copyright (c) 2024 BP Feral
# Python 3.12.1

# ===================================================================
import sys, pygame
# ===================================================================

from classes.button import MenuButton
from scenes.scene0 import Backtracking
from scenes.scene1 import Alpinist
from scenes.scene2 import Calire
from scenes.scene3 import Genetic
from scenes.info import loop
from scenes.time import showTime
# ===================================================================

pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('Aplicatie IA')
clock = pygame.time.Clock()
# Fonts
pygame.font.init()
font = pygame.font.Font(None, 42)

buttons = []
options = ['a. N Regine [backtracking]', 'b. N Regine [alpinist]', 'c. N Regine [calire]', 'd. N regine Genetic']
for i, option in enumerate(options):
    buttons.append(MenuButton(380, 100 + i * 50, 15*len(option), font, option, (125, 128, 116), i))

exitButton = MenuButton(400, 720-100, 100, font, "EXIT", (117, 36, 47), 0)
infoButton = MenuButton(400, 720-300, 100, font, "INFO", (125, 128, 116), 0)
showTimes = MenuButton(400, 720-350, 150, font, "Show Time", (125, 128, 116), 0)

execution_times = [0, 0, 0, 0]

running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if exitButton.update(event):
            pygame.quit()
            sys.exit()

        if infoButton.update(event):
            loop(screen, clock)

        if showTimes.update(event):
            showTime(screen, execution_times, clock)

        for button in buttons:
            if button.update(event):
                if button.index == 0:
                    Backtracking(screen, execution_times, clock)
                if button.index == 1:
                    Alpinist(screen, execution_times, clock)
                if button.index == 2:
                    Calire(screen, execution_times, clock)
                if button.index == 3:
                    Genetic(screen, execution_times, clock)

    for button in buttons:
        button.draw(screen)

    exitButton.draw(screen)
    infoButton.draw(screen)
    showTimes.draw(screen)

    clock.tick(60)
    pygame.display.update()

# ===================================================================
# NOTE
# python -m venv env
# 3131b Pricob Mihai
# NO CONFIG FILES
# ERROR: Activate.ps1 cannot be loaded because running scripts is disabled on this system. 
# -> run `Set-ExecutionPolicy RemoteSigned`

# ===================================================================
# TODO
# .\env\Scripts\activate
# pip install -r .\requirements.txt