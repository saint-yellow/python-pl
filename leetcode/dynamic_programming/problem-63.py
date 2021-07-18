# LeetCode Problem Nr. 63: 不同路径II

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.__method1(obstacleGrid)

    def __method1(self, obstacleGrid: List[List[int]]) -> int:
        ...


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(s.uniquePathsWithObstacles([[1, 0]]))
    print(s.uniquePathsWithObstacles([[0, 1], [0, 0]]))
