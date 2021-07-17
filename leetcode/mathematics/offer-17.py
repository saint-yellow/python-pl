# 剑指Offer Problem Nr. 17: 打印从1到最大的n位数

from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return self.__method1(n)

    def __method1(self, n: int) -> list[int]:
        return list(range(1, 10**n))
