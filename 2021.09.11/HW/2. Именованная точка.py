class Point:

    def __init__(self, name: str, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.name = name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return (self.x, self.y)

    def __str__(self):
        return f"{self.name}{(self.x, self.y)}"

    def __invert__(self):
        return Point(self.name, self.y, self.x)


if __name__ == '__main__':
    point_A = Point('A', 3, -4)
    print(point_A)
    point_B = ~point_A
    print(point_B)
    print(~Point('O', 0, 0))
