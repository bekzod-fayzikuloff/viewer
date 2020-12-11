from PIL import Image, ImageFilter
import os
import sys
"""
try:
    size = (720, 480)
    img = Image.open(r'ico/L.png')
    img.thumbnail(size)
    img.save('ico/L.ico')
except FileNotFoundError:
    print('file not found check file path')"""


def resource_path(relative):

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)

print(resource_path('ico\\78.jpg'))
