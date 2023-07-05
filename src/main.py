import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("Test Game")
     
    screen = pygame.display.set_mode((800, 600))

    y = 20
     
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill("white")

        pygame.draw.rect(screen, "blue", pygame.Rect(20, y, 50, 100))

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w]:
            y -= 0.5
            print("hi")
        
        pygame.display.update()

if __name__=="__main__":
    main()