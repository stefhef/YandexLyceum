class Cinema(list):

    def __init__(self, name: str, *halls):
        super(Cinema, self).__init__(halls)
        self.name = name.capitalize()

    def __str__(self):
        return f'{self.name}' \
               f'Halls: {super(Cinema, self).__str__()}'

    def add_halls(self, *halls) -> None:
        """
        Добавляет залы в кинотеатр
        :param halls:
        :return:
        """
        for hall in halls:
            self.append(hall)
        # map(lambda x: self.append(x), halls)

    def remove_last_hall(self) -> None:
        """
        Удаляет последний зал из кинотеатра
        :return:
        """
        self.pop()

    def remove_hall(self, count=1) -> None:
        """
        Удаляет нужное количество залов из кинотеатра начиная с конца
        :param count:
        :return:
        """
        for _ in range(count):
            self.pop()


class Hall(list):

    def __init__(self, name: str, *chairs):
        super(Hall, self).__init__(chairs)
        self.name = name.capitalize()


class Chair:

    def __init__(self, name, is_empty=True):
        self.name = name
        self.is_empty = is_empty

    def change_chair_busy(self) -> None:
        """

        :return:
        """

        self.is_empty = not self.is_empty


class Schedule(list):

    def __init__(self):
        super(Schedule, self).__init__()


c = Cinema('first', 123, 12, 1)
print(c)
print(c.pop())
c.add_halls(214, 215, 1254)
print(c)
