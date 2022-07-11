class CyclicIterator:
    def __init__(self, iterable_data):
        self.start_container = iterable_data
        self.container = None
        self.__restart__()

    def __restart__(self):
        self.container = iter(self.start_container)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.container)
        except StopIteration:
            self.__restart__()
            return next(self.container)
