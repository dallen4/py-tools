# Resize images while preserving aspect ratio & quality

import os
import PIL
from PIL import Image

basewidth = 1920

for filename in os.listdir("."):
    if not filename.startswith('.'): #ignores hidden file .DS_Store
        img = Image.open(filename)
        print('Testing size of '+ filename + '...')
        if img.size[0] > 1920:
            print(filename + ' is too large, calculating dimensions & resizing...')
            widthRatio = (basewidth / float(img.size[0]))
            hSize = int((float(img.size[1]) * float(widthRatio)))
            img = img.resize((basewidth, hSize), PIL.Image.ANTIALIAS)
            img.save(filename)
