from typing import List


class Solution:
    def pivotIndex(self, numbers: List[int]) -> int:
        return self.__method1(numbers)


    def __method1(self, numbers: List[int]) -> int:
        total = sum(numbers)
        leftSum = 0
        for i in range(len(numbers)):
            if numbers[i] + 2 * leftSum == total:
                return i
            leftSum += numbers[i]
        return -1
