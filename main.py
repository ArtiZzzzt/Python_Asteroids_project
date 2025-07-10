import pygame
from constants import * 
from circleshape import *
from player import *

def main():
    pygame.init()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
      screen.fill(000)
      dt = clock.tick(60)/1000
      for objects in drawable:
         objects.draw(screen)
      updateable.update(dt)
      

      pygame.display.flip()

if __name__ == "__main__":
    main()
