# LeetCode Problem Nr. 283: 移动零

from typing import List


class Solution:
    def moveZeroes(self, numbers: List[int]) -> None:
        """
        Do not return anything, modify numbers in-place instead.
        """
        self.__method1(numbers)

    def __method1(self, numbers: List[int]) -> None:
        if not numbers:
            return

        n = len(numbers)
        left = right = 0
        while right < n:
            if numbers[right] != 0:
                numbers[left], numbers[right] = numbers[right], numbers[left]
                left += 1
            right += 1


if __name__ == "__main__":
    numbers = [0, 1, 0, 3, 12]
    print(numbers)

    s = Solution()
    s.moveZeroes(numbers)
    print(numbers)
