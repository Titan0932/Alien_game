import sys
from Ship_class import Ship
from Bullets import Bullets
import pygame
from Aliens import aliens
import random
import time

bullet_num=6

def check_events(ship,bullets,screen,ai_settings,play,alien):
    #Respond to keypresses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play.rect.collidepoint(mouse_x, mouse_y):
               check_play_button(ai_settings, play, mouse_x, mouse_y,alien,bullets)
                
        elif event.type==pygame.KEYDOWN:
            check_key_down(event,ship,bullets,screen,ai_settings)

        elif event.type==pygame.KEYUP:
            check_key_up(event,ship)

def check_play_button(ai_settings, play, mouse_x, mouse_y,alien,bullets):
    button_clicked = play.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not ai_settings.game_active:
        ai_settings.game_active = True
        bullets.empty()
        alien.empty()
        #clock=pygame.time.Clock()
        ai_settings.start_time=0
        ai_settings.start_time=time.time()
        pygame.mouse.set_visible(False) #hides mouse cursor

def produce_bullet(screen,ship,ai_settings,bullets):
    global bullet_num
    bullet_num-=1
    new_bullet=Bullets(screen,ai_settings,ship)
    bullets.add(new_bullet)

def check_key_down(event,ship,bullets,screen,ai_settings):
    global bullet_num
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    if event.key==pygame.K_LEFT:
        ship.moving_left=True    
    if event.key==pygame.K_UP:
        ship.moving_forward=True
    if event.key==pygame.K_DOWN:
        ship.moving_backward=True
    if event.key==pygame.K_SPACE:
        if bullet_num!=0:
            produce_bullet(screen,ship,ai_settings,bullets) 
            
            

    if event.key==pygame.K_r:

        bullet_num=6
         
        

def check_key_up(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    if event.key==pygame.K_LEFT:
        ship.moving_left=False
    if event.key==pygame.K_UP:
        ship.moving_forward=False
    if event.key==pygame.K_DOWN:
        ship.moving_backward=False

def create_aliens(screen,ai_settings,alien,alien_num):
    alien_num+=1
    if len(alien)<4:
        number=random.randint(0,8)  
        alien.add(aliens(screen,ai_settings))
    if alien_num==50: 
        alien.add(aliens(screen,ai_settings))
        alien_num=0
    return alien_num


def update_bullets(alien, bullets,ship):
    power=False
    p_num=random.randint(0,5)
    if p_num==4: power=True
    if power==True:
        collissions= pygame.sprite.groupcollide(bullets, alien, False, True) #kills aliens along its path without disappearing
        

    else:
        collissions = pygame.sprite.groupcollide(bullets, alien, True, True)
    
    if collissions!={}:
        ship.score+=1

    


def bullet_operations(bullets,screen,alien,ship):     
    for bullet in bullets:
        bullet.bullet_upgrade()
        bullet.blitme()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        update_bullets(alien,bullets,ship)

def alien_operations(alien,screen,ship):
    correction=float(0.7)

    for count in alien.sprites():
        if count.left_touch==False:
            if count.rect.centerx>=1050 and count.rect.centery<=350:
                count.rect.y+=1 #round(random.uniform(0.1,0.5),1)
            else:
                count.rect.centerx-=correction
        else:
            count.rect.centerx+=1
        count.rect.y+=1 #round(random.uniform(0.1,0.8),1)
        if count.rect.left==count.screen_rect.left: 
            count.left_touch=True
        if count.rect.right==count.screen_rect.right: 
            count.left_touch=False
    for a in alien:
        if a.rect.top==a.screen_rect.bottom:
            alien.remove(a)

    ship_life(ship,screen)


def ship_life(ship,screen):
    pygame.font.init() 
    myfont = pygame.font.SysFont('AlternateGothic2 BT', 30)
    text = myfont.render(f'Lives remaining: {ship.lives}', False, (252, 0, 0))
    screen.blit(text,(0,0))

def lose_message(screen,ship):
    
    pygame.font.init() 
    msg = pygame.font.SysFont('AlternateGothic2 BT', 150)
    text = msg.render('YOU LOSE!!!!', False, (252, 0, 0))
    screen.blit(text,(450,350))
    pygame.display.flip()
    

def start(screen):
    pygame.font.init() 
    move_msg = pygame.font.SysFont('AlternateGothic2 BT', 40)
    reload_msg = pygame.font.SysFont('AlternateGothic2 BT', 40)
    shoot_msg = pygame.font.SysFont('AlternateGothic2 BT', 40)
    game_msg = pygame.font.SysFont('AlternateGothic2 BT', 80)
    move = move_msg.render('Use Arrow Keys to control the Ship', False, (252, 0, 0))
    shoot = shoot_msg.render('Press Spacebar to shoot', False, (252, 0, 0))
    reload = reload_msg.render('R to reload (max 6 bullets)', False, (252, 0, 0))
    game = game_msg.render('KILL ALL THE ALIENS!!!!!', False, (252, 0, 0))
    screen.blit(move,(0,50))
    screen.blit(shoot,(0,100))
    screen.blit(reload,(0,150))
    screen.blit(game,(0,250))

    pygame.display.flip()
    


def disp_score(ship,screen,ai_settings):
    msg="Score: "+str(ship.score)
    #pygame.font.init()
    score_msg=pygame.font.SysFont('AlternateGothic2 BT', 40)
    score=score_msg.render(msg,False,(252,0,0))
    screen.blit(score,(0,ai_settings.screen_height-50))


def reset_stats(alien,bullets,ai_settings):
    ai_settings.start_time=0
    alien.empty()
    bullets.empty()
    ai_settings.game_active = False

def calc_time(ai_settings):
    msc=ai_settings.start_time
    secs=msc*10**(-3)
    min=str(secs//60)
    index=secs//60
    secs=str(secs-index*60)
    final_time=min[:min.find('.')] + ':'+ secs[:secs.find('.')]
    return final_time
    


def disp_time(ai_settings,screen):
    time=calc_time(ai_settings)
    time_font=pygame.font.SysFont('AlternateGothic2 BT',40)
    time_msg=time_font.render(time,False,(252,0,0))
    screen.blit(time_msg,(1300,0))
    

def upgrade_screen(ai_settings, screen, ship,bullets,alien,play):
    screen.fill(ai_settings.bgcolor)
    
    alien_operations(alien,screen,ship)
    
    if not ai_settings.game_active:
        start(screen)
        play.draw_button()

    if bullet_num==0:
        reload=pygame.image.load('reload.bmp') 
        screen.blit(reload,(1200,660))
    if pygame.sprite.spritecollideany(ship, alien):
        ship.lives-=1
        alien.remove(alien)
    alien.draw(screen)
    bullet_operations(bullets,screen,alien,ship)
    disp_score(ship,screen,ai_settings)
    disp_time(ai_settings,screen)
    ship.blitme()

    

        # Make the most recently drawn screen visible.
    pygame.display.flip()




