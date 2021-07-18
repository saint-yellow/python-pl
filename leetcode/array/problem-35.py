# LeetCode Problem Nr. 35: 搜索插入位置

from typing import List


class Solution:
    def searchInsert(self, numbers: List[int], target: int) -> int:
        return self.__method2(numbers, target)

    # 暴力解法
    def __method1(self, numbers: List[int], target: int) -> int:
        length = len(numbers)
        for i in range(length):
            if numbers[i] >= target:
                return i
        return length

    # 基于二分法的解法
    def __method2(self, numbers: List[int], target: int) -> int:
        left, right = 0, len(numbers) - 1
        while left <= right:
            middle = (left + right) // 2
            if numbers[middle] > target:
                right = middle - 1
            elif numbers[middle] < target:
                left = middle + 1
            else:
                return middle
        return right + 1
