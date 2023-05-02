import pygame, sys, os
from pygame.locals import *
from random import randint


tela = pygame.display.set_mode((640, 480))
loop = True
pygame.display.set_caption("Space Kombat")
pygame.init()
fundo = pygame.image.load(os.path.join("assets", "img", "espaco.png")).convert_alpha()
nave = pygame.image.load(os.path.join("assets","img","ship.png"))
relogio = pygame.time.Clock()
nave = pygame.transform.scale(nave,(60,60))
naverect = nave.get_rect(center = (200, 400))

move_Y = 420
move_X = 640/2

meteor_X = move_Y
meteor_Y = 200



while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            sys.exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                move_X -= 30
            if event.key == K_d:
                move_X += 30
            if event.key == K_w:
                move_Y -= 30
            if event.key == K_s:
                move_Y += 30
        '''
    pygame.display.update()
    if pygame.key.get_pressed()[K_a]:
        move_X -= 10
    if pygame.key.get_pressed()[K_d]:
        move_X += 10
    if pygame.key.get_pressed()[K_w]:
        move_Y -= 10
    if pygame.key.get_pressed()[K_s]:
        move_Y += 10
    
    tela.blit(fundo, (0, 0))
    tela.blit(nave, (move_X, move_Y))
    if move_Y <= 10:
        move_Y = 12
    if move_Y >= 420:
        move_Y = 420
    if move_X > 640:
        move_X = -40
    if move_X < -40:
        move_X = 640
    
    pygame.draw.circle(tela,(160,82,45),(meteor_X,meteor_Y),20)
    meteor_Y += 10
    
    if meteor_Y > 480:
        meteor_X = move_X + 30
        meteor_Y = 0
    pygame.display.update()

    relogio.tick(60)

pygame.quit()