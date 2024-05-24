# Created on Fri May 03 2024
# Copyright (c) 2024 BP Feral
# Python 3.12.1

import pygame
# ===================================================================

class MenuButton:
    def __init__(self, x, y, width, font, text, color, index):
        self.font = font
        self.text = text
        self.index = index
        
        self.x = x
        self.y = y
        
        self.width = width
        self.height = 50
        
        self.color = color
        self.button_text = self.font.render(self.text, True, self.color)

        self.hover = False
        self.disabled = False
        
        self.font_width = self.button_text.get_width()

        self.played = False
        self.hoverSound = pygame.mixer.Sound('./music/hover.mp3')
        self.hoverSound.set_volume(0.2)

        self.update_texture()


    def update_texture(self):
        self.surface = pygame.Surface((self.width, self.height))
        if self.hover and not self.disabled:
            pygame.draw.line(self.surface, self.color, (0, self.height - 18), (self.font_width, self.height - 18), 2)
            # pygame.draw.rect(self.surface, self.color, (0, 0, self.width, self.height), 1)
        self.surface.blit(self.button_text, (0, 0))

    def draw(self, surface) -> None:
        if self.disabled:
            self.color = (25, 25, 25)
            self.button_text = self.font.render(self.text, True, self.color)

        surface.blit(self.surface, (self.x, self.y))


    def update(self, event):
        mx, my = pygame.mouse.get_pos()

        if self.x < mx < self.x + self.width and self.y < my < self.y + self.height and not self.disabled:
            if self.played == False:
                self.played = True
                pygame.mixer.Sound.play(self.hoverSound, 0, 0)

            self.hover = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.update_texture()
                    if not self.disabled:
                        return True
                    else: return False
        else:
            self.hover = False
            self.played = False
            
        self.update_texture()
        return False