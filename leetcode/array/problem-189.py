# LeetCode Problem Nr. 189: 旋转数组

from typing import List


class Solution:
    def rotate(self, numbers: List[int], k: int) -> None:
        self.__method1(numbers, k)

    def __method1(self, numbers: List[int], k: int) -> None:
        n = len(numbers)
        start = n - k % n
        numbers[:] = numbers[start:] + numbers[:start]


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(numbers)

    s = Solution()
    s.rotate(numbers, 4)
    print(numbers)
