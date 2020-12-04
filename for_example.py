from PIL import Image, ImageFilter

try:
    img = Image.open(r'images/broly.jpg')
    print(img.size)
except FileNotFoundError:
    print('file not found check file path')
blurred = img.filter(ImageFilter.BLUR)
img.show()
blurred.show()