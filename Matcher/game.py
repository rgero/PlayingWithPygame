import pygame
from pygame import display, event, image

import game_config as gc
from Animal import Animal
from time import sleep

def find_index(x,y):
  row = y // gc.IMAGE_SIZE
  col = x // gc.IMAGE_SIZE
  return int(row * gc.NUM_TILES_PER_ROW + col)

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
current_images=[]

# Game Loop
while currentlyRunning:
  currentEvents = event.get() # This gets you the list of events that have happened since the last time you got them.
  
  # Iterate over the game loops
  for e in currentEvents:
    if e.type is pygame.QUIT:
      currentlyRunning = False

    # If the Escape key is pressed, close the game.
    if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_ESCAPE:
        currentlyRunning = False

    if e.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      index = find_index(mouse_x, mouse_y)
      if index not in current_images:
        current_images.append(index)
      if len(current_images) > 2:
        current_images = current_images[1:]

  # Display the animal tiles
  screen.fill((250,250,250))

  for _, tile in enumerate(tiles):
    image_i = tile.image if tile.index in current_images else tile.box
    if not tile.skip:
      targetX = tile.col * gc.IMAGE_SIZE + gc.MARGIN;
      targetY = tile.row * gc.IMAGE_SIZE + gc.MARGIN;
      screen.blit(image_i, (targetX, targetY))

  display.flip()

  # Check if they are the same
  if len(current_images) == 2:
    ix1, ix2 = current_images
    if tiles[ix1].name == tiles[ix2].name:
      tiles[ix1].skip = True
      tiles[ix2].skip = True
      sleep(0.6)
      screen.blit(matched, (0,0))
      display.flip()
      sleep(0.4)
      current_images = []

print("Successfully Quit");
