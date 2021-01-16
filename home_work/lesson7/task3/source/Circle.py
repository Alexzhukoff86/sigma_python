class Circle:

    def __init__(self, sequence, max_times):
        self.sequence = sequence
        self.max_time = max_times
        self.count = 0
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_time:
            result = self.sequence[self.index]
            if self.index >= len(self.sequence)-1:
                self.index = 0
            else:
                self.index += 1
            self.count += 1
            return result
        else:
            raise StopIteration
