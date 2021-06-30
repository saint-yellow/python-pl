from typing import List


class Solution:
    def removeElement(self, numbers: List[int], value: int) -> int:
        return self.method1(numbers, value)

    # 基于双指针的解法
    def method1(self, numbers: List[int], value: int) -> int:
        length = len(numbers)
        slow = 0
        fast = 0
        while fast < length:
            if numbers[fast] != value:
                numbers[slow] = numbers[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        return slow

    # 基于Python语言特性的解法
    def method2(self, numbers: List[int], value: int) -> int:
        while value in numbers:
            numbers.remove(value)
        return len(numbers)

