with open('pipes.txt', 'r') as f:
    lst = []
    lines = f.readlines()
    for number, line in enumerate(lines):
        line = line.strip()
        if not line:
            break
        hour = float(line)
        if hour:
            lst.append((number, 1 / hour / 60))
    number_pipes = tuple(map(lambda x: int(x) - 1, lines[-1].strip().split()))
    speed = 0
    for number, spd in lst:
        if number in number_pipes:
            speed += spd

with open('time.txt', 'w') as f:
    print(1 / speed, file=f)
