import pygame as pg
import sys

dialogue1 = []
for x in range(3):
    dialogue1.append(pg.image.load("pics/" + str(x) + ".jpg"))
    x += 1

def startGame():
    pg.init()
    window2 = pg.display.set_mode((800, 900))
    pg.display.set_caption("Date Sim!")

    while True:
        for event in pg.event.get():
            x = 0
            for texts in range(3):
                window2.blit(dialogue1[x], (0,0))
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN or event.type == pg.K_SPACE:
                    x += 1



        pg.display.update()


pg.init()
window = pg.display.set_mode((1280, 720))
pg.display.set_caption("Date Sim!")
main_font = pg.font.SysFont(None, 50)
def switch():
    window.blit(dialogue1[0], (0,0))
class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        window.blit(self.image, self.rect)
        window.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            switch()
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, (127,255,0))
        else:
            self.text = main_font.render(self.text_input, True,(255, 255, 255))


button_surface = pg.image.load("button.jpeg")
button_surface = pg.transform.scale(button_surface, (430, 120))

button = Button(button_surface, 640, 360, "Start!")

while True:
    for event in pg.event.get():
        window.fill((255, 255, 255))

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            button.checkForInput(pg.mouse.get_pos())
            startGame()

    button.update()
    button.changeColor(pg.mouse.get_pos())

    pg.display.update()
