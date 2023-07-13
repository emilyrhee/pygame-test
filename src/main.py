import pygame
import sys

class Player:
    def __init__(self, x: float, y: float, color: str):
        self.x = x
        self.y = y
        self.color = color

def exit_on_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def game_loop(screen, background, player_one: Player):
    while True:
        exit_on_close()
        
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        pygame.draw.rect(screen, player_one.color, pygame.Rect(player_one.x, player_one.y, 50, 100))

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w]:
            player_one.y -= 0.5
        if pressed_key[pygame.K_d]:
            player_one.x += 0.5
        if pressed_key[pygame.K_a]:
            player_one.x -= 0.5
        if pressed_key[pygame.K_s]:
            player_one.y += 0.5
        
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