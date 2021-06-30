from typing import List


class Solution:
    def singleNumber(self, numbers: List[int]) -> int:
        return self.method1(numbers)

    # 基于栈的解法
    def method1(self, numbers: List[int]) -> int:
        numbers = sorted(numbers)

        while len(numbers) != 1:
            if numbers[-1] == numbers[-2]:
                numbers.pop()
                numbers.pop()
            else:
                return numbers[-1]
        
        return numbers[0]
