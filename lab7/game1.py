import pygame
import time
import datetime

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("clock")

background = pygame.image.load("images/mickeybackg.png")
background =  pygame.transform.scale(background,(600,400))

chas = pygame.time.Clock()

lefts = pygame.image.load("images/lkol.png")
rightm = pygame.image.load("images/rkol.png")

center1 = (300,200)
lefts = pygame.transform.scale(lefts,(50,420))
rightm = pygame.transform.scale(rightm,(620,630))
min = lefts.get_rect(center=center1)
sec = rightm.get_rect(center=center1)

run = True
while run:
    screen.blit(background, (0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            pygame.quit()

    time = datetime.datetime.now()
    minang = -6*time.minute
    secang = -6*time.second


    rotationright = pygame.transform.rotate(rightm,minang)
    rectin = rotationright.get_rect(center=center1)
    rotationleft = pygame.transform.rotate(lefts,secang)
    rectin1 = rotationleft.get_rect(center=center1)

    screen.blit(background, (0, 0))
    screen.blit(rotationright,rectin)
    screen.blit(rotationleft, rectin1)

    pygame.display.update()
    chas.tick(60)