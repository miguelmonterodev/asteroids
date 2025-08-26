# Asteroids
## Introduction
Build an Asteroids Game. We're going to build a simple video game, based on the classic [Asteroids](https://en.wikipedia.org/wiki/Asteroids_(video_game)). If you've never played before, you can take a look at this (slightly different from our) [version of the game](https://www.echalk.co.uk/amusements/Games/asteroidsClassic/ateroids.html).

## Prerequisites
- Python 3.10+ installed
- [uv](https://docs.astral.sh/uv/getting-started/installation/) project and package manager
- Access to a unix-like shell (e.g. zsh or bash)

## Why this project?
Because of learning goals such as:
- Multi-file Python projects
- Real-world use case for object-oriented programming
- Have fun building a program
Because this project is part of the [Boot.dev](https://boot.dev) Backend development course.

## Installation
We are going to be using pygame and a virtual environment to develop our game.
### Pygame
Pygame is a module for developing games using Python. It provides simple functions and methods for us to easily draw images within a GUI window and handle user input.
[Pygame documentation](https://www.pygame.org/docs/ref/pygame.html)
### Virtual Environment
Virtual environments are Python's way to keep dependencies (e.g. the pygame module) separate from other projects on our machine. For example, we need pygame version 2 for this project, but another project on your computer might require version 1.

As a best practice, each Python project on your machine should have its own virtual environment to keep them isolated from each other.

Create a new uv project:
```bash
uv init your-project-name
cd your-project-name
```
Create a virtual environment and activate:
```bash
uv venv
source .venv/bin/activate
```
Add the pygame library and make sure pygame is installed:
```bash
uv add pygame==2.6.1
uv run -m pygame  # exit code of 1, but the output will show that pygame is installed.
```
## Running the program
Run the program with uv:
```bash
uv run main.py
```
## Game Loop
Video games are generally built using a game loop. The simplest game loop has 3 steps:
- Check for player inputs
- Update the game world
- Draw the game to the screen

### Initialize Pygame
```python
import pygame

pygame.init()  # Initialize all imported pygame modules
```
### Get a new GUI window
```python
# pygame.display.set_mode()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# game loop
while True:
        # Check if the user has closed the window and exit the game loop 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        pygame.display.flip() # Refresh the screen
```
