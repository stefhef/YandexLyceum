points = []

for _ in range(int(input())):
    x, y = list(map(int, input().strip().split()))
    if _ == 0:
        left = right = top = bottom = (x, y)

    if abs(y) < abs(x):
        points.append((x, y))
    if left[0] > x:
        left = (x, y)
    if right[0] < x:
        right = (x, y)
    if top[1] < y:
        top = (x, y)
    if bottom[1] > y:
        bottom = (x, y)

for point in points:
    print(point)

print(f"""left: {left}
right: {right}
top: {top}
bottom: {bottom}""")
