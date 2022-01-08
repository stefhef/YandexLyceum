class DefaultList(list):

    def __init__(self, default, *args):
        super(DefaultList, self).__init__(*args)
        self.default = default

    def __getitem__(self, ind):
        try:
            return super(DefaultList, self).__getitem__(ind)
        except IndexError:
            return self.default
