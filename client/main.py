import pygame

from utils import load_image, scale_image, set_alpha, draw_on_screen, draw_rect
from paths import DEBUG_IMAGE_PATH
from colors import *

pygame.init()

screen_size:tuple[int, int] = (640, 640)
frame_rate:float = 60.0
clock = pygame.time.Clock()
screen = pygame.display.set_mode(screen_size)
running:bool = True

debug_img = load_image(DEBUG_IMAGE_PATH)
debug_img = scale_image(debug_img, 2)

x:int = 0
delta_time:float = 0.1

moving_left:bool = False
moving_right:bool = False
jumping:bool = False
grounded:bool = False
meele:bool = False
shooting:bool = False

while running:
    screen.fill(WHITE)
    
    draw_on_screen(screen, debug_img, (x, 30))
    draw_rect(screen, GREEN, (300, 0), (160, 280))

    side_modifier = 1 if moving_right else -1 if moving_left else 0
    x += 50 * delta_time * side_modifier

    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
            case pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    moving_right = True
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_SPACE:
                    jumping = True
            case pygame.KEYUP:
                if event.key == pygame.K_d:
                    moving_right = False
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_SPACE:
                    jumping = False
            case pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    meele = True
                if event.button == 2:
                    shooting = True
            case _:
                continue

    pygame.display.flip()
    delta_time = clock.tick(frame_rate) / 1000
    delta_time = max(0.001, min(0.1, delta_time))

pygame.quit()
