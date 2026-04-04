class MinStack:

    def __init__(self):
        self.data = []
        self.minimum = []

    def push(self, val: int) -> None:
        if self.minimum:
            self.minimum.append(min(val, self.minimum[-1]))
        else:
            self.minimum.append(val)
        self.data.append(val)

    def pop(self) -> None:
        self.minimum.pop()
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
