with open('input.bmp', 'rb') as img_in, open('res.bmp', 'wb') as output_file:
    data = img_in.read()
    new_palette = data[:54] + bytes([255 - b for b in data[54:]])
    output_file.write(new_palette)
