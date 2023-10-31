import math
import random
import time
import sys
from typing import Any
import pygame as pg
import os

from pygame.sprite import AbstractGroup


WIDTH = 800
HEIGHT = 500
main_dir = os.path.split(os.path.abspath(__file__))[0]


def load_sound(file):
    """"""
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None


class Enemy(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.img =  pg.transform.scale(pg.image.load("ex05\data\pngwingcom_negate.png"), (300, 200))

    def update(self, screen: pg.Surface):
        screen.blit(self.img, (250, 0))


def main():
    pg.display.set_caption("Under tale")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    sikaku1 = pg.Surface((400, 200))
    pg.draw.rect(sikaku1, (255, 255, 255), (0, 0, 400, 200))
    pg.draw.rect(sikaku1, (0, 0, 0), (5, 5, 390, 190))

    emys = pg.sprite.Group()

    if pg.mixer:
        music = os.path.join(main_dir, "data", "DG.mp3")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    while True:
        screen.blit(sikaku1, (200, 200))
        emys.add(Enemy())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0

        emys.update(screen)    
        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()