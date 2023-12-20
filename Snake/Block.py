import pygame
import game_config as gc

class Block:
    def __init__(self, screen, color, initialX, initialY, width, height):
        self.color = color
        self.screen = screen
        self.x = initialX
        self.y = initialY
        self.maxX, self.maxY = pygame.display.get_surface().get_size()
        self.width = width
        self.height = height
        self.change = (0,0)

    def draw(self):
        return pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    
    def changeDirection(self, direction):
        if direction is gc.Direction.UP:
            self.change = (0, 1)
        if direction is gc.Direction.DOWN:
            self.change = (0, -1)
        if direction is gc.Direction.LEFT:
            self.change = (-1,0)
        if direction is gc.Direction.RIGHT:
            self.change = (1,0)
    
    def move(self):
        if self.change[1] == 1 and self.y >= self.height:
            self.y -= self.height
        if self.change[1] == -1 and self.y < self.screen.get_size()[1] - self.height:
            self.y += self.height
        if self.change[0] == 1 and self.x < self.screen.get_size()[0] - self.width:
            self.x += self.width
        if self.change[0] == -1 and self.x >= self.width:
            self.x -= self.width
        self.draw()