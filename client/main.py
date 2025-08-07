import pygame

from utils import load_image, scale_image, set_alpha
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
moving:bool = False

while running:
    screen.fill(WHITE)
    
    screen.blit(debug_img, (x, 30))
    hitbox = pygame.Rect(x, 30, debug_img.get_width(), debug_img.get_height())

    mpos = pygame.mouse.get_pos()

    target = pygame.Rect(300, 0, 160, 280)
    collision:bool = hitbox.colliderect(target)
    m_collision:bool = target.collidepoint(mpos)
    pygame.draw.rect(screen, (255 * collision, 255 * m_collision, 0), target)

    x += 50 * delta_time * moving

    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
            case pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    moving = True
            case pygame.KEYUP:
                if event.key == pygame.K_d:
                    moving = False
            case _:
                continue

    pygame.display.flip()
    delta_time = clock.tick(frame_rate) / 1000
    delta_time = max(0.001, min(0.1, delta_time))

pygame.quit()
