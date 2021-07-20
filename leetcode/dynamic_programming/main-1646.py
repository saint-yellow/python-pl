# LeetCode Problem Nr. 1646: 获取生成数组中的最大值


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        return self.__method1(n)

    def __method1(self, n: int) -> int:
        if n < 2:
            return n

        dp = [0, 1]
        for i in range(2, n + 1):
            if i % 2 == 0:
                dp.append(dp[int(i / 2)])
            else:
                dp.append(dp[int((i - 1) / 2)] + dp[int((i + 1) / 2)])
        return max(dp)
