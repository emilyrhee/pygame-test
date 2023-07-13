import pygame
import sys

class Player:
    def __init__(self, x: float, y: float, color: str):
        self.x = x
        self.y = y
        self.color = color
        self.speed = 0.5

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            pygame.Rect(self.x, self.y, 50, 100)
        )
    
    def move_up(self):
        self.y -= self.speed
    
    def move_down(self):
        self.y += self.speed
    
    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

def exit_on_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def key_input(pressed_key, player_one: Player):
    if pressed_key[pygame.K_w]:
        player_one.move_up()
    if pressed_key[pygame.K_s]:
        player_one.move_down()
    if pressed_key[pygame.K_a]:
        player_one.move_left()
    if pressed_key[pygame.K_d]:
        player_one.move_right()

def game_loop(screen, background, player_one: Player):
    while True:
        exit_on_close()
        
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        player_one.draw(screen)

        key_input(pygame.key.get_pressed(), player_one)
        
        pygame.display.move_update() 

def main():
    pygame.init()
    pygame.display.set_caption("Test Game")

    game_loop(
        pygame.display.set_mode((800, 600)), 
        pygame.image.load("assets/images/grass.png").convert(),
        Player(350, 300, "blue")
    )

if __name__=="__main__":
    main()