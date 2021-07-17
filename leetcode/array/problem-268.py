# LeetCode Problem Nr. 268: 丢失的数字

from typing import List


class Solution:
    def missingNumber(self, numbers: List[int]) -> int:
        return self.__method1(numbers)

    def __method1(self, numbers: List[int]) -> int:
        n = len(numbers)
        i = 0
        while i <= n:
            if i not in numbers:
                return i
            i += 1
        return -1

    def __method2(self, numbers: List[int]) -> int:
        sum1 = sum(numbers)
        sum2 = sum(range(len(numbers)+1))
        return sum2 - sum1


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3, 0, 1]))
    print(s.missingNumber([0, 1]))
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
