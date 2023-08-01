#!/usr/bin/env python3

import pygame
import sys

class Player:
    def __init__(self, x: float, y: float):
        self.pos = pygame.math.Vector2((x, y))
        self.size = pygame.math.Vector2((50, 100))
        self.speed = 2

    def draw(self, screen: pygame.Surface, display: pygame.math.Vector2):
        pygame.draw.rect(
            screen,
            "blue",
            pygame.Rect(
                display.x / 2 - self.size.x / 2,
                display.y / 2 - self.size.y / 2,
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
        self.image = pygame.image.load(img_path).convert_alpha()

    def draw(self, screen: pygame.Surface, camera: pygame.math.Vector2):
        screen.fill((0, 0, 0))  # move out of Image class
        screen.blit(
            self.image,
            (self.pos.x - camera.x, self.pos.y - camera.y)
        )
    
    def get_position(self, camera: pygame.math.Vector2):
        return pygame.math.Vector2((
            self.pos.x - camera.x,
            self.pos.y - camera.y
        ))

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
    display: pygame.math.Vector2,
    display_rect: pygame.math.Vector2
):
    while True:
        exit_on_close()

        key_input(pygame.key.get_pressed(), player_one)

        camera.x = player_one.pos.x - display.x / 2
        camera.y = player_one.pos.y - display.y / 2

        background.draw(screen, camera)
        player_one.draw(screen, display)

        pygame.display.update()

# Refer to this:
# https://stackoverflow.com/a/67534644
def main():
    pygame.init()
    pygame.display.set_caption("Test Game")

    display = pygame.math.Vector2((800,600))
    display_rect = pygame.Rect(
        (0, 0),
        (display.x, display.y)
    )

    game_loop(
        pygame.display.set_mode((display.x, display.y)),
        Image(0, 0, "assets/images/ground.jpg"),
        Player(display.x / 2, display.y / 2),
        pygame.math.Vector2((0, 0)),
        display,
        display_rect
    )

if __name__=="__main__":
    main()