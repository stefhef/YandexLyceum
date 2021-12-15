class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print('...')

    def append(self, bell):
        self.bells.append(bell)


class LittleBell:
    def sound(self):
        print('ding')


class BigBell:

    def __init__(self):
        self.count = 0

    def sound(self):
        if self.count % 2 == 0:
            print('ding')
        elif self.count % 2 != 0:
            print('dong')
        self.count += 1


if __name__ == '__main__':
    bell_tower = BellTower()
    bell_tower.sound()
    bell_tower.append(BigBell())
    bell_tower.sound()
    bell_tower.append(BigBell())
    bell_tower.sound()