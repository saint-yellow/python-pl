# LeetCode Problem Nr. 1893: 检查是否区域内所有整数都覆盖

from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        return self.__method1(ranges, left, right)

    def __method1(self, ranges: List[List[int]], left: int, right: int) -> bool:
        n = len(ranges)
        while left <= right:
            for i in range(n):
                if left in range(ranges[i][0], ranges[i][1] + 1):
                    break

                if i == n - 1 and left not in range(ranges[i][0], ranges[i][1] + 1):
                    return False

            left += 1
        return True


if __name__ == "__main__":
    ranges = [[1, 10], [10, 20]]
    left, right = 21, 21

    s = Solution()
    print(s.isCovered(ranges, left, right))
