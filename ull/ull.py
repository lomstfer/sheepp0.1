import pygame
import sys
from random import randint
import math

pygame.init()

#WINDOW
WINW, WINH = 500, 500
WIN = pygame.display.set_mode((WINW, WINH))

#FÅR CLASS
class Får(pygame.sprite.Sprite):
    def __init__(self, p_x, p_y):
        super().__init__()
        self.image = (pygame.image.load("fåra/får0.png")).convert_alpha()
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect(center=(p_x, p_y))

    def update(self):
        m1 = randint(0,10)
        if m1 == 0:
            if self.rect.x < WINW-20 > 0 and self.rect.y < WINH > 0:
                self.rect.x += 3
            else: 
                self.rect.x = -40
                self.rect.y = randint(20, WINH-20)
        elif m1 == 1:
            if self.rect.x < WINW > 0 and self.rect.y < WINH > 0:
                self.rect.y += 1
            else: 
                self.rect.y = randint(20, WINH-20)
                self.rect.x = -40
        elif m1 == 2:
            if self.rect.x < WINW > 0 and self.rect.y < WINH > 0:
                self.rect.y -= 1
            else: 
                self.rect.y = randint(20, WINH-20)
                self.rect.x = -40

#STARTER PAINTINGS+RECTS
fårs = pygame.sprite.Group()
fårW, fårH = 14, 20

#exit
def exit_and_new_får():
    for E in pygame.event.get():
        if E.type == pygame.QUIT or E.type == pygame.KEYDOWN and E.key == pygame.K_ESCAPE: pygame.quit(), sys.exit()
        elif E.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            får = Får(mouse_pos[0], mouse_pos[1])
            fårs.add(får)
#paint
def paint():
    WIN.fill((108, 252, 104))
    fårs.update()
    fårs.draw(WIN)
    pygame.display.update()
#loop
while True:
    exit_and_new_får()
    paint()
    pygame.time.Clock().tick(6000)