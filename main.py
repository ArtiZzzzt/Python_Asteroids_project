import sys
import pygame
from constants import * 
from player import *
from asteroid import Asteroid
from AsteroidField import AsteroidField

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)


    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    dt = 0

    while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()
         
      updateable.update(dt)

      screen.fill(000)
      
      for objects in drawable:
         objects.draw(screen)

      for asteroid in asteroids:
         if asteroid.check_collision(player):
            print("Game over!")
            sys.exit()
      
      for asteroid in asteroids:
         for shot in shots:
            if shot.check_collision(asteroid):
               shot.kill()
               asteroid.split()
         
      

      pygame.display.flip()

      dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
