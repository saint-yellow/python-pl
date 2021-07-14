# 剑指Offer Problem Nr. 03: 数组中重复的数字

from typing import List


class Solution:
    def findRepeatNumber(self, numbers: List[int]) -> int:
        return self.__method1(numbers)

    def __method1(self, numbers: List[int]) -> int:
        if not numbers:
            return -1

        d = {}
        for n in numbers:
            if n not in d:
                d[n] = 1
            else:
                return n
        return -1

    def __method2(self, numbers: List[int]) -> int:
        if not numbers:
            return -1

        numbers.sort()
        i, n = 0, len(numbers)
        while i <= n-2:
            if numbers[i] == numbers[i+1]:
                return numbers[i]
            i += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
