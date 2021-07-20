# LeetCode Problem Nr. 155: 最小栈


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, val: int) -> None:
        if not self.data:
            self.data.append((val, val))
        else:
            self.data.append((val, min(val, self.data[-1][1])))

    def pop(self) -> None:
        if self.data:
            self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]
