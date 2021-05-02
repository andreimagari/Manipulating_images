#!/usr/bin/python3
from PIL import Image
import os, sys

path = "/home/testpc/Images/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.rotate(90).resize((128,128), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)
resize()
