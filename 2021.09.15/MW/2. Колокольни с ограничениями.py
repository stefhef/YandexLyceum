import inspect


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


class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print('...')

    def append(self, bell):
        self.bells.append(bell)

    def print_info(self):
        for number, bell in enumerate(self.bells, start=1):
            bell: Bell
            print(f'{number} {bell}')
            bell.print_info()
        print()


class LittleBell(Bell):
    def sound(self):
        print('ding')

    def __str__(self):
        return 'LittleBell'


class BigBell(Bell):
    count = 0

    def sound(self):
        if self.count % 2 == 0:
            print('ding')
        elif self.count % 2 != 0:
            print('dong')
        self.count += 1

    def __str__(self):
        return 'BigBell'


class SizedBellTower(BellTower):

    def __init__(self, *bells, size=10):
        # if params:
        #     self.size = params.get('size')
        # else:
        #     self.size = 10

        self.size = size

        super().__init__(*bells)
        self.remove_excess_bell()

    def remove_excess_bell(self):
        if len(self.bells) > self.size:
            self.bells = self.bells[-self.size:]

    def append(self, bell):
        super(SizedBellTower, self).append(bell)
        self.remove_excess_bell()


class TypedBellTower(BellTower):

    def __init__(self, *bells, bell_type=LittleBell):
        super().__init__()
        self.bells = []
        self.type = bell_type
        # if params:
        #     self.type = params.get('bell_type')
        # else:
        #     self.type = LittleBell
        for bell in bells:
            self.append(bell)

    def append(self, bell):
        if bell.__class__ == self.type:
            super(TypedBellTower, self).append(bell)


if __name__ == '__main__':
    sbt = SizedBellTower(BigBell("бронзовый"),
                         LittleBell("медный", нота="ля"),
                         BigBell(название="Корноухий", вес="1275 пудов"),
                         size=2)
    sbt.print_info()
    sbt.append(BigBell("самый звонкий"))
    sbt.print_info()
