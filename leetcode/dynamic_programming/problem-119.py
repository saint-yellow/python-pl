# LeetCode Problem Nr. 119: 杨辉三角II

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return self.__method1(rowIndex)

    # 基于动态规划的解法
    def __method1(self, rowIndex: int) -> list[int]:
        result = [[1], [1, 1]]

        if rowIndex <= 1:
            return result[rowIndex]

        for row in range(2, rowIndex + 1):
            level = [1] * (row + 1)
            for i in range(1, row):
                level[i] = result[row - 1][i - 1] + result[row - 1][i]
            result.append(level)
        return result[rowIndex]


if __name__ == "__main__":
    s = Solution()
    for i in range(3, 11):
        print(s.getRow(i))
