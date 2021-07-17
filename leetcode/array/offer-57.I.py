# 剑指Offer Problem Nr. 57: 和为s的两个数字

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.__method1(numbers, target)

    def __method1(self, numbers, target) -> List[int]:
        if not numbers:
            return [-1, -1]

        left, right = 0, len(numbers) - 1
        while left <= right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [numbers[left], numbers[right]]
            elif total > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]
