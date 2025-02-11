import sys

from PIL import Image

images = []

# iterate over command line arguments then append it 
# 1: is a slice = start at one index and give all the way to the end
# sys.argv includes file name so don't want to include therefore slice
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
    
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)