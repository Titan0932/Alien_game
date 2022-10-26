import pygame
from settings import Settings
from Ship_class import Ship
import game_functions as gf
from Bullets import Bullets
from pygame.sprite import Group
import time
from button import Button




def game_run():

    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(screen,ai_settings) #makes a ship
    bullets=Group()
    alien=Group()
    alien_num=0
    play= Button(ai_settings,screen, "Play")
    
# Start the main loop for the game.
    gf.upgrade_screen(ai_settings, screen, ship,bullets,alien,play)
    while True:
# Watch for keyboard and mouse events.
        gf.check_events(ship,bullets,screen,ai_settings,play,alien)
        if ai_settings.game_active==True:
            ai_settings.start_time=pygame.time.get_ticks()
            alien_num=gf.create_aliens(screen,ai_settings,alien,alien_num)
        
            gf.update_bullets(alien, bullets,ship)
            ship.update()
            gf.upgrade_screen(ai_settings, screen, ship,bullets,alien,play)
        if ship.lives==-1:
            gf.lose_message(screen,ship)
            pygame.mouse.set_visible(True)
            time.sleep(3)
            ship=Ship(screen,ai_settings)
            gf.disp_time(ai_settings,screen)
            gf.reset_stats(alien,bullets,ai_settings)
            gf.upgrade_screen(ai_settings, screen, ship,bullets,alien,play)
            
    
        
               
game_run()


