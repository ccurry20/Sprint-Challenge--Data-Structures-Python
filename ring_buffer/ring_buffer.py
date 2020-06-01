class RingBuffer:
    def __init__(self, capacity):
        pass
        self.capacity = capacity
        self.storage = []
        self.index = 0
        
    def append(self, item):
     # If storage is empty add one
        if len(self.storage) == 0:
            self.storage.append(item)
        else:
            # If len of storage == capacity
            if len(self.storage) == self.capacity:
                # Check if the index is capacity
                if self.index == self.capacity:
                    # Zero out index
                    self.index = 0
                    # Add item into storage at index
                    self.storage[self.index] = item
                    # Increment index
                    self.index += 1
                # If index is not capacity
                else:
                    # Add item into storage at index
                    self.storage[self.index] = item
                    # Increment index
                    self.index += 1
            # Len of storage not capacity
            else:
                # Add into storage
                self.storage.append(item)
            

    def get(self):
        #return array
        return self.storage
     