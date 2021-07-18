from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.__method1(numbers, target)

    def __method1(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

    def __method2(self, numbers: List[int], target: int) -> int:
        n = len(numbers)
        for i in range(n):
            left, right = i, n - 1
            while left <= right:
                middle = (left + right) // 2
                if numbers[middle] == target - numbers[i]:
                    return [i + 1, middle + 1]
                elif numbers[middle] > target - numbers[i]:
                    right = middle - 1
                else:
                    left = middle + 1
        return [-1, -1]
