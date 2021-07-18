# 剑指Offer Problem Nr. 53-I: 0～n-1中缺失的数字

from typing import List


class Solution:
    def missingNumber(self, numbers: List[int]) -> int:
        return self.__method1(numbers)

    def __method1(self, numbers: List[int]) -> int:
        sum1 = sum(numbers)
        sum2 = sum(range(len(numbers) + 1))
        return sum2 - sum1
