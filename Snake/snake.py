import pygame
from pygame import display, event, image

import game_config as gc

# Initialize pygame
pygame.init()

screen = display.set_mode( (gc.SCREEN_WIDTH, gc.SCREEN_HEIGHT) )
display.set_caption("SNAAAAAAAAAAAAAAAAAKE")

currentlyRunning = True

screen.fill(gc.white)

while currentlyRunning:
  display.update()

  currentEvents = event.get() # This gets you the list of events that have happened since the last time you got them.
  for e in currentEvents:
    if e.type is pygame.QUIT:
      currentlyRunning = False

  # Draw stuff
  pygame.draw.rect(screen, gc.red, (300,200,10,10))

pygame.quit();