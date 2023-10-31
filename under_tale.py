import math
import random
import time
import sys
import pygame as pg


WIDTH = 800
HEIGHT = 450


def main():
    pg.display.set_caption("Under tale")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    sikaku1 = pg.Surface((650, 375))
    pg.draw.rect(sikaku1, (255, 255, 255), (150, 160, 700, 420))
    pg.draw.rect(sikaku1, (0, 0, 0), (155, 165, 490, 205))

    while True:
        screen.blit(sikaku1, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            
        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()