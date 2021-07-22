# 剑指Offer Problem Nr. 30: 包含min函数的栈

from typing import List, Union


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data: List[int] = []
        self.minValue: Union[int, None] = None


    def push(self, x: int) -> None:
        if not self.data:
            self.data.append(x)
            self.minValue = x
        else:
            self.minValue = min(self.minValue, x)
            self.data.append(x)


    def pop(self) -> None:
        if not self.data:
            return

        self.data.pop()

        if not self.data:
            self.minValue = None
        else:
            self.minValue = min(self.data)


    def top(self) -> Union[int, None]:
        if not self.data:
            return None
        return self.data[-1]


    def min(self) -> Union[int, None]:
        return self.minValue
