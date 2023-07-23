import pygame
import sys

class Player:
    def __init__(self, x: float, y: float, color: str):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 100
        self.color = color
        self.speed = 2

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            pygame.Rect(self.x, self.y, self.width, self.height)
        )
    
    def move_up(self):
        self.y -= self.speed
    
    def move_down(self):
        self.y += self.speed
    
    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

class Image:
    def __init__(self, x: float, y: float, img_path: str):
        self.x = x
        self.y = y
        self.img_path = img_path

    def draw(self, screen: pygame.Surface):
        screen.fill((0, 0, 0))
        screen.blit(
            pygame.image.load(self.img_path).convert(),
            (self.x, self.y)
        )

def exit_on_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def key_input(pressed_key: pygame.key.ScancodeWrapper, player_one: Player):
    if pressed_key[pygame.K_w]:
        player_one.move_up()

    if pressed_key[pygame.K_s]:
        player_one.move_down()

    if pressed_key[pygame.K_a]:
        player_one.move_left()

    if pressed_key[pygame.K_d]:
        player_one.move_right()

def game_loop(
    screen: pygame.Surface, 
    background: Image, 
    player_one: Player
):
    while True:
        exit_on_close()
        background.draw(screen)
        player_one.draw(screen)
        key_input(pygame.key.get_pressed(), player_one)
        pygame.display.update()

def main():
    pygame.init()
    pygame.display.set_caption("Test Game")

    display_width: int = 800
    display_height: int = 600

    game_loop(
        pygame.display.set_mode((display_width, display_height)), 
        Image(0, 0, "assets/images/ground.jpg"),
        Player(display_width/2, display_height/2, "blue")
    )

if __name__=="__main__":
    main()