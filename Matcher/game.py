import pygame
from pygame import display, event, image

import game_config as gc
from Animal import Animal

# This has to be first, it initializes everything
pygame.init()

# Sets the title
display.set_caption("Roy's Awesome Matching Game")

# Displays the screen. The resolution has to be a tuple
screen = display.set_mode( (gc.SCREEN_WIDTH, gc.SCREEN_HEIGHT) )

# Load Assets
matched = image.load('other_assets/matched.png')

# The current status of the application.
currentlyRunning = True

tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]

# Game Loop
while currentlyRunning:
  currentEvents = event.get() # This gets you the list of events that have happened since the last time you got them.
  
  # Iterate over the game loops
  for e in currentEvents:
    if e.type is pygame.QUIT:
      currentlyRunning = False

  # Display the animal tiles
  screen.fill((250,250,250))

  for tile in tiles:
    targetX = tile.col * gc.IMAGE_SIZE + gc.MARGIN;
    targetY = tile.row * gc.IMAGE_SIZE + gc.MARGIN;
    screen.blit(tile.image, (targetX, targetY))

  display.flip()

print("Successfully Quit");
