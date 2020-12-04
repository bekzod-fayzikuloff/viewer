from PIL import ImageFilter, Image


def image_size_fix(path):
    dir_path = path[:-5]+'_new.jpg'
    size = (720, 480)
    img = Image.open(path)
    img.thumbnail(size)
    img.save(dir_path)
    return dir_path
