# LeetCode Problem Nr. 946: 模拟栈序列

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        return self.__method1(pushed, popped)

    def __method1(self, pushed: List[int], popped: List[int]) -> bool:
        stack: List[int] = []
        j = 0
        n = len(popped)

        for u in pushed:
            stack.append(u)
            while stack and j < n and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == n 


if __name__ == "__main__":
    s = Solution()
    print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
