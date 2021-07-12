# LeetCode Problem Nr. 120: 三角形最小路径和

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.__method2(triangle)


    # 基于动态规划的解法
    def __method1(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        levels = len(triangle)

        # 自顶向下的递推
        for i in range(1, levels):
            for j in range(0, i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])

        # 自行实特定的排序算法然后取第一个元素为结果
        return min(triangle[levels-1])

    # 基于动态规划的解法，针对空间复杂度进行优化
    def __method2(self, triangle: List[List[int]]) -> int:
        pass


    # 基于动态规划的解法
    def __method3(self, triangle: List[List[int]]) -> int:
        # to-do: 自顶向上的递推
        pass


if __name__ == '__main__':
    s = Solution()
    # print(s.minimumTotal([[-10]]))
    print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
