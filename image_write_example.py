"""
Sample code to show how to create an image by
coloring in each pixel manually!  This is by making a
formula to generate a color value base on each pixel position

This uses Python Image Library (PIL/pillow)

Ref
https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels
"""
import os
from PIL import Image

# init the image size (note: they don't need to be the same)
# TODO: try changing these
IMG_X_SIZE = 512
IMG_Y_SIZE = 512
IMG_SIZE_TUPLE = (IMG_X_SIZE, IMG_Y_SIZE)

def pick_pixel_color(x,y):
    red_intensity = 0
    # red_intensity = 255 if y % 25 in range(12) else 0
    # green_intensity = int( (x+y) / 4)
    # TODO: try setting the green intensity to one of these (and try your own)
    # green_intensity = 255 if y > 255 else y
    # blue_intensity = int( (x+y) / 4)
    # green_intensity = int(x / 2) % 256
    # blue_intensity = int(x / 2) % 256
    green_intensity =  int((1024-(x+y))/4) % 256
    # green_intensity = int(x+ 2*y) % 256
    # green_intensity = 0
    blue_intensity = 0
    # blue_intensity = 255 if x % 25 in range(12) else 0
    color = (red_intensity, green_intensity, blue_intensity)

    return color

# Set the dir and filename stuff
my_dir = os.path.dirname(os.path.realpath(__file__))
ofname = 'output_image.png'
full_ofname = my_dir + '/' + ofname

# Initialize the image as an RGB (24bit color) image
# and init the pixel from that image
my_image = Image.new('RGB', IMG_SIZE_TUPLE)
my_pixels = my_image.load()

# Get the image dimension so we can iterate over it
image_x_size = my_image.size[0]
image_y_size = my_image.size[1]

# iterate over all the pixels
for y in range(image_y_size):
    for x in range(image_x_size):
        pixel_color = pick_pixel_color(x,y)
        my_pixels[x, y] = pixel_color

# save the image as a PNG file
my_image.save(full_ofname, 'png')
