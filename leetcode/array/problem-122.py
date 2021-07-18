from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.__method1(prices)

    # 基于贪心策略的解法
    def __method1(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0)
        return result

    # 基于动态规划的解法
    def __method2(self, prices: List[int]) -> int:
        pass
