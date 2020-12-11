from PIL import ImageFilter, Image


def image_size_fix(path):
    end_with = path[-3:]
    if end_with == 'peg':
        end_with = 'jpeg'
        dir_path = path[:-5]+f'_new.{end_with}'
    else:
        dir_path = path[:-4] + f'_new.{end_with}'
    size = (720, 480)
    img = Image.open(path)
    img.thumbnail(size)
    img.save(dir_path)
    return dir_path
