def reverse():
    with open('input.dat', 'rb') as input_file, \
            open('output.dat', 'wb') as output_file:
        output_file.write(input_file.read()[::-1])
