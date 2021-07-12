# LeetCode Problem Nr. 931: 下降路径最小和

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        return self.__method1(matrix)

    def __method1(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j+1]) + matrix[i][j]
                elif j == n-1:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j]) + matrix[i][j]
                else:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1]) + matrix[i][j]
        return min(matrix[n-1])


if __name__ == '__main__':
    s = Solution()
    print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
    print(s.minFallingPathSum([[-19,57],[-40,-5]]))
