# LeetCode Problem Nr. 1289: 下降路径最小和II

from typing import List


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        return self.__method1(arr)

    def __method1(self, arr: List[List[int]]) -> int:
        if not arr:
            return 0

        n = len(arr)
        for i in range(1, n):
            for j in range(n):
                arr[i][j] += min(arr[i - 1][:j] + arr[i - 1][j + 1 :])
        print(arr)
        return min(arr[n - 1])


if __name__ == "__main__":
    s = Solution()
    print(s.minFallingPathSum([[1]]))
    print(s.minFallingPathSum([[1, 2], [3, 4]]))
    print(s.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
