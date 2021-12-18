x1, y1, w1, h1 = tuple(map(int, input().split()))
x11 = x1 + w1
y11 = y1 + h1
x2, y2, w2, h2 = tuple(map(int, input().split()))
x21 = x2 + w2
y21 = y2 + h2
if x2 < x1 < x21:
    print('YES')
else:
    print('NO')
