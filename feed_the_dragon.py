import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Dragon")



FPS = 60
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0,0,0))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()