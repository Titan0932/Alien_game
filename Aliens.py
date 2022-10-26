import pygame
from pygame.sprite import Sprite
import random

class aliens(Sprite):
    def __init__(self,screen,ai_settings):
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.image=pygame.image.load('Alien_green.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        x_pos=float(random.randrange(0,self.screen_rect.right-100))
        self.rect.x=x_pos
        
        self.rect.y=0
        self.left_touch=False

    def blitme(self):
        self.screen.blit(self.image,self.rect)