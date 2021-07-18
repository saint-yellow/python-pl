# Interview Problem Nr. 08.06: 汉诺塔问题

from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        self.__method1(A, B, C)

    def __method1(self, A: List[int], B: List[int], C: List[int]) -> None:
        n = len(A)
        self.__move(n, A, B, C)

    def __move(self, n: int, start: List[int], middle: List[int], end: List[int]):
        if n == 1:
            end.append(start[-1])
            start.pop()
            return
        else:
            self.__move(n - 1, start, end, middle)
            end.append(start[-1])
            start.pop()
            self.__move(n - 1, middle, start, end)


if __name__ == "__main__":
    A, B, C = [2, 1, 0], [], []
    s = Solution()
    s.hanota(A, B, C)
    print(C)
