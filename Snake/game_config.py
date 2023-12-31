import os
from enum import Enum

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

# colors
red = (128,0,0)
black = (0,0,0)
white = (255,255,255)

Direction = Enum('Direction', ['UP', 'DOWN', 'LEFT', 'RIGHT'])