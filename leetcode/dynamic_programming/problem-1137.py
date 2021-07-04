# LeetCode Problem Nr. 1137: 第N个泰波那契数

class Solution:
    def tribonacci(self, n: int) -> int:
        return self.method1(n)


    def method1(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]

        for i in range(3, n+1):
            dp.append(dp[i-3]+dp[i-2]+dp[i-1])
        return dp[n-1]

    def method2(self, n: int) -> int:
        pass

    def method3(self, n: int) -> int:
        pass

    def method4(self, n: int) -> int:
        pass
