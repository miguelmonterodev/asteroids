import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # 60 FPS calling the tick() passing 1/60th seconds
    pygame.time.Clock()
    dt = 0
    # Creating Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Every instance of the class is added to these groups upon creation
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable) 
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    # Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # AsteroidField
    asteroid_field = AsteroidField()
    # Game Loop
    while True:
        # Check if the user has closed the window and exit the game loop 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Update rotation
        updatable.update(dt)
        # Check Collisions player-asteroid
        for obj in asteroid:
            if obj.check_collision(player):
                print("Game over!")
                sys.exit(1)
        # Check Collisions bullet-asteroid and Destroy using .kill() method
        for shot in shots:
            for obj in asteroid:
                if obj.check_collision(shot):
                    obj.split()
                    shot.kill()
        # fill screen with black
        screen.fill("black") 
        # player.draw(screen) # draw player in white
        for obj in drawable:
            obj.draw(screen) 
        pygame.display.flip() # Refresh the screen

        dt = pygame.time.Clock().tick(60) / 1000  # Delta time
        

if __name__ == "__main__":
    main()
