from PIL import Image

im = Image.open('image.bmp')
x, y = im.size
x1, y1 = x // 4, y // 4
for j in range(0, y, y1):
    for i in range(0, x, x1):
        if i == x - x1 and j == y - y1:
            exit()
        new_image = im.crop((i, j, i + x1, j + y1))
        name1, name2 = i % (x1 - 1) + 1, j % (y1 - 1) + 1
        new_image.save(f'image{name2}{name1}.bmp')
