from typing import List


class Solution:
    def removeElement(self, numbers: List[int], value: int) -> int:
        return self.__method1(numbers, value)

    # 基于双指针的解法
    def __method1(self, numbers: List[int], value: int) -> int:
        left, right = 0, len(numbers)
        while left < right:
            if numbers[left] == value:
                numbers[left] = numbers[right - 1]
                right -= 1
            else:
                left += 1
        return left

    # 基于Python语言特性的解法
    def __method2(self, numbers: List[int], value: int) -> int:
        while value in numbers:
            numbers.remove(value)
        return len(numbers)

    def __method3(self, numbers: List[int], value: int) -> int:
        n = len(numbers)
        left = 0
        for right in range(n):
            if numbers[right] != value:
                numbers[left] = numbers[right]
                left += 1
        return left
