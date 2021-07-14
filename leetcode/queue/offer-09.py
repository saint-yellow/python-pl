# 剑指Offer Problem Nr. 09: 用栈实现队列

class CQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []


    def appendTail(self, value: int) -> None:
        self.input_stack.append(value)


    def deleteHead(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        try:
            return self.output_stack.pop()
        except:
            return -1
