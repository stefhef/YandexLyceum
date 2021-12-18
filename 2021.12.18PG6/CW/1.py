x1, y1, r1 = tuple(map(int, input().split()))
x2, y2, r2 = tuple(map(int, input().split()))
if ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 <= r1 + r2:
    print('YES')
else:
    print('NO')
