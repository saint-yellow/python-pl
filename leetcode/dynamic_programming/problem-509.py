# LeetCode Problem Nr. 509: 斐波那契数

class Solution:
    def fib(self, n: int) -> int:
        return self.__method1(n)

    # 基于动态规划的线性级空间复杂度的解法
    def __method1(self, n: int) -> int:
        dp = [0, 1]
        if n == 0 or n == 1:
            return dp[n]
        for i in range(2, n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[-1]

    # 基于动态规划的常数级空间复杂度的解法
    def __method2(self, n: int) -> int:
        if n < 2:
            return n

        p, q, r = 0, 0, 1
        for _ in range(2, n+1):
            p, q = q, r
            r = p + q
        return r
