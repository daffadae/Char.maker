import pygame as pg

pg.init()

window = pg.display.set_mode((1280,720))
pg.display.set_caption('Dating sim!')
running = True

icon = pg.image.load('pics/icon.png')
pg.display.set_icon(icon)


def character():
    x = 0
    y = 0
    charImg = pg.image.load("pics/character.png")
    window.blit(charImg, (x, y))

while running:
    window.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break
    #    if event.type == pg.KEYDOWN:
    #        if event.key == pg.K_SPACE:
    pg.display.update()
