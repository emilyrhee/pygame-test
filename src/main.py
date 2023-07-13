import pygame
import sys

class Player:
    def __init__(self, x: float, y: float, color: str):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            pygame.Rect(self.x, self.y, 50, 100)
    )
    
    def up(self):
        self.y -= 0.5
    
    def down(self):
        self.y += 0.5
    
    def left(self):
        self.x -= 0.5

    def right(self):
        self.x += 0.5

def exit_on_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def key_input(pressed_key, player_one):
    if pressed_key[pygame.K_w]:
        player_one.up()
    if pressed_key[pygame.K_s]:
        player_one.down()
    if pressed_key[pygame.K_a]:
        player_one.left()
    if pressed_key[pygame.K_d]:
        player_one.right()

def game_loop(screen, background, player_one: Player):
    while True:
        exit_on_close()
        
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        player_one.draw(screen)

        key_input(pygame.key.get_pressed(), player_one)
        
        pygame.display.update() 

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