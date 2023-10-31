import math
import random
import time
import sys
import pygame as pg


WIDTH = 800
HEIGHT = 500


def main():
    pg.display.set_caption("Under tale")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    sikaku1 = pg.Surface((400, 200))
    pg.draw.rect(sikaku1, (255, 255, 255), (0, 0, 400, 200))
    pg.draw.rect(sikaku1, (0, 0, 0), (5, 5, 390, 190))
    hpbar_width = 100
    hpbar_sur = pg.Surface((250, 50)) # HPバーが表示される空間
    hp_fonto = pg.font.Font(None, 25)
    hp_txt_num = hp_fonto.render(f"{hpbar_width}/100", True, (255, 255, 255))
    hp_txt = hp_fonto.render("HP", True, (255, 255, 255))


    tmr = 0
    while True:
        screen.blit(sikaku1, (200, 200))
        screen.blit(hpbar_sur, (250, 405)) # hpbar_surの表示位置の指定
        hpbar_sur.blit(hp_txt_num, [170, 5])
        hpbar_sur.blit(hp_txt, [20, 5])
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
        
        pg.draw.rect(hpbar_sur, (255, 0, 0), (50, 0, 100, 20)) # HPバー（赤）を表示
        pg.draw.rect(hpbar_sur, (0, 255, 0), (50, 0, hpbar_width-tmr/10, 20))  # HPバー（緑）を表示
        hpbar_sur.set_colorkey((0, 0, 0))  

        pg.display.update()
        tmr += 1


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()