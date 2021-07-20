class Solution:
    def isValid(self, s: str) -> bool:
        return self.__method1(s)

    def __method1(self, s: str) -> bool:
        mapping = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        stack = []

        for i in s:
            if i in mapping.keys():
                stack.append(i)
            elif stack and stack[-1] == mapping[i]:
                stack.pop()
            else:
                return False

        return stack == []