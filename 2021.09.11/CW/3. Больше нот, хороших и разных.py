PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    note_d = {
        'до': 'до-о',
        'ре': 'ре-э',
        'ми': 'ми-и',
        'фа': 'фа-а',
        'соль': 'со-оль',
        'ля': 'ля-а',
        'си': 'си-и'
    }

    def __init__(self, note, is_long=False):
        self.nt = note
        self.is_long = is_long

    def __str__(self):
        if self.is_long:
            return self.note_d.get(self.nt)
        return self.nt


class LoudNote(Note):

    def __init__(self, nt, is_long=False):
        super(LoudNote, self).__init__(nt, is_long)

    def __str__(self):
        if self.is_long:
            return self.note_d.get(self.nt).upper()
        return self.nt.upper()


class DefaultNote(Note):

    def __init__(self, note='до', is_long=False):
        super().__init__(note, is_long)


class NoteWithOctave(DefaultNote, LoudNote, Note):

    def __init__(self, note, octave, is_long=False):
        super().__init__(note, is_long)
        self.octave = octave

    def __str__(self):
        if self.is_long:
            return f'{self.note_d.get(self.nt)} ({self.octave})'
        return f'{self.nt} ({self.octave})'
