import pygame as pg

pg.init()

window = pg.display.set_mode((1280,720))
pg.display.set_caption('Dating sim!')
running = True

icon = pg.image.load('pics/icon.png')
pg.display.set_icon(icon)

black =(0, 0, 0)

font = pg.font.Font('freesansbold.ttf', 32)
text = font.render('Test text', True, black)
def character():
    x = 0
    y = 0
    charImg = pg.image.load("pics/character.png")
    window.blit(charImg, (x, y))

while running:
    window.fill((255, 255, 255))
    window.blit(text)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break
    #    if event.type == pg.KEYDOWN:
    #        if event.key == pg.K_SPACE:
    pg.display.update()

