# Created on Thu May 16 2024
# Copyright (c) 2024 BP Feral
# Python 3.12.1

import pygame, sys
# ===================================================================

from classes.button import MenuButton
# ===================================================================

def loop(screen, clock):
    font = pygame.font.Font(None, 42)
    text = ['Numele echipei: ???', 'Membrii:', ' -> Pricob Mihai Alexandru', ' -> Sandru Alexandru', ' -> Ghilescu Dumitru', 'Semi-grupa: 3131B']
    fonts = []
    for i, item in enumerate(text):
        fonts.append(font.render(item, True, (150, 20, 50+  i * 20)))

    backButton = MenuButton(50, 720-50, 15 * len('< Back'), font, '< Back', (69, 69, 69), 0)

    running = True
    while running:

        screen.fill((0, 0, 0))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if backButton.update(event):
                running = False
                return

        backButton.draw(screen)
        for i, item in enumerate(fonts):
            screen.blit(item, (100, 200 +  i * 50))
        clock.tick(60)
        pygame.display.update()