import pygame
import sys

def exit_on_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def game_loop(screen, background, x: int, y: int):
    while True:
        exit_on_close()

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        pygame.draw.rect(screen, "blue", pygame.Rect(x, y, 50, 100))

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w]:
            y -= 0.5
        if pressed_key[pygame.K_d]:
            x += 0.5
        if pressed_key[pygame.K_a]:
            x -= 0.5
        if pressed_key[pygame.K_s]:
            y += 0.5
        
        pygame.display.update() 

def main():
    pygame.init()
    pygame.display.set_caption("Test Game")
    
    game_loop(
        pygame.display.set_mode((800, 600)), 
        pygame.image.load("assets/images/grass.png").convert(),
        350,
        300
    )

if __name__=="__main__":
    main()