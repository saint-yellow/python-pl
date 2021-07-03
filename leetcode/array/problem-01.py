from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int):
        n = len(numbers)
        d = {}
        for i in range(n):
            a = target - numbers[i]
            if numbers[i] in d:
                return [d[numbers[i]], i]
            else:
                d[a] = i
