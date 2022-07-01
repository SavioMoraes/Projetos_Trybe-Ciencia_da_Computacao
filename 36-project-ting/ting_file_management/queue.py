class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return not len(self._data)

    def __str__(self):
        return (
            "Deque(" + ", ".join(str(x) for x in self._data) + ")"
        )

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self._data:
            return self._data.pop(self.FIRST_ELEMENT)
        return None

    def search(self, index):
        if index < 0 or index > len(self._data) - 1:
            raise IndexError()
        else:
            return self._data[index]
