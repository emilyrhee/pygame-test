import pygame
import sys

class Player:
    def __init__(self, x: float, y: float):
        self.pos = pygame.math.Vector2((x, y))
        self.size = pygame.math.Vector2((50, 100))
        self.speed = 2

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            "blue",
            pygame.Rect(
                self.pos.x - self.size.x / 2,
                self.pos.y - self.size.y / 2,
                self.size.x,
                self.size.y
            )
        )
    
    def move_up(self):
        self.pos.y -= self.speed
    
    def move_down(self):
        self.pos.y += self.speed
    
    def move_left(self):
        self.pos.x -= self.speed

    def move_right(self):
        self.pos.x += self.speed

class Image:
    def __init__(self, x: float, y: float, img_path: str):
        self.pos = pygame.math.Vector2((x, y))
        self.img_path = img_path

    def draw(self, screen: pygame.Surface):
        screen.fill((0, 0, 0))  # move out of Image class
        screen.blit(
            pygame.image.load(self.img_path).convert(),
            (self.pos.x, self.pos.y)
        )

def exit_on_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def key_input(pressed_key: pygame.key.ScancodeWrapper, player: Player):
    if pressed_key[pygame.K_w]:
        player.move_up()

    if pressed_key[pygame.K_s]:
        player.move_down()

    if pressed_key[pygame.K_a]:
        player.move_left()

    if pressed_key[pygame.K_d]:
        player.move_right()

def game_loop(
    screen: pygame.Surface, 
    background: Image, 
    player_one: Player,
    camera: pygame.math.Vector2,
    display: pygame.math.Vector2
):
    while True:
        exit_on_close()

        key_input(pygame.key.get_pressed(), player_one)

        camera.x = player_one.pos.x - display.x / 2
        camera.y = player_one.pos.y - display.y / 2

        background.draw(screen)
        player_one.draw(screen)

        pygame.display.update()

# Refer to this:
# https://stackoverflow.com/a/67534644
def main():
    pygame.init()
    pygame.display.set_caption("Test Game")

    display = pygame.math.Vector2((800,600))
    background = Image(0, 0, "assets/images/ground.jpg")
    player_one = Player(display.x / 2, display.y / 2)

    game_loop(
        pygame.display.set_mode((display.x, display.y)), 
        background,
        player_one,
        pygame.math.Vector2((0, 0)),
        display
    )

if __name__=="__main__":
    main()