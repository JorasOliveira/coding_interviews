class Stack:
    def __init__(self):
        # Your subclass must not access this attribute
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)


class StackWithMin(Stack):
     # Create whatever methods you need
    def __init__(self):
        super().__init__()
        self._min_item = []

    def push(self, value):
        if not self._min_item or value <= self._min_item[-1]:
            self._min_item.append(value)
        super().push(value)

    def pop(self):
        value = super().pop()
        if value == self._min_item[-1]:
            self._min_item.pop()
        return value

    def minimum(self):
        if not self._min_item:
            return None
        return self._min_item[-1]
