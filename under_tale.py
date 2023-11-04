import math
import random
import time
import sys
import pygame as pg


WIDTH = 800
HEIGHT = 500
#追加
jump_flag=0
cnt=0
jump=[]


class player_move:
    # 押下キーと移動量の辞書
    delta={ pg.K_UP: (0, -1),#ハートが赤いときの辞書
            pg.K_DOWN: (0, 1),
            pg.K_LEFT: (-1, 0),
            pg.K_RIGHT: (+1, 0),
        }
    delta2={ pg.K_UP: (0, -4),#ハートが青いときの辞書
            pg.K_DOWN: (0, 1),
            pg.K_LEFT: (-1, 0),
            pg.K_RIGHT: (+1, 0),
        }

    def __init__(self, xy: tuple[float, float],ao):
        #aoが０なら赤いハートで１なら青いハートの画像を使う
        if ao==0:
            self.img = pg.transform.flip(pg.transform.rotozoom(pg.image.load(f"fig/0.png"),0,0.02),True, False)
        elif ao==1:
            self.img = pg.transform.flip(pg.transform.rotozoom(pg.image.load(f"fig/1.png"),0,0.02),True, False)
        self.rct = self.img.get_rect()
        self.rct.center = xy

    def update(self,key_lst: list[bool],screen:pg.Surface,ao):
        sum_mv = [0, 0]

        #普通のハートが赤いとき
        if ao==0:
            for k, mv in __class__.delta.items():
                if key_lst[k]:
                    sum_mv[0] += mv[0]
                    sum_mv[1] += mv[1]
            self.rct.move_ip(sum_mv)

            #ハートが枠から出ないようにする
            if self.rct[1]<=205:#上
                self.rct[1]=205
            if self.rct[1]>=376:#した
                self.rct[1]=376
            if self.rct[0]>=578:#右
                self.rct[0]=578
            if self.rct[0]<=205:#左
                self.rct[0]=205


        #ハートが青いとき
        elif ao==1:
            global jump,cnt
            jump.append(self.rct[1])  
            for k, mv in __class__.delta2.items():   
                if self.rct[1]<=376:#ハートが枠の下についていないとき落ちる
                    sum_mv[1]+=0.3
                
                if key_lst[k]:
                    sum_mv[0] += mv[0]
                    print(jump[cnt],jump[cnt-1])
                    if jump[cnt]<=jump[cnt-1]:#ハートが前回より下がっているときは上にいけない
                        sum_mv[1] += mv[1]


            self.rct.move_ip(sum_mv)
            if self.rct[1]<=205:#上
                self.rct[1]=205
            if self.rct[1]>=375:#した
                self.rct[1]=375
            if self.rct[0]>=578:#右
                self.rct[0]=578
            if self.rct[0]<=205:#左
                self.rct[0]=205
            cnt+=1

        screen.blit(self.img, self.rct)
#追加

def main():
    pg.display.set_caption("Under tale")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    sikaku1 = pg.Surface((400, 200))
    pg.draw.rect(sikaku1, (255, 255, 255), (0, 0, 400, 200))
    pg.draw.rect(sikaku1, (0, 0, 0), (5, 5, 390, 190))
    
    ##追加
    ao_flag=1
    if ao_flag==0:#ハートが赤の時は真ん中からスタート
        player = player_move((WIDTH/2, HEIGHT/2),ao_flag)
    elif ao_flag==1:#ハートが青の時地面からスタート
        player = player_move((WIDTH/2, 376),ao_flag)
    clock = pg.time.Clock()
    ##追加

    while True:
        screen.blit(sikaku1, (200, 200))    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            
        ##追加
        key_lst = pg.key.get_pressed()
        player.update(key_lst, screen,ao_flag)
        pg.display.update()
        clock.tick(165)#動くの遅くする
        ##追加

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()