# 剑指OfferProblem Nr. 21: 调整数组顺序使奇数位于偶数前面

from typing import List


class Solution:
    def exchange(self, numbers: List[int]) -> List[int]:
        return self.__method1(numbers)

    def __method1(self, numbers: List[int]) -> List[int]:
        if not numbers:
            return numbers

        left, right = 0, len(numbers) - 1
        while left <= right:
            a, b = numbers[left] % 2, numbers[right] % 2
            if a == 1 and b == 0:
                left += 1
                right -= 1
            elif a == 1 and b == 1:
                left += 1
            elif a == 0 and b == 0:
                right -= 1
            else:
                numbers[left], numbers[right] = numbers[right], numbers[left]
                left += 1
                right -= 1
        return numbers


if __name__ == "__main__":
    numbers = [2, 16, 3, 5, 13, 1, 16, 1, 12, 18, 11, 8, 11, 11, 5, 1]
    print(numbers)

    s = Solution()
    print(s.exchange(numbers))
