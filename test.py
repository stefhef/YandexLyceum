def test(x0, x1):
    for i in range(x0, x1 + 1):
        yield i


numbers = test(1, 5)
for _ in range(20):
    print(next(numbers))
