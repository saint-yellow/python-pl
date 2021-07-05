from typing import List


class Solution:
    def maxProductDifference(self, numbers: List[int]) -> int:
        return self.__method1(numbers)

    def __method1(self, numbers: List[int]) -> int:
        
        # 或者：
        # numbers = sorted(numbers)
        # return numbers[-1] * numbers[-2] - numbers[0] * numbers[1]

        numbers = sorted(numbers, reverse=True)
        return numbers[0] * numbers[1] - numbers[-1] * numbers[-2]
