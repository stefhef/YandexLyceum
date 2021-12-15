from PIL import Image

im = Image.open('../image.png')
pixels = im.load()
background_color = pixels[0, 0]
x_size, y_size = im.size
left, up = x_size - 1, y_size - 1
down = right = 0
for x in range(x_size):
    for y in range(y_size):
        if pixels[x, y] != background_color:
            if up > y:
                up = y
            if down < y:
                down = y
            if left > x:
                left = x
            if right < x:
                right = x

new_image = im.crop((left, up, right + 1, down + 1))
new_image.save('res.png')
