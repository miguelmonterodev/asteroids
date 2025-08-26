import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # 60 FPS calling the tick() passing 1/60th seconds
    pygame.time.Clock()
    dt = 0
    # Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # Game Loop
    while True:
        # Check if the user has closed the window and exit the game loop 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Update rotation
        player.update(dt)
        screen.fill("black") # fill screen with black
        player.draw(screen) # draw player in white 
        pygame.display.flip() # Refresh the screen

        dt = pygame.time.Clock().tick(60) / 1000  # Delta time
        

if __name__ == "__main__":
    main()
