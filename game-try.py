import pygame as pg

pg.init()

window = pg.display.set_mode((800,400))
gameplay = True

class rectangle:
    def __init__(self, sideSize):
        self.sideSize = sideSize

xKordinaat = 1

while gameplay:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameplay = False
            break
    if xKordinaat==799:
        xKordinaat = 0
    pg.time.delay(5)
    window.fill((0,0,0))
    pg.draw.rect(window, (255, 0, 0), (xKordinaat,30,60,60)) #(window, (*rgb colour*), (sideSize1,sideSize2,x,y))
    pg.display.update()
    xKordinaat += 1