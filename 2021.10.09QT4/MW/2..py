print('          00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f', end='\n\n')
# text = 'Bill Gates: Sorry about Control-Alt-Delete  '[-2:]
text = ''
with open('data.txt', 'rb') as f:
    count = 16
    c = 0
    c1 = 1
    out = ''
    print('000000', end='    ')
    for b in f.read():
        if c == count:
            c = 0
            print(f'{out}    {text}')
            text = ''
            out = ''
            print(hex(c1).replace('x', "0").rjust(5, '0') + '0', end='    ')
            c1 += 1
        out += f'{hex(b)[-2:].replace("x", "0")} '
        c += 1
        ch = chr(b)
        if ch.isprintable():
            text += chr(b)
        else:
            text += '.'
    if out:
        print(f'{out.ljust(48, " ")}    {text}')

