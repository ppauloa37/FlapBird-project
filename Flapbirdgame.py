import pygame
import os
import random

tela_width = 500
tela_height = 800

imagen_pipe = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','pipe.png')))
imagem_chao = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','base.png')))
imagem_cenario = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bg.png')))
imagem_personagem = [
pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird2.png'))),
pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','pipe.png'))) ]

pygame.font.init()

font_rewnads = pygame.font.SysFont('sans', 45)


class Personagem:
    IMGS = imagem_personagem
    rotcao_max = 25
    rotcao_velo = 20
    tmp_animation = 5

    def __init__(self, x,y):
        self.x
        self.y
        self.angl = 0
        self.veloc = 0
        self.pwa = self.y
        self.tmp = 0
        self.ctimg = 0
        self.aimg = self.IMGS[0]
    def pular(self):
            self.veloc = -10.5
            self.tmp = 0
            self.pwa = self.y
    def move(self):
        self.tmp += 1
        deslc = 1.5 * (self.tmp**2) + self.veloc * self.tmp
        if deslc > 16:
             deslc = 16
        elif deslc < 0:
             deslc -= 2
        
        self.y += deslc

        if deslc < 0 or self.y < (self.pwa + 50):
             if self.angl < self.rotcao_max:
                  self.angl = self.rotcao_max
        else:
             if self.angl > -90:
                  self.angl - self.rotcao_velo
    def draws(self, tela):
        self.ctimg += 1

        if self.ctimg < self.tmp_animation:
            self.imagem = self.IMGS[0]
        elif self.ctimg < self.tmp_animation*2:
             self.imagem = self.IMGS[1]
        elif self.ctimg < self.tmp_animation*3:
             self.imagem = self.IMGS[2]
        elif self.ctimg < self.tmp_animation*4:
             self.imagem = self.IMGS[1]
        elif self.ctimg >= self.tmp_animation*4 + 1:
             self.imagem = self.IMGS[0]
             self.ctimg = 0

        if self.angl <= -80:
             self.imagem = self.IMGS[3]
             self.ctimg = self.tmp_animation*2
        img_rtc = pygame.transform.rotate(self.imagem, self.angl).center
        pos_center_img = self.imagem.get_rect(topleft=(self.x, self.y))
        rect = img_rtc.get_rect(center=pos_center_img)
        tela.blit(img_rtc, rect.topleft) 
        





class pipes:
    pass
class chao:
    pass


input("tst")
