import os, random
import game_config as gc

from pygame import image, transform

animals_count = dict((a, 0) for a in gc.ASSET_FILES)

def available_animals():
  return [animal for animal, count in animals_count.items() if count < 2]

class Animal:
  def __init__(self, index):
    self.index = index
    self.row = index // gc.NUM_TILES_PER_ROW
    self.col = index % gc.NUM_TILES_PER_ROW
    self.name = random.choice(available_animals())
    animals_count[self.name] += 1

    self.image_path = os.path.join(gc.ASSET_DIR, self.name)
    self.image = image.load(self.image_path)

    # Scale the image
    targetImageSize = gc.IMAGE_SIZE - 2*gc.MARGIN
    self.image = transform.scale(self.image, (targetImageSize, targetImageSize))

    # Create the box that hides the image
    self.box = self.image.copy()
    self.box = self.image.copy()
    self.box.fill((200, 200, 200))
    
    # When this is set to true, this will be skipped.
    self.skip = False