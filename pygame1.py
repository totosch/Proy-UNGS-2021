import pygame, sys
from pygame.locals import *

pygame.init()
visor = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Typing of the dead")

pygame.display.flip()
relleno = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_ESCAPE]):
        pygame.quit()
        sys.exit()
    if keys[K_l]:
        visor =
    pygame.display.set_mode((640,480),0,32)
    
        