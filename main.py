import pygame

from settings import WIDTH, HEIGHT, BLACK, WHITE, FPS
from sprites import Player


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

        self.player = Player(self)

    def cleanup(self) -> None:
        pygame.font.quit()
        pygame.quit()

    def execute(self) -> None:
        self.start()
        while self.is_running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.display.fill(BLACK)
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

    def update(self) -> None:
        self.player.update()

if __name__ == "__main__":
    game = Game()
    game.execute()
