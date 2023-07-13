import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("Test Game")
     
    screen = pygame.display.set_mode((800, 600))

    x = 350
    y = 300

    background = pygame.image.load("assets/images/grass.png").convert()
     
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill((0, 0, 0, 0))
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

if __name__=="__main__":
    main()