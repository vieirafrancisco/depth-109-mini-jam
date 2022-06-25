import pygame
from pygame.locals import *

from settings import HEIGHT, WHITE, WIDTH


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        groups = [game.all_sprites]
        super().__init__(groups)
        self.game = game
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2(WIDTH//2 - 16, 0)
        self.rect.topleft = self.pos
        self.velocity = pygame.Vector2(0, 0)
    
    def update(self):
        keys = pygame.key.get_pressed()
        self.velocity = pygame.Vector2(0, 0)

        if keys[K_LEFT] or keys[K_a]:
            self.velocity.x = -5
        if keys[K_RIGHT] or keys[K_d]:
            self.velocity.x = 5
        
        self.pos += self.velocity

        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > WIDTH - self.image.get_width():
            self.pos.x = WIDTH - self.image.get_width()

        self.rect.topleft = self.pos


class Fish(pygame.sprite.Sprite):
    def __init__(self, game):
        groups = [game.all_sprites, game.fishs]
        super().__init__(groups)
        self.image = pygame.image.load("assets/fish.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2(game.player.pos.x+8, 32)
        self.rect.topleft = self.pos
        self.velocity = pygame.Vector2(0, 5)
    
    def update(self):
        if self.pos.y > HEIGHT:
            self.kill()
        
        self.pos += self.velocity
        self.rect.topleft = self.pos


class Mob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        groups = [game.all_sprites, game.mobs]
        super().__init__(groups)
        self.image = pygame.Surface((32, 32))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2(x, y)
        self.rect.topleft = self.pos
