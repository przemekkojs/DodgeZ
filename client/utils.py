import os
import pygame

from paths import DEBUG_IMAGE_PATH

def load_image(path:str):
    if not os.path.exists(path):
        return pygame.image.load(DEBUG_IMAGE_PATH).convert()

    return pygame.image.load(path).convert()

def load_image_alpha(path:str):
    if not os.path.exists(path):
        return pygame.image.load(DEBUG_IMAGE_PATH).convert()

    return pygame.image.load(path).convert_alpha()

def set_alpha(image, color:tuple[int, int, int]):
    image.set_colorkey(color)

def draw_on_screen(screen, image, position:tuple[int, int]):
    screen.blit(image, position)

def draw_rect(screen, color, position:tuple[float, float], size:tuple[float, float]):
    target = pygame.Rect(
        position[0],
        position[1],
        size[0],
        size[1]
    )

    return pygame.draw.rect(screen, color, target)

def scale_image(image, magnifier:float):
    width = image.get_width()
    height = image.get_height()

    return pygame.transform.scale(
        image,
        (
            int(width * magnifier),
            int(height * magnifier)
        )
    )