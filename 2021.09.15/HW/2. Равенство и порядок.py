from functools import total_ordering


@total_ordering
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

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)


if __name__ == "__main__":
    points = [Point('A', 101, 1), Point('B', -1, 0),
              Point('A', 11, 0), Point('A', 111, -11)]
    points.sort()
    print(', '.join(map(str, points)))

