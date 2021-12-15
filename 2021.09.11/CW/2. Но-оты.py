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

    def __init__(self, note, duration=False):
        self.nt = note
        self.dur = duration

    def __str__(self):
        if self.dur:
            return self.note_d.get(self.nt)
        return self.nt
