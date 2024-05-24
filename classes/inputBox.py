# Created on Thu May 16 2024
# Copyright (c) 2024 BP Feral
# Python 3.12.1

import pygame
# ===================================================================

class inputBox:
    def __init__(self, screen, x, y, width, font):
        self.input_rect = pygame.Rect(x, y, width, 32)
        self.active = False
        self.screen = screen
        self.font = font
        self.width = width
        
        self.text_color = pygame.Color(255, 255, 255)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('gray15')

        self.content = ''
        self.color = self.color_passive
        self.allowed_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                              '\\', '!', '?', '.', ',', "'", '"', '@', '#', '%', '^', '&', '*', '-', '_', '+', '=', '|', ':', ';', '<', '>',
                              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '[', ']', '{', '}']
    def update(self, event):
            # Select by mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_rect.collidepoint(event.pos):
                    if self.active == False:
                        self.active = True
                else:
                    self.active = False

            if self.active == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.active = False
                        return

                    elif event.key == pygame.K_BACKSPACE:
                        self.content = self.content[:-1]
                        return
                
                    elif event.key == pygame.K_SPACE:
                        self.content += ' '
                        return

                    elif event.unicode in self.allowed_chars:
                        if len(self.content) < 3:
                            self.content += event.unicode

    def is_active(self):
        return self.active

    def get_content(self):
        return self.content

    def draw(self):

        if self.active:
            self.render = True
            self.color = self.color_active
            self.text_color = (255, 255, 255)

        else:
            self.color = self.color_passive
            self.text_color = self.color_passive

        text_surface = self.font.render(self.content, True, self.text_color)
        self.input_rect.w = self.width
        pygame.draw.rect(self.screen, self.color, self.input_rect, 2)
        self.screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))