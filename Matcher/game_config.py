import os

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

NUM_TILES_PER_ROW = 4
NUM_TILES_TOTAL = 16

IMAGE_SIZE = SCREEN_WIDTH / NUM_TILES_PER_ROW

# Gap between two images
MARGIN = 4

ASSET_DIR = 'assets'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']

# Safety Checks
assert len(ASSET_FILES) == 8
