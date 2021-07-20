from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.__method1(cost)

    def __method1(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            dp.append(min(dp[i - 1], dp[i - 2]) + cost[i])
        print(f"dp={dp}")
        return min(dp[-1], dp[-2])

    def __method2(self, cost: List[int]) -> int:
        dp0, dp1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            dpi = min(dp0, dp1) + cost[i]
            dp0, dp1 = dp1, dpi
        return min(dp0, dp1)

    def __method3(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]

    def __method4(self, cost: List[int]) -> int:
        n = len(cost)
        previousCost = currentCost = 0
        for i in range(2, n + 1):
            nextCost = min(currentCost + cost[i - 1], previousCost + cost[i - 2])
            previousCost, currentCost = currentCost, nextCost
        return currentCost


if __name__ == "__main__":
    s = Solution()
    s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
