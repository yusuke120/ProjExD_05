import math
import random
import time
import sys
import pygame as pg


WIDTH = 800
HEIGHT = 500

def check_bound(obj_rct: pg.Rect) -> tuple[bool, bool]:
    yoko, tate = True, True
    if obj_rct.left < 390/2+10 or 595 < obj_rct.right:
        yoko = False
    if obj_rct.top < 205 or 395 < obj_rct.bottom:
        tate = False
    return yoko, tate

class player_move:
    
    delta = { # 押下キーと移動量の辞書
        pg.K_UP: (0, -1),
        pg.K_DOWN: (0, 1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0),
    }

    def __init__(self, xy: tuple[float, float]):
        self.img = pg.transform.flip(  # 左右反転
            pg.transform.rotozoom(  # 
                pg.image.load(f"fig/0.png"), 
                                0, 
                                0.02), 
                                True, 
                                False)
        self.rct = self.img.get_rect()
        self.rct.center = xy

    def update(self,key_lst: list[bool],screen:pg.Surface):
        sum_mv = [0, 0]
        for k, mv in __class__.delta.items():
            if key_lst[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        self.rct.move_ip(sum_mv)
        if check_bound(self.rct) != (True, True):
            self.rct.move_ip(-sum_mv[0], -sum_mv[1])
        
        screen.blit(self.img, self.rct)


def main():
    pg.display.set_caption("Under tale")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    sikaku1 = pg.Surface((400, 200))
    pg.draw.rect(sikaku1, (255, 255, 255), (0, 0, 400, 200))
    pg.draw.rect(sikaku1, (0, 0, 0), (5, 5, 390, 190))

    player = player_move((WIDTH/2, HEIGHT/2))

    clock = pg.time.Clock()#動くの遅くする
    while True:
        screen.blit(sikaku1, (200, 200))    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            
        key_lst = pg.key.get_pressed()
        player.update(key_lst, screen)#わい
        pg.display.update()
        clock.tick(165)#動くの遅くする
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()