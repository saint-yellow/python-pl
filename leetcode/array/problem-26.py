from typing import List


class Solution:
    def removeDuplicates(self, numbers: List[int]) -> int:
        return self.method1(numbers)

    def method1(self, numbers: List[int]) -> int:
        length = len(numbers)
        if length <= 1:
            return length

        slow = 1
        fast = 1
        while fast < length:
            if numbers[fast] != numbers[fast-1]:
                numbers[slow] = numbers[fast]
                slow += 1
            fast += 1
        return slow


