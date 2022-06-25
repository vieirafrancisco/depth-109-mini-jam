import random

import pygame

from settings import GREEN, RED, WIDTH, HEIGHT, BLACK, WHITE, FPS, YELLOW
from sprites import Fish, Player


def HUD(game):
    # shooting cooldown
    if not game.is_shooting:
        pygame.draw.rect(game.display, WHITE, (WIDTH - 50, 25, 25, 150))
    else:
        pygame.draw.rect(game.display, WHITE, (WIDTH - 50, 25, 25, 150 * min(game.cooldown, 1)))
    pygame.draw.rect(game.display, BLACK, (WIDTH - 50, 25, 25, 150), width=2)


class Game:
    def __init__(self) -> None:
        self.display = None
        self.is_running = False
        self.clock = pygame.time.Clock()

    def start(self) -> None:
        pygame.init()
        pygame.font.init()

        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.is_running = True

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.fishs = pygame.sprite.Group()

        self.player = Player(self)
        self.cooldown = 0
        self.is_shooting = False

    def cleanup(self) -> None:
        pygame.font.quit()
        pygame.quit()

    def execute(self) -> None:
        self.start()
        while self.is_running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.display.fill((156, 185, 247))
            self.render()
            self.update()
            pygame.display.flip()
            self.dt = self.clock.tick(FPS) / 1000
        self.cleanup()

    def handle_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self.is_running = False

    def render(self) -> None:
        pygame.display.set_caption(f"Depth - FPS: {round(self.clock.get_fps(), 2)}")
        self.all_sprites.draw(self.display)

        # sea
        sea = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        sea.fill((51, 104, 220, 128))
        self.display.blit(sea, (0, 125))

        HUD(self)

    def update(self) -> None:
        self.player.update()

        for sprite in self.fishs:
            sprite.update()

        has_mouse_click = pygame.mouse.get_pressed()[0]
        if not self.is_shooting and has_mouse_click:
            Fish(self)
            self.is_shooting = True
        
        # shooting cooldown
        if self.is_shooting:
            self.cooldown += self.dt
        
        if self.cooldown >= 1:
            self.cooldown = 0
            self.is_shooting = False

if __name__ == "__main__":
    game = Game()
    game.execute()
