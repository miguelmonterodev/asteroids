import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        # Check if the user has closed the window and exit the game loop 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Game Loop
        screen.fill("black")
        pygame.display.flip() # Refresh the screen


if __name__ == "__main__":
    main()
