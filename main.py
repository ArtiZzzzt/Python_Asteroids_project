import pygame
from constants import * 
from circleshape import *
from player import *

def main():
    pygame.init()
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
      player.draw(screen)
      player.update(dt)
      

      pygame.display.flip()

if __name__ == "__main__":
    main()
