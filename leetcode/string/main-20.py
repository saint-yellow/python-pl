# LeetCode Problem Nr. 20: 有效的括号

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
                if stack and stack[-1] == mapping[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return stack == []


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
