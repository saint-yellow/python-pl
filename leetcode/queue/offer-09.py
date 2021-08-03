# 剑指Offer Problem Nr. 09: 用栈实现队列

from typing import List


class CQueue:
    def __init__(self):
        self.input_stack: List[int] = []
        self.output_stack: List[int] = []

    def appendTail(self, value: int) -> None:
        self.input_stack.append(value)

    def deleteHead(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        if self.output_stack == []:
            return -1
        else:
            return self.output_stack.pop()
