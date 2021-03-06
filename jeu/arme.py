import sys
import pygame
from random import randint
from pygame import *
import math
import os

sys.path.append(os.path.join('menu'))
sys.path.append(os.path.join('jeu'))
sys.path.append(os.path.join('sound'))
sys.path.append(os.path.join('hugo_boss.py'))

from time import sleep
from entity import Entity

img_swordr="graphics/arme/sword/ironsword.png"
img_swordl="graphics/arme/sword/ironswordl.png"

class Arme(Entity):
    atk_max= 20
    atk=atk_max
    r = False
    l = False

    def __init__(self, x, y):
        Entity.__init__(self)

        self.xvel = x+10
        self.yvel = y+10
        self.image = image.load(img_swordr)
        (hauteur, largeur) = self.image.get_size()
        self.rect = Rect(x, y, hauteur, largeur)
        self.onGround = False

    def realease(self):
        self.xvel = 8
        self.yvel = 8

    def update(self, up, down, left, right, running, platforms, boss, player, screen):
        if boss.inv % 10 == 5:
            boss.image = pygame.image.load(boss.img_bossf).convert()
            boss.image.set_alpha(0)
        elif boss.inv%10 == 0:
            boss.image = pygame.image.load(boss.img_bossf)
        if running==True and self.atk==0:
            self.atk=self.atk_max
        if left:
            self.l=True
            self.r=False
        elif right:
            self.l=False
            self.r=True

        if  self.atk !=0:
            if self.l:
                self.xvel = -8
                self.image = pygame.image.load(img_swordl)
                self.rect.top = player.rect.top+25
                self.rect.left = player.rect.left-45
            elif self.r:
                self.xvel = 8
                self.image = pygame.image.load(img_swordr)
                self.rect.top = player.rect.top+25
                self.rect.left = player.rect.left+45
            else:
                self.xvel = 8
                self.image = pygame.image.load(img_swordr)
                self.rect.top = player.rect.top+25
                self.rect.left = player.rect.left+45
            self.atk-=1

        else:
            self.rect.top = player.rect.top
            self.rect.left = player.rect.left
            self.image = pygame.image.load(img_swordr).convert()
            self.image.set_alpha(0)
        if self.atk > 0:
            return self.hitbox(0, self.yvel, boss, screen)
        else :
            return False

    def hitbox(self, xvel, yvel, boss, screen):
        if pygame.sprite.collide_rect(self, boss):
            pygame.mixer.init(44100, -16, 2, 2048)
            son=pygame.mixer.Sound("sound/SmallExplosion8-Bit.ogg")
            son.play()
            if boss.inv==0:
                boss.hp-=1
                boss.xvel*=-1
                boss.inv = boss.max_inv

            if boss.hp==0:
                return True
            else:
                return False
