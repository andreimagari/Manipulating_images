#!/usr/bin/python3
from PIL import Image
import os, sys

path = "/home/testpc/Images/"
dirs = os.listdir( path )
new_path = "/home/testpc/Images_new/"

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.rotate(90).resize((128,128), Image.ANTIALIAS)
            imResize.save(new_path + item, 'JPEG', quality=90)
resize()
