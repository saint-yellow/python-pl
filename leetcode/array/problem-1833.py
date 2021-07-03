from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return self.method1(costs, coins)


    # 基于排序和贪心策略的解法
    def method1(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        count = 0
        for c in costs:
            if c <= coins:
                count += 1
                coins -= c
        return count
