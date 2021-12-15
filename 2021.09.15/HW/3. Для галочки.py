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
        return self.x, self.y

    # def check_one_line(self, p2):
    # return True if self.y == p2.y else False

    def __str__(self):
        return self.name

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)


class CheckMark:

    def __init__(self, *points):
        self.p1, self.p2, self.p3 = points
        self.points = points

    def __str__(self):
        return ''.join(map(str, self.points))

    def __bool__(self):
        return False if (self.p3.x * (self.p2.y - self.p1.y) - self.p3.y * (
                    self.p2.x - self.p1.x) == self.p1.x * self.p2.y - self.p2.x * self.p1.y) else True

    def __eq__(self, other):
        return True if self.p1 in other.points and self.p2 == other.p2 and self.p3 in other.points else False


if __name__ == "__main__":
    A1 = Point('P1', -30, 20)
    A2 = Point('P2', -10, -10)
    A3 = Point('P3', -20, -30)
    A4 = Point('P4', 20, -30)
    A5 = Point('P5', 30, 20)
    A6 = Point('P6', 10, 10)
    A7 = Point('P7', 30, 30)

    cm_a = CheckMark(A1, A2, A3)
    cm_b = CheckMark(A3, A2, A4)
    cm_c = CheckMark(A3, A2, A7)
    cm_d = CheckMark(A4, A2, A3)
    cm_e = CheckMark(A2, A6, A7)
    cm_f = CheckMark(A7, A5, A6)
    cm_g = CheckMark(A1, A1, A6)
    cm_h = CheckMark(A4, A5, A4)
    cm_i = CheckMark(A3, A3, A3)

    print(bool(cm_a))
    print(bool(cm_b))
    print(bool(cm_c))
    print(bool(cm_d))
    print(bool(cm_e))
    print(bool(cm_f))
    print(bool(cm_g))
    print(bool(cm_h))
    print(bool(cm_i))
