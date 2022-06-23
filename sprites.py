import pygame
from pygame.locals import *

from settings import HEIGHT, WHITE, WIDTH


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        groups = [game.all_sprites]
        super().__init__(groups)
        self.image = pygame.Surface((32, 32))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH//2 - 16
        self.rect.y = HEIGHT//2 - 16
        self.pos = pygame.Vector2(self.rect.x, self.rect.y)
        self.gravity = pygame.Vector2(0, 5)
        self.velocity = pygame.Vector2(0, 0)
        self.is_jumping = False
    
    def update(self):
        keys = pygame.key.get_pressed()
        self.velocity = pygame.Vector2(0, 0)

        if keys[K_LEFT] or keys[K_a]:
            self.velocity.x = -5
        if keys[K_RIGHT] or keys[K_d]:
            self.velocity.x = 5
        if (keys[K_UP] or keys[K_w]):
            self.velocity.y = -10
        
        if self.rect.y + 5 <= HEIGHT - 32:
            self.velocity += self.gravity
        else:
            self.pos.y = HEIGHT - 32
        
        self.pos += self.velocity
        self.rect.topleft = self.pos
