class RingBuffer:
    def __init__(self, capacity):
        pass
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.index] = item
        else:
            self.storage.append(item)
            self.index = (self.index + 1) % self.capacity

    def get(self):
        #return full array
        return self.storage