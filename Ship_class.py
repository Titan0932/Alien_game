import pygame


class Ship():
    def __init__(self,screen,ai_settings):
        self.screen=screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('rocket_sample.png')
        self.ai_settings=ai_settings
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
# Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx #the center of the rect of rocket is placed at the screen's rect's center(the x-coordinates)
        self.rect.bottom = self.screen_rect.bottom # placing the rocket in the bottom of the screen(the y-coordinates)
        self.centerx=float(self.rect.centerx)
        self.centery=float(self.rect.centery)
        self.moving_right=False
        self.moving_left=False
        self.moving_forward=False
        self.moving_backward=False
        self.lives=5
        self.score=0

    def blitme(self): #Draw the ship at its current location(specified above).
        self.screen.blit(self.image, self.rect)


    def ship_movement(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.centerx+=self.ai_settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.centerx-=self.ai_settings.ship_speed
        self.rect.centerx=self.centerx

        if self.moving_forward and self.rect.top>0:        # top left corner is the origin always and y-axis value increases from top to bottom
            self.centery-= self.ai_settings.ship_speed
        if self.moving_backward and self.rect.bottom<self.screen_rect.bottom:
            self.centery+=self.ai_settings.ship_speed

        self.rect.centery=self.centery

    def update(self):
        self.ship_movement()