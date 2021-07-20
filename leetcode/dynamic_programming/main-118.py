# LeetCode Problem Nr. 118: 杨辉三角

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return self.__method1(numRows)

    # 基于动态规划的解法
    def __method1(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]
        for row in range(3, numRows + 1):
            level = [1] * row
            for i in range(1, row - 1):
                level[i] = result[row - 2][i - 1] + result[row - 2][i]
            result.append(level)
        return result

    # 基于数学的解法
    def __method2(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret


if __name__ == "__main__":
    s = Solution()
    for i in range(3, 11):
        print(s.generate(i))
