import math
import random
import time
import sys
import pygame as pg


WIDTH = 800
HEIGHT = 500

# HP関連の機能を実装するためのクラス
class Hp:
    def __init__(self):
        self.width = 100

    #図形を生成するためのインスタンス
    def genfont(self, txt): 
        self.fonto = pg.font.Font(None, 25)
        self.txt = self.fonto.render(txt, True, (255, 255, 255))

    #　文字を生成するためのインスタンス
    def genobj(self, color, locate, hpbar_sur: pg.Surface):
        self.color = color
        self.locate = locate
        self.rct = pg.draw.rect(hpbar_sur, color, locate)

    # 文字と図形で違う処理で更新するインスタンス
    def update(self, hpbar_sur: pg.Surface, xy=None, txt=None):
        if txt: # 文字を生成
            self.obj = self.fonto.render(txt, True, (255, 255, 255))
            hpbar_sur.blit(self.obj, xy)
        elif self.rct: #　図形を生成
            print(self.locate)
            pg.draw.rect(hpbar_sur, self.color, self.locate)
        


def main():
    pg.display.set_caption("Under tale")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    sikaku1 = pg.Surface((400, 200))
    clock = pg.time.Clock()
    pg.draw.rect(sikaku1, (255, 255, 255), (0, 0, 400, 200))
    pg.draw.rect(sikaku1, (0, 0, 0), (5, 5, 390, 190))

    #　ここからhpクラスオブジェクトを生成
    hpbar_width = 100
    hpbar_sur = pg.Surface((250, 50)) # HPバーが表示される空間
    hp_HP = Hp()
    hp_HP.genfont("HP")
    hp_num = Hp()
    hp_num.genfont(f"{hpbar_width}/100")
    hp_bar_red = Hp()
    hp_bar_red.genobj((255, 0, 0), (50, 0, 100, 20), hpbar_sur)
    hp_bar_green = Hp()
    hp_bar_green.genobj((0, 255, 0), (50, 0, hpbar_width, 20), hpbar_sur)
    hp_bar_black = Hp()
    hp_bar_black.genobj((1, 1, 1), (170, 0, 100, 20), hpbar_sur)
    #　ここまで





    tmr = 0
    while True:
        hp_bar_green.width = hp_bar_green.width - tmr/100
        hp_bar_green.locate = (50, 0, hp_bar_green.width, 20)
        screen.blit(sikaku1, (200, 200))
        screen.blit(hpbar_sur, (250, 405)) # hpbar_surの表示位置の指定
        hpbar_sur.set_colorkey((0, 0, 0)) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
         
        #ここからhpクラスオブジェクトを更新
        hp_bar_black.update(hpbar_sur)
        hp_bar_red.update(hpbar_sur)
        hp_bar_green.update(hpbar_sur)
        hp_HP.update(hpbar_sur, [20, 5], "HP")
        hp_num.update(hpbar_sur, [170, 5], f"{hp_bar_green.width}/100")
        #　ここまで

        pg.display.update()
        tmr += 1
        clock.tick(30)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()