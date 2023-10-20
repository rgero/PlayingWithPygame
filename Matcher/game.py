import pygame
from pygame import display, event

# This has to be first, it initializes everything
pygame.init()

# Sets the title
display.set_caption("Roy's Awesome Matching Game")

# Displays the screen. The resolution has to be a tuple
screen = display.set_mode( (1080,720) )

# The current status of the application.
currentlyRunning = True

# Game Loop
while currentlyRunning:
  currentEvents = event.get() # This gets you the list of events that have happened since the last time you got them.
  
  # Iterate over the game loops
  for e in currentEvents:
    if e.type is pygame.QUIT:
      currentlyRunning = False

print("Successfully Quit");
