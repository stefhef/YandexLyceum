with open('prices.txt') as f:
    text = f.readlines()
    if text:
        out = sum(map(lambda x: int(x[1]) * float(x[2]), [elem.strip().split() for elem in text]))
    else:
        out = 0.00
    out = str(round(out, 2)).split('.')
    out = out[0] + '.' + out[1].ljust(2, '0')
    print(out)
