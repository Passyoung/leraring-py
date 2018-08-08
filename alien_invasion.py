import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化游戏，创建一个屏幕对象
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings,screen,"Play")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个子弹数组
    bullets = Group()
    # 创建一个外星人
    aliens = Group()
    stats = GameStats(ai_settings)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏主循环
    while True:
        # 监测键盘和鼠标事件
        gf.check_events(ai_settings, screen,stats, play_button, ship, bullets)

        if stats.game_active:
            ship.updade()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen,stats, ship, aliens, bullets,play_button)


run_game()
