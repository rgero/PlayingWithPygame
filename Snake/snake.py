import pygame
from pygame import display, event, image

import game_config as gc
from Block import *

class SnakeGame:
  def __init__(self):
    self.currentlyRunning = True
    pygame.init()
    self.clock = pygame.time.Clock()
    self.screen = display.set_mode( (gc.SCREEN_WIDTH, gc.SCREEN_HEIGHT) )
    self.screen.fill(gc.white)
    display.set_caption("SNAAAAAAAAAAAAAAAAAKE")
    self.playerBlock = Block(self.screen, gc.red, 10,10,10,10);

  def run(self):
    display.update()
    while self.currentlyRunning:
        currentEvents = event.get() # This gets you the list of events that have happened since the last time you got them.
        for e in currentEvents:
            if e.type is pygame.QUIT:
                self.currentlyRunning = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.playerBlock.changeDirection(gc.Direction.UP)
                if e.key == pygame.K_DOWN:
                    self.playerBlock.changeDirection(gc.Direction.DOWN)
                if e.key == pygame.K_LEFT:
                    self.playerBlock.changeDirection(gc.Direction.LEFT)
                if e.key == pygame.K_RIGHT:
                    self.playerBlock.changeDirection(gc.Direction.RIGHT)
        self.screen.fill(gc.white);
        self.playerBlock.move()
        display.update()
        self.clock.tick(30)
    pygame.quit();


SnakeGame().run()


