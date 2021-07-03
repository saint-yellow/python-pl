from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return self.method1(tokens)

    def method1(self, tokens: List[str]) -> int:
        mapping = {
            "+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "*": lambda a, b: a*b,
            "/": lambda a, b: int(a/b),
        }

        stack = []

        for t in tokens:
            if t in mapping.keys():
                a = int(stack.pop())
                b = int(stack.pop())
                n = mapping[t](b, a)
                stack.append(n)
            else:
                stack.append(int(t))
                
        return stack[-1]
