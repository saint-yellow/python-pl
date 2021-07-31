# LeetCode Problem Nr. 232: 用栈实现队列


from typing import List


class MyQueue:
    def __init__(self) -> None:
        self.input_stack: List[int] = []
        self.output_stack: List[int] = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()

    def peek(self) -> int:
        if self.output_stack:
            return self.output_stack[-1]
        else:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
            return self.output_stack[-1]

    def empty(self) -> bool:
        return not (self.input_stack or self.output_stack)
