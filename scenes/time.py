# Created on Thu May 24 2024
# Copyright (c) 2024 BP Feral
# Python 3.12.1

import pygame, sys
# ===================================================================

from classes.button import MenuButton
# ===================================================================

def cast(value, max_seconds):
    if max_seconds != 0:
        percentage = value / max_seconds * 100
        return percentage / 100 * 700
    else:
        return 0

def showTime(screen, execution_times, clock):
    font = pygame.font.Font(None, 42)
    backButton = MenuButton(50, 720-50, 15 * len('< Back'), font, '< Back', (128, 145, 71), 0)

    val1_color = (117, 36, 47)
    val2_color = (49, 106, 117)
    val3_color = (47, 122, 67)
    val4_color = (73, 45, 97)

    val1text = font.render('%.3fs backtracking' % execution_times[0], True, val1_color)
    val2text = font.render('%.3fs alpinist' % execution_times[1], True, val2_color)
    val3text = font.render('%.3fs calire' % execution_times[2], True, val3_color)
    val4text = font.render('%.3fs genetic' % execution_times[3], True, val4_color)

    timetext = font.render('time', True, (125, 128, 116))
    solutiontext = font.render('solution', True, (125, 128, 116))

    max_seconds = 0
    for item in execution_times:
        max_seconds = item if item > max_seconds else max_seconds
    
    start_pos = [300, 600]

    end_points = [0, 0, 0, 0]
    # 0 - max_seconds   cast   300 --- 1000
    end_points[0] = cast(execution_times[0], max_seconds)
    end_points[1] = cast(execution_times[1], max_seconds)
    end_points[2] = cast(execution_times[2], max_seconds)
    end_points[3] = cast(execution_times[3], max_seconds)
    
    pannel = pygame.Rect(300, 100, 700, 500)

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

        screen.blit(val1text, (5, 100))
        screen.blit(val2text, (5, 150))
        screen.blit(val3text, (5, 200))
        screen.blit(val4text, (5, 250))

        pygame.draw.rect(screen, (255, 255, 255), pannel, 1)
        screen.blit(timetext, (600, 600))
        screen.blit(solutiontext, (180, 350))

        pygame.draw.line(screen, val1_color, start_pos, (end_points[0] + 300, 100 if end_points[0] > 0 else 600), 2)
        pygame.draw.line(screen, val2_color, start_pos, (end_points[1] + 300, 100 if end_points[1] > 0 else 600), 2)
        pygame.draw.line(screen, val3_color, start_pos, (end_points[2] + 300, 100 if end_points[2] > 0 else 600), 2)
        pygame.draw.line(screen, val4_color, start_pos, (end_points[3] + 300, 100 if end_points[3] > 0 else 600), 2)

        clock.tick(60)
        pygame.display.update()