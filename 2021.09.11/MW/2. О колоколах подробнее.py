class Bell:
    def __init__(self, *other, **other_name):
        self.other = other
        self.other_name = other_name

    def print_info(self):
        if not self.other and not self.other_name:
            print('-')
            return
        for num, (key, item) in enumerate(sorted(self.other_name.items())):
            print(f"{key}: {item}", end='')
            if num != len(self.other_name) - 1:
                print(', ', end='')
            elif num == len(self.other_name) - 1 and self.other:
                print('; ', end='')
        print(', '.join(self.other))


class BellTower(Bell):
    def __init__(self, *bells, **other_name):
        super().__init__(**other_name)
        self.bells = list(bells)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print('...')

    def append(self, bell):
        self.bells.append(bell)


class LittleBell(Bell):
    def sound(self):
        print('ding')


class BigBell(Bell):

    count = 0

    def sound(self):
        if self.count % 2 == 0:
            print('ding')
        elif self.count % 2 != 0:
            print('dong')
        self.count += 1


if __name__ == '__main__':
    BigBell("крупнейший в мире действующий колокол", название="Bell of Good Luck",
            высота="810,8 см", диаметр="511,8 см", вес="116 тонн").print_info()
    LittleBell().print_info()
