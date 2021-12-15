from copy import deepcopy
from functools import total_ordering


PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
N = 7
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


@total_ordering
class Note:

    def __init__(self, note, is_long=False):
        self.n0 = note
        if is_long:
            self.n = LONG_PITCHES[PITCHES.index(note)]
        else:
            self.n = note
        self.is_long = is_long

    def __str__(self):
        return self.n

    def __eq__(self, other):
        return self.n0 == other.n0

    def __lt__(self, other):
        return PITCHES.index(self.n0) < PITCHES.index(other.n0)

    def __rshift__(self, number):
        return Note(PITCHES[((PITCHES.index(self.n0) + number) % 7)], self.is_long)

    def __lshift__(self, number):
        ind = PITCHES.index(self.n0) - number
        ind %= N
        return Note(PITCHES[ind], self.is_long)

    def get_interval(self, other):
        interval_index = abs(PITCHES.index(self.n0) - PITCHES.index(other.n0))
        return INTERVALS[interval_index]


class Melody(list):
    def __str__(self):
        if self:
            return ", ".join(map(str, self)).capitalize()
        return ''

    def replace_last(self, note):
        self.pop()
        self.append(note)

    def remove_last(self):
        self.pop()

    def __lshift__(self, other):
        index_list = list(map(lambda x: PITCHES.index(x.n0) - other, self))
        if all(map(lambda x: x >= 0, index_list)):
            return Melody([Note(PITCHES[i], n.is_long) for i, n in zip(index_list, self)])
        return deepcopy(self)

    def __rshift__(self, other):
        index_list = list(map(lambda x: PITCHES.index(x.n0) + other, self))
        if all(map(lambda x: x <= 6, index_list)):
            return Melody([Note(PITCHES[i], n.is_long) for i, n in zip(index_list, self)])
        return deepcopy(self)


if __name__ == '__main__':
    melody = Melody([Note('ля'), Note('соль'), Note('ми'), Note('до', True)])
    print(melody)
    print(Melody() >> 2)
    melody_up = melody >> 1
    melody_down = melody << 1
    melody.replace_last(Note('соль'))
    print('>> 1:', melody_up)
    print('<< 1:', melody_down)
    print(melody)
