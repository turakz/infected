# std
import os

# 3rd
import pygame
from pygame._sdl2 import Window

# local

os.environ['SDL_VIDEO_CENTERED'] = "1"

pygame.init()

# main window
main_display_info = pygame.display.Info()
main_window_width, main_window_height = main_display_info.current_w, main_display_info.current_h
main_window_size = tuple([main_window_width, main_window_height])
main_window_surface = pygame.display.set_mode(main_window_size, pygame.RESIZABLE)
Window.from_display_module().maximize()
main_window_surface.fill(pygame.color.THECOLORS["darkslategray"])

# window loop
clock = pygame.time.Clock()
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    # Render the graphics here.
    # ...
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
