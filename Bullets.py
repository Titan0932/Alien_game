import pygame
from Ship_class import Ship
from pygame.sprite import Sprite


class Bullets(Sprite):

    def __init__(self,screen,ai_settings,ship):
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load('bullet.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.ship=ship
        self.rect.centerx=self.ship.centerx
        self.rect.top=self.ship.rect.top
        self.y=float(self.rect.centery)
        self.ai_settings=ai_settings
        
        self.rect.top=self.ship.rect.top

    def blitme(self): #Draw the ship at its current location(specified above).
        self.screen.blit(self.image, self.rect)


    def bullet_movement(self):
        if self.rect.bottom>=0:
            self.y-=self.ai_settings.bullet_speed 
            self.rect.centery=self.y


    def bullet_upgrade(self):
        self.bullet_movement()


    