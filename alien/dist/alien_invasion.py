import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():
    #初始化游戏，并创建屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建飞船
    ship=Ship(ai_settings,screen)
    #创建用于存储子弹的编组
    bullets=Group()
    #创建外星群
    aliens=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        print(len(bullets))
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()
